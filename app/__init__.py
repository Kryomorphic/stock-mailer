import os
import logging
import socket
import sys
from logging.handlers import SysLogHandler
from flask import Flask, request
from dotenv import load_dotenv
from traceback import format_exception

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

from config import Config

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.config.from_object(Config)


class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True

    def error_handler(etype, value, tb):
        exc = ''.join(format_exception(etype, value, tb))
        app.logger.exception(exc)

    # Install exception handler
    sys.excepthook = error_handler


from app import routes
app.register_blueprint(routes.stock)
