# Bottle Redis Service Broker

This is a Python implementation of a Redis Service Broker using Bottle and Docker. It provides a RESTful API that allows you to provision and bind Redis instances.

## Dependencies

This project requires the following dependencies:

- Python 2.7
- Bottle
- Docker
- PyYAML

## Installation

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To start the service broker, run the following command:

```
python app.py
```

By default, the service broker will listen on port 9999. You can change this by setting the `VCAP_APP_PORT` environment variable.

## API

The service broker provides the following RESTful API:

### GET /v2/catalog

Returns the service catalog.

### PUT /v2/service_instances/:instance_id

Provisions a new Redis instance.

### DELETE /v2/service_instances/:instance_id

Deprovisions a Redis instance.

### PUT /v2/service_instances/:instance_id/service_bindings/:binding_id

Binds a Redis instance to an application.

### DELETE /v2/service_instances/:instance_id/service_bindings/:binding_id

Unbinds a Redis instance from an application.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request.

## References

- [Bottle documentation](https://bottlepy.org/docs/dev/)
- [Docker documentation](https://docs.docker.com/)
- [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)