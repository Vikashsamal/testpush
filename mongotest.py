import pymongo
client = pymongo.MongoClient("mongodb+srv://Bikash:Loveyoubaby@bikashmacbook.ndlu6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Bikash",
    "Surname" : 'Samal',
    "Email ID" : "vks.samal1992@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

