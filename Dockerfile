# pull official base image
FROM python:3.9.5-slim-buster

# Install prerequisites
RUN apt-get update && apt-get install -y \
    curl

# set work directory
WORKDIR /app/
# set environment variables
COPY ./pyproject.toml ./poetry.lock* /app/

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-dev

# copy project
COPY . /app