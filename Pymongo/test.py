'''
import pymongo

myClient = pymongo.MongoClient()

testdb = myClient['testdb']

todosCol = testdb['todos']


todosData = [{'userName':"Admin", 'pin':"5t6y", 'age':45},
            {'userName':"SenoirDev1", 'pin':"v5465", 'age':33},
            {'userName':"JuniorDev1", 'pin':"g5y4", 'age':26},
            {'userName':"Account33", 'pin':"09u7", 'age':56},
            {'userName':"Janitor4", 'pin':"p654", 'age':21},
            {'userName':"FrontendDev1", 'pin':"mnbg", 'age':30}
             ]
# todosCol.insert_many(todosData)

print(f'The list of the databases are: {myClient.list_database_names()}')
print(f'The list of the collecitons in testdb database are: {testdb.list_collection_names()}')
for i in testdb.list_collection_names():
    print(i, end="\n")


for x in todosCol.find():
    print(f'VALUE: {x}')

for y in todosCol.find({'age':{"$gte":30}}):
    print(f'GREATE THAN 30 ----->   {y}')
'''

import  test1
test1.sayHello()

x1 = test1.MyClass("Ibrahim Musa Suleiman")