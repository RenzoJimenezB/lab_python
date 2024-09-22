"""
JSON
"""

import json

json_data = '{"nombre": "Python", "tipo": "Backend", "paradigna": "POO"}'

"""
Convert JSON => Python dictionary

loads()

"""
json_to_python = json.loads(json_data)

if __name__ == "__main__":
    print(json_data)
    print(type(json_data))

    print(json_to_python)
    print(type(json_to_python))
