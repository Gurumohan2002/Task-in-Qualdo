# Writing a file and checking for the user specific word was in the file and 
# returns true and counting the each word in it and printing each word with its count
def write_file():
    with open("readme.txt", "w") as file:
        L = ["Hi Everyone\n", "Hi I am Guru \n", "I am from Trichy\n","I watch movies and webseries\n"]
        file.writelines(L)

# check() function gets details for checking and tofind for matching the matches in it 
# Here the string are case insensitive So converting them to lower() easily matches the strings in it.
def check(details, tofind):
    return tofind.lower() in details.lower()

# word_count() gives the count of each word from the file
def word_count(details):
    word_count = {}
    words = details.split()
    # print(words)
    for word in words:
        word = word.strip('.,!?()[]{}:;"\'').lower()
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    # print(word_count)
    return word_count


# Reading the file and checking for the matches given by the user and
# printing the word count in it.
def read_file():
    with open("readme.txt", "r") as file:
        details = file.read()
        print("Output of the Read file is ")
        print(details)
        tofind = 'from' 
        final = check(details, tofind)
        print(f"String '{tofind}' is found in this file: {final}")
        word_counts = word_count(details)
        
        print("\nWord counts in the file:")
        print(word_counts)

write_file()
read_file()