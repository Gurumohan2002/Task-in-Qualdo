import random

def generate_random_number():
    return random.randint(10000,99999)

def checking(random_number,user_input):
    rand_digits=list(str(random_number))
    user_digits=list(str(user_input))
    
    result=["","","","",""]
        
    for i in range(5):
        if user_digits[i] == rand_digits[i]:
            result[i]='C'
        elif user_digits[i] in rand_digits :
            result[i]='B'
        else:
            result[i]='A'        
                   

    while len(result) < 5:
        result.append('A')
    
    return result

def main():
    random_number=generate_random_number()
    print(random_number)
    start=0
    
    while start<5:
        user_input=input("Enter a 5 digit number:")
        if len(user_input)!=5 or not user_input.isdigit():
            print("Invalid input! Please enter a valid input:")
            continue
        
        user_input=int(user_input)
        
        result = checking(random_number, user_input)
        print(result)
        
        if result == ['C', 'C', 'C', 'C', 'C']:
            print("Congratulations! You guessed the number!")
            break
        
        start += 1
    
    if start == 5:
        print(f"Sorry, you couldn't guess the number. The number was {random_number}.")

if __name__ == "__main__":
    main()