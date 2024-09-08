string = "a string with whitespaces"
print(f"String original: '{string}'")

list_of_strings = string.split(" ")
print(f"String separado en strings almacenados en una lista:\n{list_of_strings}")

for word in list_of_strings:
    print(word.upper())

list_back_to_string = " ".join(list_of_strings)
print(list_back_to_string)
