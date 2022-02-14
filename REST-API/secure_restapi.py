from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

USER_DATA = {
	"admin": "SuperSecretPwd"
}
#route to verify the password
@auth.verify_password
def verify(username, password):
	if not(username and password):
		return False
	return USER_DATA.get(username) == password

class PrivateResource(Resource):
	@auth.login_required
	def get(self):
		return {"How's the Josh": "High"}

api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
	app.run(debug=True)
	