# Python `Hello world` Program

![example workflow](https://github.com/izzkhairable/python-hello-world/actions/workflows/ci.yml/badge.svg?branch=main)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Getting Started

### Running in Local Machine

#### Install Requirements

```shell
pip install -r requirements.txt
```

#### Running the `Hello world` program

```shell
python main.py
```

#### Running Test Cases

```shell
python -m unittest src.test.hello_world_test
```

### Running in Docker 

To ensure that the `Hello world` program is `backward compatible`, each new increment of the 
`Hello world` python program would result in the publishing of 4 docker images for the 
follow python versions:

> Python version of `Hello world` images available: **3.12, 3.11, 3.10, 3.9**



#### Pull the published images from Docker Hub

```shell
docker pull izzkhair/python-hello-world:main-3.12
docker pull izzkhair/python-hello-world:main-3.11
docker pull izzkhair/python-hello-world:main-3.10
docker pull izzkhair/python-hello-world:main-3.9
```

#### Run container using pulled images in Local Machine

```shell
PYTHON_VERSION=3.12
docker run izzkhair/python-hello-world:main-$PYTHON_VERSION python main.py
```

#### Optional: Build image and Run container in Local Machine
```shell
docker build --build-arg BASE_IMAGE_VERSION=3.12 -t python-hello-world-local .
docker run python-hello-world-local
```

## GitHub Actions

Currently,the GitHub Actions for this project is configured with a workflow `Build and publish python hello-world` and it
contains two jobs: 

- `python-build`: test, lint, build artifacts, run `hello world` program and upload the artifacts
- `docker-publish`: builds and publish `hello world` image to docker hub, scans for vulnerability and run the image

```yaml
name: Build and publish python hello-world
jobs:
  python-build:
    steps:
      - Checkout to current branch
      - Set up Python X.YZ
      - Display Python version
      - Install dependencies
      - Lint with Ruff
      - Test with Unittest
      - Run python program
      - Upload packaged python artifacts
  docker-publish:
    steps:
      - Download packaged python artifacts
      - Authenticate to docker hub
      - Extract tags and labels metadata
      - Build and publish docker image
      - Scan container for vulnerabilities
      - Run docker image
```


## Contributing

If you'd like to contribute, please fork the repository or open an issue and use a feature branch.


