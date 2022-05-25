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

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argumnt('question', required=True)
		parser.add_argumnt('optionA', required=True)
		parser.add_argumnt('optionB', required=True)
		parser.add_argumnt('optionC', required=True)
		parser.add_argumnt('optionD', required=True)
		parser.add_argumnt('rightAnswer', required=True)
		
		args = parser.parse_args()
		
		newData = pd.DataFrame({
				'question': args['question'],
				'optionA': args['optionA'],
				'optionB': args['optionB'],
				'optionC': args['optionC'],
				'optionD': args['optionD'],
				'rightAnswer': args['rightAnswer']
			})

		data = pd.read_csv('questions.csv')
		data = data.append(newData, ingnore_index=True)
		data.to_csv('questions.csv', index=False)
		return [ data.to_dict() ], 200

api.add_resource(Questions, '/all')


if __name__=='__main__':
	app.run(debug=True)