import json
my_dict = {"name": "Nitesh", "age": 21}

jsonoutput = json.dumps(my_dict)
print("JSON OUTPUT")
print(type(jsonoutput))
json_dict = json.loads(jsonoutput)
print(type(json_dict))
print(json_dict)
