###############
# DEVELOPMENT #
###############

# pull official base image
FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add build-base linux-headers
RUN apk add --no-cache bash

# install dependencies
COPY requirements/common.txt /tmp/common.txt
COPY requirements/development.txt /tmp/development.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/development.txt

# set work directory
RUN mkdir /app
WORKDIR /app

# copy project
COPY . .

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh