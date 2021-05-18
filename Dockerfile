FROM python:3.9.2

COPY . app/

WORKDIR /app

RUN pip install -e .

ENTRYPOINT 'resourcemanager_docker'

EXPOSE 2002