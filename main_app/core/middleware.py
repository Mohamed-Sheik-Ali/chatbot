from werkzeug.wrappers import Response, request
from flask import session


class Middleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # print(f'Environment => {environ} <==> Response => {start_response}')
        return self.app(environ, start_response)
