"""
Title: Assignment 7.3
Author: Riley Bird
Date: 7/13/2025
Description: Python program to connect to MongoDB
"""

#import the Mongo Client
from pymongo import MongoClient
import datetime

#build a connection string to connect to client
client = MongoClient("mongodb+srv://web_335_admin:s3cret@bellevueuniversity.9ygnr7d.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

print(client)

#configure a variable to access the web335DB
db = client['web335DB']

#create an update query to change the user's email address
db.users.update_one(
  {"employeeId": "1007"},
  {
    "$set":{
      "email": "jobach@me.com"
    }
  }
)

#prove update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employee": "1007"}))

#build a query to remove a user document
result = db.users.delete_one({
  "employeeId": "1007"
})

#display the results of the query
print(result)

#prove the delete worked by searching the collection for the deleted document
print(db.users.find_one({"employeeId": "1007"}))
