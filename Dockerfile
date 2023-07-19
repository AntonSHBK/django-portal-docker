# pull official base image
FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ARG CUID=1000
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN apt-get update && \
#     apt-get install -y \
#         gcc \
#         libpq-dev \
#         postgresql-dev \
#         python3-dev \
# RUN rm -rf /var/lib/apt/lists/* && apt-get clean

# install dependencies
COPY requirements/common.txt /tmp/common.txt
COPY requirements/development.txt /tmp/development.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/development.txt

# set work directory
RUN mkdir /app
WORKDIR /app

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# copy project
COPY . .

EXPOSE 8000