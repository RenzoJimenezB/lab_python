"""Diccionarios en Python"""

var_1 = {
    "nombre": "MySQL",
    "tipo": "SQL db"
}

print(f"Original dictionary: {var_1}")

"""convertir diccionarios a listas"""

# Converting dictionary to list of keys
var_2 = list(var_1)
print(f"Dictionary converted to list: {var_2}")

# Converting dictionary values to a list
var_1_values = list(var_1.values())
print(f"Dictionary values to list: {var_1_values}")

# Converting dictionary keys to a list
var_1_keys = list(var_1.keys())
print(f"Dictionary keys to list: {var_1_keys}")

# Converting dictionary items to a list. Items are converted into sets
var_1_items = list(var_1.items())
print(f"Dictionary items to list: {var_1_items}")