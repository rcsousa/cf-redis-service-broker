# Redis Service Broker

This is a simple Redis Service Broker that can be used to provision Redis instances on a Docker host. It is built using Python and the Bottle web framework.

## Dependencies

This project requires the following dependencies:

- Python 2.7
- Bottle
- Docker SDK for Python

## Installation

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To run the Redis Service Broker, execute the following command:

```
python redis_broker.py
```

By default, the broker will listen on port 9999. You can change this by setting the `VCAP_APP_PORT` environment variable.

## API

The Redis Service Broker provides the following API endpoints:

### GET /v2/catalog

Returns the catalog of services offered by the broker.

### PUT /v2/service_instances/:instance_id

Provisions a new Redis instance with the given `instance_id`.

### DELETE /v2/service_instances/:instance_id

Deprovisions the Redis instance with the given `instance_id`.

### PUT /v2/service_instances/:instance_id/service_bindings/:binding_id

Binds a Redis instance with the given `instance_id` to an application with the given `binding_id`.

### DELETE /v2/service_instances/:instance_id/service_bindings/:binding_id

Unbinds a Redis instance with the given `instance_id` from an application with the given `binding_id`.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## References

- [Bottle documentation](https://bottlepy.org/docs/dev/)
- [Docker SDK for Python documentation](https://docker-py.readthedocs.io/en/stable/)