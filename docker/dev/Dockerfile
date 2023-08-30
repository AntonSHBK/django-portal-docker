###############
# DEVELOPMENT #
###############

# pull official base image
FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add -y --no-cache\
    postgresql-dev\
    gcc\
    python3-dev\
    musl-dev\
    build-base\
    linux-headers\
    bash\
    zsh

# install dependencies
COPY pip_install_txt/common.txt /tmp/common.txt
COPY pip_install_txt/development.txt /tmp/development.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/development.txt

# set work directory
ENV APP_HOME=/app/backend
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# copy project
COPY ./backend $APP_HOME
