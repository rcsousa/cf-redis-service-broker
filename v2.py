# coding: utf8.
from bottle import route, run, auth_basic, response
import os, traceback, docker, yaml, json


PORT = int(os.getenv('VCAP_APP_PORT', '9999'))
HOST = str(os.getenv('VCAP_APP_HOST', '0.0.0.0'))
DOCKER_HOST = "<<YOUR DOCKER HOST>>:<<DOCKER API PORT>>"
REDIS_HOST = "<<YOUR REDIS HOST>>"

def check_pass(username, password):
    return True

def check_container(container_name):
    try:
    	c = docker.Client(base_url=DOCKER_HOST,version='1.21')
    	result = c.inspect_container(container_name)
	if result['State']['Status']:
    		return "Container exists"
    except:
	return "Container not Found"

def check_host_port(container_name):
    try:
    	c = docker.Client(base_url=DOCKER_HOST,version='1.21')
        result = c.inspect_container(container_name)
	host_port = result['NetworkSettings']['Ports']['6379/tcp'][0]['HostPort']
        return host_port
    except:
        return "Host Port not Found"

def default_async_answer():
    print traceback.format_exc()
    response.status = 422
    result = {"error": "AsyncRequired","description": "This service plan requires client support for asynchronous service operations."}
    return result

    
@route('/v2/catalog', method='GET')
@auth_basic(check_pass)
def catalog():
    with open('service_catalog.yml', 'r') as f:
        yaml_settings = yaml.load(f)
    json_settings = json.dumps(yaml_settings)
    data = json.loads(json_settings)
    return data['catalog']


@route('/v2/service_instances/:instance_id', method='PUT')
@auth_basic(check_pass)
def provisioning_service_instances(instance_id):
    try:
	c_status =  check_container(str(instance_id))
	if c_status == "Container exists":
		response.status = 409
		result = {}
		return result
	else:
    		password = "pw_"+str(hash(instance_id[0-10]))
    		host = str(hash(instance_id[0-10]))
    		c = docker.Client(base_url=DOCKER_HOST,version='1.21')
    		container = c.create_container(image='tutum/redis',name=instance_id, hostname=host, environment=["REDIS_PASS="+password], ports=[(6379,'tcp')])
    		started_container = c.start(container, port_bindings={6379:('0.0.0.0',)})
		if container:
			response.status = 201
    			result = { "dashboard_url": container['Id'] }
    			return result
    except:
	result = default_async_answer()
	return result

@route('/v2/service_instances/:instance_id', method='DELETE')
@auth_basic(check_pass)
def deprovisioning_service_instances(instance_id):
    try:
       	c_status =  check_container(str(instance_id))
	if c_status == "Container not Found":
        	response.status = 410
                result = {}
                return result
	else:
    		c = docker.Client(base_url=DOCKER_HOST,version='1.21')
		check = c.stop(str(instance_id))
		container  = c.remove_container(str(instance_id))
        	if container:
        		response.status = 200
                	result = { }
                	return result
    except:
	result = default_async_answer()
	return result

@route('/v2/service_instances/:instance_id/service_bindings/:binding_id', method='PUT')
@auth_basic(check_pass)
def binding_service_instances(instance_id, binding_id):
    try:
        c_status =  check_container(str(instance_id))
        password = "pw_"+str(hash(instance_id[0-10]))
        host = str(hash(instance_id[0-10]))
        host_port = check_host_port(str(instance_id))
        response.status = 201
	result =     {
      			"credentials": {
        		"password": password,
        		"host": REDIS_HOST,
        		"port": host_port,
      			}
    		     }
        return result
    except:
	result = default_async_answer()
	return result

@route('/v2/service_instances/:instance_id/service_bindings/:binding_id', method='DELETE')
@auth_basic(check_pass)
def binding_service_instances(instance_id, binding_id):
    try:
        response.status = 200
        result =     {}
        return result
    except:
        result = default_async_answer()
	return result

run(host=HOST, port=PORT)
