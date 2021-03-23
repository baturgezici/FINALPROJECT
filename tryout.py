import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["User"]

myq = {"username":"batur"}
a = mycol.find()[0]
print(a)