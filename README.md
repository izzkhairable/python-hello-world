# Python `Hello world` Program

![workflow status](https://github.com/izzkhairable/python-hello-world/actions/workflows/ci.yml/badge.svg?branch=main)
![coverage status](https://raw.githubusercontent.com/izzkhairable/python-hello-world/python-coverage-comment-action-data/badge.svg)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Getting Started

### Running in Local Machine

![img-001](assets/img-001.gif)

#### Install Requirements

```shell
pip install -r requirements.txt
```

#### Running the `Hello world` program

```shell
python src/main.py
```

#### Running Test Cases

```shell
coverage run -m unittest discover -p '*_test.py'
coverage report -m --omit="*_test.py"
```

### Running in Docker 

![img-002](assets/img-002.gif)

#### View the published Docker Images on Docker Hub: [izzkhair/python-hello-world](https://hub.docker.com/repository/docker/izzkhair/python-hello-world/general)
#### View the published Docker Images on GitHub Container Registry: [izzkhairable/python-hello-world](https://github.com/izzkhairable/python-hello-world/pkgs/container/python-hello-world)

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

#### Pull the published images from Github Container Registry

```shell
docker pull ghcr.io/izzkhairable/python-hello-world:main-3.12
docker pull ghcr.io/izzkhairable/python-hello-world:main-3.11
docker pull ghcr.io/izzkhairable/python-hello-world:main-3.10
docker pull ghcr.io/izzkhairable/python-hello-world:main-3.9
```

#### Run container using pulled images in Local Machine

```shell
PYTHON_VERSION=3.12
docker run izzkhair/python-hello-world:main-$PYTHON_VERSION
```

#### Optional: Build image and Run container in Local Machine
```shell
PYTHON_VERSION=3.12
docker build --no-cache --build-arg BASE_IMAGE_VERSION=$PYTHON_VERSION -t python-hello-world-local .
docker run python-hello-world-local
```

## GitHub Actions

![img-005](assets/img-005.png)

#### View the GitHub Action Workflows and Jobs: [izzkhairable/python-hello-world/actions](https://github.com/izzkhairable/python-hello-world/actions)

Currently, the GitHub Actions for this project is configured with a workflow `Build and publish python hello-world` and it
contains two jobs: 

- `python-build`: test, producer coverage, lint, build artifacts, run `hello world` program and upload the artifacts
- `docker-publish`: build, scan, run and publish `hello world` image to docker hub and github cr

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
      - Test with Coverage Unittest
      - Publish Coverage Report to Summary
      - Run python program
      - Upload packaged python artifacts
  docker-publish:
    steps:
      - Download packaged python artifacts
      - Set up QEMU
      - Set up Docker Buildx
      - Authenticate to docker hub
      - Authenticate to github cr
      - Extract tags and labels metadata
      - Build local docker image
      - Run local docker image
      - Run Trivy vulnerability scanner
      - Publish Trivy Output to Summary
      - Push docker image to docker hub and github cr
      - Generate artifact attestation
```

## Dependencies

### Python Packages

```yaml
inspirational-quotes
pyfiglet
ruff
wonderwords
```

### GitHub Actions

```yaml
actions/attest-build-provenance
actions/checkout
actions/download-artifact
actions/setup-python
actions/upload-artifact
aquasecurity/trivy-action
docker/build-push-action
docker/login-action
docker/metadata-action
docker/setup-buildx-action
docker/setup-qemu-action
py-cov-action/python-coverage-comment-action
```

## Contributing

If you'd like to contribute, please fork the repository, create a PR or open an issue.

## Useful Links

* https://github.com/izzkhairable/python-hello-world/actions
* https://hub.docker.com/repository/docker/izzkhair/python-hello-world/general
* https://github.com/izzkhairable/python-hello-world/pkgs/container/python-hello-world

