# cf-redis-service-broker

To deploy this service broker on bluemix, follow these steps:

1. Clone this repository : git clone https://github.com/rcsousa/cf-redis-service-broker.git
2. Update v2.py with your host info:
	
	DOCKER_HOST = "<<YOUR DOCKER HOST>>:<<DOCKER API PORT>>"
	REDIS_HOST = "<<YOUR REDIS HOST>>"

3. Update the manifest.yml file with you app information (name and domain depending on your bluemix region)
4. login to your bluemix account:

	ie: cf login api.eu-gb.mybluemix.net

5. Publish your service broker:

	cf push
