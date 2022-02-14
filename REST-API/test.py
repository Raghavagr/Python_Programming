from run import app
import json
import unittest

class FlaskTest(unittest.TestCase):
	#Check for response 200
	def test_inde(self):
		tester = app.test_client(self) #tester object
		response = tester.get("/")
		statuscode = response.status_code
		self.assertEqual(statuscode, 200)

	#check if the content return is application JSON
	def test_index_content(self):
		tester = app.test_client(self)
		response = tester.get("/")
		self.assertEqual(response.content_type, "application/json")

	#check the Data returned
	def test_index_data(self):
		tester = app.test_client(self)
		response = tester.get("/")
		self.assertTrue(b'Message' in response.data)

if __name__ == '__main__':
	unittest.main()
