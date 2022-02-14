from flask import Flask
from flask_restful import Resource, Api
import datetime
from flask import request
from functools import wraps
 
 
app = Flask(__name__)
api = Api(app)
 
 
def time(function=None):
 
    @wraps(function)
    def wrapper(*args, **kwargs):
        s = datetime.datetime.now()
        _ = function(*args, **kwargs)
        e = datetime.datetime.now()
        print("Execution  Time : {} ".format(e-s))
        return _
    return wrapper 
 
def monitor(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        _ = function(*args, **kwargs)
        print("Ip Address  : {} ".format(request.remote_user))
        print("Cookies : {} ".format(request.cookies))
        print(request.user_agent)
        return _
    return wrapper
 
 
class HelloWorld(Resource):
 
    @monitor
    def get(self):
        return {'hello': 'world'}
 
api.add_resource(HelloWorld, '/')
 
if __name__ == '__main__':
    app.run(debug=True)