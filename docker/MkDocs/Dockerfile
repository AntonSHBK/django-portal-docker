###############
# MkDocks #
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
COPY pip_install_txt/mkdocs.txt /tmp/mkdocs.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/mkdocs.txt

# set work directory
ENV APP_HOME=/app/wiki
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# copy project
COPY ./wiki $APP_HOME