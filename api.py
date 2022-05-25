from flask import Flask 
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Questions(Resource):

	def get(self):
		data = pd.read_csv('questions.csv')
		data = data.to_dict() #convert datafram to object/dictionary
		return [ data ], 200


api.add_resource(Questions, '/all')

if __name__=='__main__':
	app.run(debug=True)