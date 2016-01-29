from flask import Flask, url_for, request, render_template
from workout import app
import pymongo
from pymongo import MongoClient
from models import exerciseBook
# import redis



#connect to pymongoodb data store
client = MongoClient('localhost',27017)
db = client.workouts
exercisebook = exerciseBook(db)
#client = MongoClient("localhost:27019")
#connect to redis data store
# r = redis.StrictRedis(host='localhost',port=6379, db=0, charset="utf-8", decode_responses=True)
#other ways to connect to redis
#r=redis.StrictRedis()
#r=redis.StrictRedis('localhost',6379, 0)

@app.route('/workouts', methods=['GET','POST'])
def show_workouts():
	if request.method == 'GET':
		workouts_list = exercisebook.find_exercises()
		return workouts_list
	elif request.method == 'POST':
		name = request.form['name']
		muscle = request.form['muscle']
		sets = request.form['sets']
		exercisebook.insert_exercise(name,muscle,sets)
		newworkout = exercisebook.find_one_exercise(name)
		return newworkout

#pure backend
@app.route('/workouts/<name>', methods=['GET'])
def show_workout(name):
	#read form data and save it
	one_workout = exercisebook.find_one_exercise(name)
	return one_workout


# # #to website
# @app.route('/create', methods=['GET', 'POST'])
# def create():

# 	if request.method == 'GET':
# 		#send the user the form
# 		return render_template('CreateQuestion.html');
# 	elif request.method == 'POST':
# 		#read form data and save it
# 		name = request.form['name']
# 		muscle = request.form['muscle']
# 		sets = request.form['sets']

# 		#store data in data store
# 		# r.set(title + ':question', question)
# 		# r.set(title + ':answer', answer)
# 		exercisebook.insert_exercise(name,muscle,sets)

# 		return render_template('CreatedQuestion.html', name = name, muscle = muscle, sets = sets)
# 	else:
# 		return "<h2>Invalid request</h2>"

# 	return '<h2> This is create </h2>'

# @app.route('/drill/<title>', methods=['GET', 'POST'])
# def drill(title):
# 	if request.method == 'GET':
# 		#send the user the form
# 		question = exercisebook.find_names(name + ":name")
# 		return render_template('AnswerQuestion.html', name = name);
	
# 	elif request.method == 'POST':
# 		#user has attmpted an answer
# 		submittedAnswer = request.form['submittedAnswer']
# 		answer = r.get(title+':answer')

# 		if submittedAnswer == answer:
# 			return render_template('Correct.html')
# 		else:
# 			return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer)
# 	else:
# 		return '<h2>Invalid request</h2>'