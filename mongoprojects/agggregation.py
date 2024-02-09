import pymongo.errors
from pymongo import MongoClient

def get_connection ():
    dbconn=MongoClient("mongodb://localhost:27017/")
    return dbconn

def get_db_details(dbconn):
    db_details=dbconn["video_game"]
    #print(db_details)
    coll_details=db_details["products"]
    #print(coll_details)
    return coll_details

def get_match(coll):
    return coll.aggregate([ {"$match":{"tags":"Beauty"}},{"$group":{"_id":"$seller_id"}},{"$project":{"beauty_product_seller_id":"$_id","_id":0}}])
    #return coll.aggregate([ {"$unwind":"$tags"},{"$group":{"_id":"$tags","seller_id":{"$addToSet":"$seller_id"}}},{"$project":{"tag_name":"$_id","seller_id":1,"_id":0}}])
    #return coll.aggregate([ {"$unwind":"$tags"},{"$group":{"_id":"$tags","seller_id_count": { "$sum": 1 }}}]) #why incorrect????
    #return coll.aggregate([{"$unwind": "$tags"}, {"$group": {"_id": "$tags", "seller_id": {"$addToSet": "$seller_id"}}},{"$project": {"tag_name": "$_id", "num_seller": {"$size": "$seller_id"}, "_id": 0}}])
    #return coll.aggregate([{"$group": {"_id": "$seller_id", "product_name": {"$push": "$name"}}},
     #                      {"$lookup": {"from": "users", "localField": "_id", "foreignField": "_id", "as": "sellers"}},
      #                     {"$project": {"product_name": "$product_name", "sellers_name": "$sellers.name","_id":0}}])

def print_cursor(cursor):
    for r in cursor:
     print(r)


coll=get_db_details(get_connection())
merge_cursor=get_match(coll)
print_cursor(merge_cursor)
