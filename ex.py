import json

data = {
    "emp1":{
        "Name":"Balaji",
        "Age": 18,
        "Employed":False,
        "Non_Employed":True,
        "Salary":10000
    },
    "emp2":{
        "Name":"Abi",
        "Age":19,
        "Employed":True,
        "Non Employed":False,
        "Salary":18000
    }
}

server_file = open("/home/balaji/Documents/server.json", "w")
json.dump(data, server_file, indent=6)
server_file.close()