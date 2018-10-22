FROM ubuntu:18.04

MAINTAINER Pedro Silva "ams.pedro@gmail.com"

RUN apt-get update -y && \
    apt-get install -y libpq-dev && \
    apt-get install -y gcc musl-dev && \
    apt-get install -y python-pip python-dev

RUN pip install --no-binary :all: psycopg2


COPY requirements/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]
