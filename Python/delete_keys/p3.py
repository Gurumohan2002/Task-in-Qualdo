# Deleting key value pair from the dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

# {'city': 'New york', 'age': 25}

# Here Popping the key value pair from the dictionary
def met1():
    for i in keys:
        sample_dict.pop(i)
    print(sample_dict)

# Here deleting the key value pair from the dictionary
def met2():
    for i in keys:
        del sample_dict[i]
    print(sample_dict)

if __name__ == "__main__":
    # met2()
    met1()