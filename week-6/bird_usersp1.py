"""
Title: Assignment 6.3
Author: Riley Bird
Date: 7/2/2025
Description: Python program to connect to MongoDB and print documents
"""

#import the Mongo Client
from pymongo import MongoClient

#build a connection string to connect to client
client = MongoClient("mongodb+srv://web_335_admin:s3cret@bellevueuniversity.9ygnr7d.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

print(client)

#configure a variable to access the web335DB
db = client['web335DB']

#select collection
collection = db["users"]

#call find function to display all documents in a collection
documents = collection.find()

#for function to display print to screen
for doc in documents:
    print(doc)

#call find_one function to display all results in collection using projections to filter data
print(db.users.find_one({"employeeId": "1011"}))

print(db.users.find_one({"lastName": "Mozart"}))
