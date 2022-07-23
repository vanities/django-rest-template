FROM python:3.10.5

ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        graphviz libgraphviz-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD requirements.txt /
RUN pip install -r /requirements.txt \
    && rm -rf /requirements.txt

ADD . /app
