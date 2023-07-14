# Service Broker for Redis using Docker

This is a Python script that implements a service broker for Redis using Docker. It is designed to be used with Cloud Foundry, but can be used with any platform that supports service brokers.

## Dependencies

This script requires the following dependencies:

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

To run the service broker, execute the following command:

```
python service_broker.py
```

By default, the service broker will listen on port 9999. You can change this by setting the `VCAP_APP_PORT` environment variable.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions.

## References

- [Bottle documentation](https://bottlepy.org/docs/dev/)
- [Docker SDK for Python documentation](https://docker-py.readthedocs.io/en/stable/)
- [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)