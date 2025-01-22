import pymongo
url = 'mongodb+srv://kaushalpratap:fjIZxzNzXnMtfzsW@synnefocluster.vporf.mongodb.net/'
client = pymongo.MongoClient(url)
db = client['imagedatabase']