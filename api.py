from flask import Flask 
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)



class Questions(Resource):

	def get(self):
		pass

	def post(self):
		pass

class Home(Resource):

	def get(self):
		return 'API made by Eusébio Simango'

api.add_resource(Questions, '/api/questions/all')
api.add_resource(Home, '/api')

if __name__=='__main__':
	app.run(debug=True)