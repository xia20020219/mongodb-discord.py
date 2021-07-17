from pymongo import MongoClient
import pymongo
import json

with open('bot_id.json', "r", encoding = "utf8") as datafile:
    jsondata = json.load(datafile)

#checkdatabase is exist ?
def checkdatabase(name, ID):
    cluster = MongoClient(jsondata["mongoclient"])

    db = cluster['discord_bot_database']
    collection = db['member']
    
    result = collection.find_one({str(name) : str(ID)})
    
    if not result:
        
        post = { str(name) : str(ID) , "wallet" : 0, "bank" : 0}

        collection.insert_one(post)
        return False
    
    else:
        return True

#beg $$調整
def begdata(name, ID, begnums):
    cluster = MongoClient(jsondata["mongoclient"])

    db = cluster['discord_bot_database']
    collection = db['member']
    
    id = str(ID)
    membername = str(name)
    
    test = []
    for i in collection.find({membername : id}):
        test.append(i)
    
    print("succeddful")
    wallet = next(item for item in test if item[membername] == id)
    nowwallet = wallet["wallet"]
    
    myquery = { "wallet": nowwallet }
    newvalues = { "$set": { "wallet": nowwallet + begnums } }
    
    print("succeddful")
    collection.update_one(myquery, newvalues)
    
#view bank data
def viewbank(name, ID):
    cluster = MongoClient(jsondata["mongoclient"])

    db = cluster['discord_bot_database']
    collection = db['member']
    
    id = str(ID)
    membername = str(name)
    
    test = []
    for i in collection.find({membername : id}):
        test.append(i)
    
    print("succeddful")
    wallet = next(item for item in test if item[membername] == id)
    
    nowwallet = wallet["wallet"]
    nowbank = wallet["bank"]
    
    print("succeddful")
    return nowwallet, nowbank
    