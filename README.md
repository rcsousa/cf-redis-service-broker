# Redis Container Provisioning Service

This project is a simple web service that provides provisioning and deprovisioning of Redis containers using Docker. It is built using the Bottle framework in Python and interacts with the Docker API to manage the containers.

## Installation

To run this project, you need to have the following dependencies installed:

- Python
- Docker

You can install the Python dependencies by running the following command:

```shell
pip install bottle docker pyyaml
```

## Execution

To execute the code, you need to set the following environment variables to the appropriate values for your environment:

- `VCAP_APP_PORT`
- `VCAP_APP_HOST`
- `DOCKER_HOST`
- `REDIS_HOST`

Once the environment variables are set, you can run the code by executing the following command:

```shell
python main.py
```

The web service will start running on the specified host and port.

## How to Contribute

If you want to contribute to this project, you can follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.

## References

- [Bottle Documentation](https://bottlepy.org/docs/dev/)
- [Docker SDK for Python Documentation](https://docker-py.readthedocs.io/en/stable/)
- [YAML Documentation](https://yaml.org/spec/1.2/spec.html)