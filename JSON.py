import json
import datetime
# testing with JSON


#From a tutorial:
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print ('DATA:', repr(data))

data_string = json.dumps(data)
print ('JSON:', data_string)


#jsontest = '{"first_name": "Guido", "last_name":"Rossum"}'
#parsed = json.loads(jsontest)
#print(jsontest['first name]'])

test = '{"first_name": "Guido", "last_name":"ros"}'
parsed = json.loads(test)
print(type(test), "<-- test type")
#don't know how to use a dictionary in python...
print(parsed)
print(type(parsed))
print(list(parsed.keys()))

print (parsed['first_name'])
#gr =test("first_name")
#print(gr)

dt = datetime.datetime.now()
#jsontime = json.dumps(dt)
print(dt)

