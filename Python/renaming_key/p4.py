# Changing the key name from the dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

# used pop() function to remove the city key value pair from the dictionary
# and using update() function updated the  location to the key value pair in place of city   
def met1():
    sample_dict.pop('city')
    print(sample_dict)
    sample_dict.update({"location":"New york"})
    print(sample_dict)

# met1()

#used del keyword to delete the key value pair in dictionary 
# and update() function to update the key value pair in  place of city 
def met2():
    del sample_dict['city']
    print(sample_dict)
    sample_dict.update({"location":"New york"})
    print(sample_dict)
    
# met2()

# Here directly updating the key to updating key and deleting the old key pair in dictionary
def met3():
    sample_dict["location"]=sample_dict["city"]
    del sample_dict["city"]
    print(sample_dict)
    
# Here taking the value of city from dictionary and popping up the city key from the dictionary
# and updating the key to the value   
def met4():
    location = sample_dict.pop("city", None)
    if location:
        sample_dict["location"] = location
    print(sample_dict)
    
# met3()

if __name__ == "__main__":
    # met3()
    # met1()
    # met3()
    met4()