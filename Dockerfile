ARG BASE_IMAGE_VERSION=latest
FROM python:${BASE_IMAGE_VERSION}

RUN useradd -m defaultuser -u 1000

USER defaultuser

WORKDIR /home/defaultuser/app

COPY ./ .

CMD [ "python", "src/main.py" ]
