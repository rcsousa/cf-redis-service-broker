# Redis Service Broker

This is a simple Redis Service Broker that can be used to provision Redis instances on a Docker host. It is built using Python and the Bottle web framework.

## Dependencies

This project requires the following dependencies:

- Python 2.7
- Docker
- Bottle
- PyYAML

## Installation

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To start the Redis Service Broker, run the following command:

```
python app.py
```

By default, the service broker will listen on port 9999. You can change this by setting the `VCAP_APP_PORT` environment variable.

## API

The Redis Service Broker provides the following API endpoints:

### GET /v2/catalog

Returns the service catalog.

### PUT /v2/service_instances/:instance_id

Provisions a new Redis instance.

### DELETE /v2/service_instances/:instance_id

Deprovisions an existing Redis instance.

### PUT /v2/service_instances/:instance_id/service_bindings/:binding_id

Binds an existing Redis instance to an application.

### DELETE /v2/service_instances/:instance_id/service_bindings/:binding_id

Unbinds an existing Redis instance from an application.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.