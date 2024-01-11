
import json

#Visit https://www.guru99.com/python-json.html to learn more.
#But note, the Output of the json example is not correct, copy_paste to confirm


#JSON -> JavaScript Object Notation
#A lightweight data format that is used for data exchange

#Converting of python object to JSON is called Serialization or encoding
#Converting of json to python object is called Deserialization or decoding

dict1 = {'fName': "Ibrahim",
         'mName': "Musa",
         'sName': "Suleiman",
         'fullName': ["Ibrahim","Musa","Suleiman"],
         'age': 26,
         'adult': True,
         'phone Numbers':{
             'Phone1': '08123456776',
             'Phone2': '07087654334'
         }
}

#Converting dict1 to JSON

#dict1JSON = json.dumps(dict1)
dict1JSON = json.dumps(dict1, indent=4, sort_keys=True)
#dict1JSON = json.dumps(dict1, indent=4, separators=("$","#"), sort_keys=True)       #dumps, s -> string
print(f'DICTIONARY: {dict1}')
print(f'JSON: {dict1JSON}')

#dump python object into json file
with open('JSON.json', 'w') as jsonFileObj:
    json.dump(dict1, jsonFileObj, indent=4, sort_keys=True)

#Converting json file into python object:
dict1Python = json.loads(dict1JSON)
print(f'JSON_TO_PYTHON: {dict1Python}')

#Load json file from json file
with open('JSON.json', 'r') as jsonFileObj:
    content = json.load(jsonFileObj)
    #content1 = json.loads(content)
    print(f"CONTENT: {content}")
    #print(f"CONTENT1: {content1}")
