from unicodedata import name


person = {"name": "Jack", "age": 26}
# adding info to person
person["salary"] = 26000
person["age"] = 27
print(person)

# removing element having key name

value = person.pop("name")
print("Value removed: ", value)
print("Updated dict: ", person)
