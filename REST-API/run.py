from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
	def __init__(self):
		pass

	def get(self):
		return json.dumps({"Message": "Fine"})

api.add_resource(Helloworld, '/')

if __name__ == '__main__':
	app.run(debug=True)