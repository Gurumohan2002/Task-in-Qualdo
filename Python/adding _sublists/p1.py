# adding a list in a sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# Here extend() function is used for extending the values in the list to the sublist
def met1():
    list1[2][1][2].extend(sub_list)
    print(list1)

if __name__ == "__main__":
    met1()
