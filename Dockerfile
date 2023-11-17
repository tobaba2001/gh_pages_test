FROM python:3.8-slim-buster

ARG LISTENER=3000
ENV LISTENERENV=${LISTENER}

RUN chmod +rwx /usr/local/bin/*

WORKDIR /opt/app
RUN pip install --upgrade pip
RUN pip install -U Flask waitress==2.0.0 flask-json-logger==0.1.0

COPY ./app /app

EXPOSE ${LISTENER}

ENTRYPOINT python3 /app/run.py ${LISTENERENV}