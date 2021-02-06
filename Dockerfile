FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc g++ \ 
        make musl-dev python3-dev jpeg-dev zlib-dev libffi-dev && \
    pip install --upgrade pip==20.2.4 && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps && \
    apk add --no-cache bash

COPY . /app/

WORKDIR /app/src

ENTRYPOINT ["bash", "../docker-entrypoint.sh"]
