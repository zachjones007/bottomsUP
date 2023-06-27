import pprint

# Creating a dictionary
user = {"name": "Bob", "username": "bob42"}

# Accessing a value in the dictionary
print("Name:", user["name"])

# Trying to access a non-existent key with a default value (avoids KeyError)
print("Age:", user.get("age", "Unknown"))

# Adding a key-value pair to the dictionary
user["age"] = 30
print("Age after adding:", user["age"])

# Using setdefault to ensure a key is set
user.setdefault("location", "Unknown")
print("Location:", user["location"])

# 'Pretty printing' the dictionary
print("Pretty printing the dictionary:")
pprint.pprint(user)

# Looping over the dictionary keys and values
print("Printing all key-value pairs:")
for key, value in user.items():
    print(key, ":", value)
