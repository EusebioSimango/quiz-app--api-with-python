from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions'
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
		

		return str(questions)
		
	def post(self):
		pass

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
	app.run()
