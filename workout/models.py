import string

class exerciseBook(object):
	def __init__(self, database):
		self.db = database
		self.myexercises = database.myexercises

	def find_exercises(self):
		l = []
		for each_exercise in self.myexercises.find():
			l.append({'name':each_exercise['name'].encode('utf-8'), 'muscle':each_exercise['muscle'].encode('utf-8'), 'sets':each_exercise['sets'].encode('utf-8')})		
		return str(l)

	def insert_exercise(self, name, muscle, sets):
		newexercise = {'name':name, 'muscle':muscle, 'sets':sets}
		self.myexercises.insert(newexercise)

	def find_one_exercise(self, name):
		name_dict = self.myexercises.find_one({'name':name})
		return str({'name':name_dict['name'].encode('utf-8'), 'muscle':name_dict['muscle'].encode('utf-8'), 'sets':name_dict['sets'].encode('utf-8')})