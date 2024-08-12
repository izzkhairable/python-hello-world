# Python `Hello world` Program

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

To ensure for python version `backward compatibility`, each new increment of the 
`Hello world` python program would result in the publishing of 4 docker images for the 
follow python versions:

> Version of Python images available: **3.12, 3.11, 3.10, 3.9**

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

