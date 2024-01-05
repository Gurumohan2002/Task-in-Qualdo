# Function for Airflow Operations
from airflow.models import Variable

#Storing input in Variable class with key value pair
def get_user_input(input_list):
    for word in input_list:
        Variable.set(word, len(word))

#Printing the word and its length in the of the words
def print_word_lengths(input_list):
    word_lengths = {word: Variable.get(word) for word in input_list}
    print(word_lengths)

#Function for adding two values
def adding_two_values(a, b):
    result = a + b
    print(f"Addition of a and b : {result}")
    return result

#Function for Subracting two values
def subtracting_two_values(c, d):
    result = c - d
    print(f"Subtraction of c and d : {result}")
    return result

#Function for multiplying two values
def multiplying_two_values(e, f):
    result = e * f
    print(f"Multiplication of e and f : {result}")
    return result


