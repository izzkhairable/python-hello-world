ARG BASE_IMAGE_VERSION=latest
FROM python:${BASE_IMAGE_VERSION}

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ /app

CMD [ "python", "main.py" ]