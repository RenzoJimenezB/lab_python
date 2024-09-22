"""
Convert Python dictionary to JSON

dumps()

"""
import json

from test_09 import json_to_python

print(json_to_python)
print(type(json_to_python))

python_to_json = json.dumps(json_to_python)
print(python_to_json)
print(type(python_to_json))
