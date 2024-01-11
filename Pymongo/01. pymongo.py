
import pymongo

#Initialize a client to interact with the database
client = pymongo.M3ongoClient()

#Create/append to a database.  Database will not be visible in Compass if no collection created yet
mydb1 = client['mydb1']

#Create a collection, if already exits, then append
mycol = mydb1["people"]

#create data to add to the collection. After which refresh mongoDB Compass to see the database
#In this case, these datas are known as posts
data = {'fName': "Ibrahim", "sName":"Suleiman", "id":'001'}
mycol.insert_one(data)

#Add a list of data to the collection
d1 = {'fName': "Kabir", "sName":"Mustapha", "id":'002'}
d2 = {'fName': "Jane", "sName":"Doe", "id":'003'}
datalist = [d1,d2]
mycol.insert_many(datalist)
# x = mycol.insert_many(datalist2)

#Access the IDs of newly added data to the collection
datalist2 = [{'fName': "Sammy", 'sName':"Jay", 'id':'004'},{'fName': 'Reily', 'sName':"Freeman", 'id':'005'}]
x = mycol.insert_many(datalist2)
print(x.inserted_ids)


#View existing database names
x = client.list_database_names()
print(f'The available databases are: {x}')

#View all existing collection within an existing database
x = mydb1.list_collection_names()     #where mydb1 is the name of the particular database
print(f'The available collections are {x}')

print(f'mydb1 collections: {x}')
print(f'local collections: {y}')



#===================== QUERY DATABASE ========================
#--------- View all data in a collection. Output will be as a dictionary, key-value pair
for x in mycol.find():
    print(f'Available data ---->>> {x}')
    print(f'{list(x.keys())}')
print("================= &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& =================")

#--------- View just one data in a collection, first occurence.
x = mycol.find_one()
print(f'First avalilabe data ---->>> {x}')
print("================= &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& =================")

#--------Adding conditions to filter contents of a dictionary
for x in mycol.find({'id':"002"}):    #todosCol.find({'age':{"$gte":30}}) ---> age(int) >= 30
    print(f'Filtered data ---->>> {x}')

#--------- View just one data in a collection, first occurence.
x = mycol.find_one({'id':"002"})
print(f'First avalilabe data ---->>> {x}')
print("================= &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& =================")


#--------- Delete data from a collection -------------
# result = mycol.delete_one({"id":"002"})  #Delete the first occurence only
# result = mycol.delete_many({"id":"003"})
# result = mycol.delete_many({})  #Delete everythin in the collection
