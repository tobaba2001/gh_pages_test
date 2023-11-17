import logging
import os
import sys
from logging.config import dictConfig

from flask import Flask, url_for, render_template
from pythonjsonlogger import jsonlogger
from waitress import serve

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

dictConfig({
    "version": 1,
    "disable_existing_loggers": "true",
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s",
            "datefmt": "%Y-%m-%dT%T.%3N%z"
        }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json"
        }
    },
    "loggers": {
        "": {
            "handlers": ["json"],
            "level": 20
        }
    }
})

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def hello():
    app.logger.info("Hello World from github pages")
    return "Hello World from A web app"

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except:
        port: 8000
    serve(app, host='0.0.0.0', port=port)