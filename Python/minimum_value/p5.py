# Getting the key from the dictionary which has lowest mark in it.

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
#Creating the list which contains the values of dictionary in it
a=list(sample_dict.values())

# Here finding the index of the min of the values from the created list
# and taking the key of the min index from the dictionary
def met1():
    x=a.index(min(a))
    key, value = list(sample_dict.items())[x]
    print(key)
    
# Here creating loop for key value pair and finding which value is equal to the min of the value
#and printing the respective key to it
def met2():
    for key,value in sample_dict.items():
        if value == min(a):
            print(key)
            
if __name__ == "__main__":
    met2()
    # met1()
    
    