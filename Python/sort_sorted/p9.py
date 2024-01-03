# Program for sort() and sorted() function

sample=[2,1,4,6,3,5,7,0,8,9]
sample1=(1,4,3,6,7,8,2,4,5,7,9,0)
sample2={1,5,3,8,2,8,0,7,5,3,8}
sample3={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven"}
sample4=[(1,3),(3,2),(1,5)]

# Here the sorted function will returns only the sorted value and returns the sorted one
# it does not change anything in the list or dictionaries and it creates a new list and dictionaries
def sorted_fun():
    print(sorted(sample))
    print(sample)
    print(sorted(sample1))
    print(sample1)
    print(sorted(sample2))
    print(sample2)
    print(sorted(sample3))
    print(sample3)
    print(sorted(sample4,key=lambda x: x[1]))
    print(sample4)
    
# Here the sort function will modify the existing list and returns None
# it does not create a new list and it works for only the list not for dictionary or tuples etc..
def sort_fun():
    print(sample.sort())
    print(sample)
    print(sample4.sort())
    print(sample4)

# sorted_fun()
# sort_fun()
print(sorted(sample4,key=lambda x: x[1]))