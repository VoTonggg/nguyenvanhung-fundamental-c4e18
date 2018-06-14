from pymongo import MongoClient


mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# Connect to database

client = MongoClient(mongo_uri)

# Get database

db = client.get_default_database()

posts = db['posts']

# all_posts = posts.find()

# for post in all_posts:
#     print(post)

new_post = {
    "title" : "Châm ngôn cuộc sống",
    "author" : "Võ Tòng",
    "content" : "Hãy cứ sai đi rồi cuộc đời này bốc shit !!! "
}

posts.insert_one(new_post)