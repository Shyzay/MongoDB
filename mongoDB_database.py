# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:47:37 2018

@author: KELS
"""

import json
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client.New_York_Times_Top_StoriesDB
collection = db.topStories
articles = [

    {"_id": 1, "article_title": "We Are Not The Resistance", "article_link": "https://www.nytimes.com/2018/09/21/opinion/sunday/resistance-kavanaugh-trump-protest.html?action=click&module=Opinion&pgtype=Homepage", "byline": "Michelle Alexander", "published_date": "Sept. 21, 2018"},
    {"_id": 2, "article_title": "Coders of Kentucky", "article_link": "https://www.nytimes.com/2018/09/21/opinion/sunday/silicon-vall0ey-tech.html?action=click&module=Opinion&pgtype=Homepage", "byline": "Arlie Hochschild", "published_date": "Sept. 21, 2018"},
    {"_id": 3, "article_title": "Making Tariffs Corrupt Again", "article_link": "https://www.nytimes.com/2018/09/20/opinion/tariffs-trump-corrupt.html?action=click&module=Opinion&pgtype=Homepage", "byline": "Paul Krugman", "published_date": "Sept. 20, 2018"},
    {"_id": 4, "article_title": "Democracy Will Still Surprise Us", "article_link": "https://www.nytimes.com/2018/09/21/opinion/western-democracy-trump-challenges.html?action=click&module=Opinion&pgtype=Homepage", "byline": "Roger Cohen", "published_date": "Sept. 21, 2018"},
    {"_id": 5, "article_title": "We Need to Hear From Christine Blasey Ford", "article_link": "https://www.nytimes.com/2018/09/20/opinion/columnists/christine-blasey-ford-testify-brett-kavanaugh-hearing.html?action=click&module=Opinion&pgtype=Homepage", "byline": "Michelle Goldberg", "published_date": "Sept. 20, 2018"}
]

# collection.insert_many(articles)
print('***************************************', '\n')
# Printing the number of documents in the collections

print("The number of documents in my collection: ", collection.count_documents({}))
print('***************************************', '\n')

# query entries in the collection using regex
myquery = {"article_title": {"$regex": "^We"}}

mydoc = collection.find(myquery)
print("All entries with 'We' in field 'article_title': ", collection.count_documents(myquery))

# Print all entries
print('***************************************', '\n')
print('Printing all entries:')

# iterate through the collection and read the entries
for x in collection.find():
    print(json.dumps(x, indent=2))