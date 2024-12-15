from pymongo import MongoClient

# Configura la conexión a MongoDB Atlas
mongo_uri = "mongodb+srv://caalsandovalgu:d2golPqRt3b2bKn7@cluster0.m9gzv.mongodb.net/"
client = MongoClient(mongo_uri)
db = client.get_database("litcrit")