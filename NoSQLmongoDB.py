# file for practicing MongoDB no SQL database
import pymongo


client = pymongo.MongoClient("mongodb+srv://imailpradeep:ammaacha@cluster0.gujy4jv.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "fname" : "Pradeep",
    "lname" : "Bhaskar",
    "email" : "imailpradeep1@gmail.com",
    "subject" : ["data science", "big data", "data analytics"]
}

database = client['myinfo']
collection = database["Prad"]
collection.insert_one(data)