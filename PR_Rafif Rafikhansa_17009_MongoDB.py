import pymongo

print("          Program Demo CRUD MongoDB Database ")
print("         Rafif Rafikhansa (19/447315/SV/17009)            ")
print("========================================================\n")
print("Menu operasi database:")
print("1. Create database & tabel")
print("2. Insert data")
print("3. Select/search data")
print("4. Update data")
print("5. Delete data")
menu=input("\nSilahkan pilih operasi ( 1/2/3/4/5 ) ? ")
print("\nOperasi : " + menu)

if menu=='1' :
    print("\nCreate database dan tabel")
    # create a database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Project_MongoDB"]
    print(client.list_database_names())
    
    # create a collection
    col = db ["management_user"]
    print(db.list_collection_names())

    #create a content or insert
    mylist = [
        { "_id": 1, "username": "Aly Akbar", "password": "11111111", "status": "active"},
        { "_id": 2, "username": "Gilang Durhaka", "password": "00000000", "status": "non-active"}
        ]
    x = col.insert_many(mylist)
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    for x in col.find():
        print(x)

elif menu=='2' :
    print("\nInsert data")
    #insert
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Project_MongoDB"]
    col = db ["management_user"]
    mylist = { "_id": 3, "username": "Rio", "password": "12345678", "status": "active" }
    x = col.insert_one(mylist)
    print(x.inserted_id)
    
    mydict = { "_id": 4, "username": "Reiner", "password": "66666666", "status": "non-active" }

    x = col.insert_one(mydict)

elif menu=='3' :
    print("\nSelect/search data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Project_MongoDB"]
    col = db ["management_user"]
    #search data
    myquery = { "username": "Rio" }
    mydoc = col.find(myquery)
    for x in mydoc:
        print(x)

elif menu=='4' :
    print("\nUpdate data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Project_MongoDB"]
    col = db ["management_user"]
    #update data
    myquery = { "username": "Rio" }
    newvalues = { "$set": { "username": "Brenda" } }
    col.update_one(myquery, newvalues)
    #print "customers" after the update:
    for x in col.find():
        print(x)

elif menu=='5' :
    print("\nDelete data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Project_MongoDB"]
    col = db ["management_user"]
    #delete data
    myquery = { "password": "66666666" }
    col.delete_one(myquery)