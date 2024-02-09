import pymongo.errors
from pymongo import MongoClient
data={
    "name": "champ_updated",
    "health": 5,
    "energy": "100",
    "items": [
        {
            "name": "health_potion",
            "quantity": 2,
            "effects": [
                {
                    "heal": 10
                }
            ]
        }
    ],
    "exists": 1

}
criteria= {"$or":[{"name":"champ","health":{"$gte":0,"$lte":5},"health":{"$type":"number","$exists":True},"exists":{"$exists":True}}]}

def get_connection ():
    dbconn=MongoClient("mongodb://localhost:27017/")
    return dbconn

def get_db_details(dbconn):
    db_details=dbconn["BucketListsUSA"]
    #print(db_details)
    coll_details=db_details["temp_video"]
    #print(coll_details)
    return coll_details

def get_count(coll_details):
    count=coll_details.count_documents({})
    return count

def insert_data_coll(db_coll,data):
    ins_res=db_coll.insert_one(data)
    return ins_res

def search_results(db_coll,criteria):
    result_search=db_coll.find(criteria)
    return result_search


def update_result(db_collection):
     res_upd=db_collection.update_one( {"name":"champ"},{"$set":{"items.0.name":"health_portionsss"}})
     return res_upd


def delete_record(db_collection):
    res_del = db_collection.delete_one({ "name": "champ_updated"})
    return res_del

if __name__=='__main__':

    con=get_connection()
    db_coll=get_db_details(con)
    count=get_count(db_coll)
    print(count)
    if count==0:

        try:
            res=insert_data_coll(db_coll,data)
            if res.acknowledged==bool(1):
                print("Data Inserted Successfully")
            else:
                print("Error in adding data")
        except pymongo.errors.WriteError:
            print("Error in exception")

    search_rec=search_results(db_coll,criteria)
    #print(search_rec)
    counts = 0
    for rr in search_rec:

        if search_rec.alive:
         print("*" * 3 + "page=", counts)
         counts=counts+1

         print(" Firstname= "+rr["firstname"]+" lastname= "+rr["lastname"])
    else:
     res=search_results(db_coll,criteria)
     try:
         print(update_result(db_coll))
        # delete_record(db_coll)
     except:
         print("error in update")
     print(res)
     print("hii out cursor")
     for r in res:
         print("hii in cursor")
         print(r["name"])

