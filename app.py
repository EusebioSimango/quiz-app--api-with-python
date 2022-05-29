from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
import json


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions' local db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dmxqmqvaaekgmv:5c90e25e6c4c748186b6fd1c0bd6b53079395d3150fa7d93abbed5b4a22337b4@ec2-44-196-174-238.compute-1.amazonaws.com:5432/d80n33rfkrucbs'
db = SQLAlchemy(app)
api = Api(app)

class Questions(db.Model):
	question = db.Column(db.String(200), unique=True, primary_key=True, nullable=False)
	optionA = db.Column(db.String(140), unique=False, nullable=False)
	optionB = db.Column(db.String(140), unique=False, nullable=False)
	optionC = db.Column(db.String(140), unique=False, nullable=False)	
	optionD = db.Column(db.String(140), unique=False, nullable=False)
	rightAnswer = db.Column(db.String(1), unique=False, nullable=False)

	def __repr__(self):
		return str({
					'question': self.question,
					'optionA': self.optionA,
					'optionB': self.optionB,
					'optionC': self.optionC,
					'optionD': self.optionD,
					'rightAnswer': self.rightAnswer,
				})


class QuestionsRepository(Resource):
	def get(self):
		questions = Questions.query.all()
		questions = str(questions).replace("'", '"')
		questions = json.loads(questions)

		return questions

	def post(self):
		dataJson = request.get_json()
		question = dataJson['question']
		optionA	 = dataJson['optionA']
		optionB	 = dataJson['optionB']
		optionC	 = dataJson['optionC']
		optionD	 = dataJson['optionD']
		rightAnswer	 = dataJson['rightAnswer']
		newQuestion = Questions(question=question, optionA=optionA, optionB=optionB, optionC=optionC, optionD=optionD, rightAnswer=rightAnswer)
		db.session.add(newQuestion)
		return db.session.commit()
		
 

class Home(Resource):

	def get(self):
		return 'API made by Eusébio Simango'


class NotFounded(Resource):

	def get(self):
		return { 'error':  '404 Not Founded'}

	def post(self):
		return { 'error':  '404 Not Founded'}


api.add_resource(QuestionsRepository, '/api/questions/all')
api.add_resource(Home, '/')

if __name__=='__main__':
	app.run(debug=True)
