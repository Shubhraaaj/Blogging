__author__ = 'Shubhraj'
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

# students = collection.find({})
# student_list = []
#
# for student in students:
#     student_list.append(student)

#List comprehension
students = [student['name'] for student in collection.find({}) if student['marks'] == 100]
print(students)