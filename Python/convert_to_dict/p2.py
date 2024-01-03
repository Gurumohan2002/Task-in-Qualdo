# converting two list to a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Here zip() function is used to make the key value pair for forming a dictionary and 
# dict keyword used for converting the list to dictionary
def met1():
    dict1=dict(zip(keys,values))
    print(dict1)

# Here creating a empty dictionary and by looping assigning the key value pairs in it
def met2():
    dict1={}
    for i in range(0,len(keys)):
        dict1[keys[i]]=values[i]
    print(dict1)

# Here using lambda function assigning the key value pair with respect to each other 
# and mapping the values as a dictionary
def met3():
    dict1=dict(map(lambda i,j : (i,j) , keys, values))
    print(dict1)
    
if __name__ == "__main__":
    # met1()
    # met2()
    met3()