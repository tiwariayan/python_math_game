# Importing required libraries
import random

# Function to generate random number based on constraints and operator selected
def rand_generator(f_operator):
    # limit --> Positive and Negative range of numbers
    limit = 100
    if f_operator == '+':
        n1 = random.randint(-limit,limit)
        if n1 < 0:
            n2 = random.randint(abs(n1),limit)
        else:
            n2 = random.randint(0,limit)
    if f_operator == '-':
        n1 = random.randint(-limit,limit)
        n2 = random.randint(-limit,n1)
    if f_operator == '*' or f_operator == '/':
        n1 = random.randint(-limit,limit)
        if n1 >0:
            n2 = random.randint(0,limit)
        else:
            n2 = random.randint(-limit,0)
    return(n1,n2)

# Function to allow user to solve math equations
def calculate(operator):
    
    # f_counter --> Counter to check if user entered numeric input
    # count --> Count of correct responses from user
    f_counter = 3
    count = 0
    flag = 0
    for i in range(10):
        num1,num2 = rand_generator(operator)
        if operator == '+':
            out = num1 + num2
            print(i+1,'. ',num1 ,' ' , operator , ' ', num2)

        elif operator == '-':
            out = num1 - num2
            print(i+1,'. ',num1 ,' ' , operator , ' ', num2)

        elif operator == '/':
            out = int(num1 / num2)
            print(i+1,'. ',num1 ,' ' , operator , ' ', num2)

        elif operator == '*':
            out = num1 * num2
            print(i+1,'. ',num1 ,' ' , operator , ' ', num2)
        
        # Checking if User entered numeric input
        for j in range(f_counter):
            u_out = input()
            if u_out.isnumeric() == False:
                print("Enter numeric input, Tries remaining : ", f_counter-j)
                flag = 1
            else:
                flag = 0
                break
        if flag ==  1:
            return False

        # Checking if user input is equal to the correct value
        if int(u_out) == out:
            count +=1
    print("Number of correct responses :" , count, "/10")
            
    return True
def main():
    # List of operators to be used
    l_operator = ['+','-','*','/']

    # c --> Counter for retries in case of wrong input
    # start --> To keep our game running until user inputs wrong operator max times
    c = 3
    error_flag = 0
    start = 0

    while start < c:
        print("Choose operator \n 1. '+' \n 2. '-' \n 3. '*' \n 4. '/'")
        val = input("Choose your operator (by symbol) : ")
        
        # Checking if user input is from our menu
        if val not in l_operator:
            print("Wrong Input, Please try again")
            start +=1
            error_flag = 1
        else:
            error_flag = 0
            out = calculate(val)

            # Checking if user entered numeric answer to equation for fixed number of times
            if out == False:
                print("User did not enter numeric input, Please try running the game again")
                break
            print("Do you want to exit or play again?")
            print("Write 'y' to play again, any other input to exit")
            u_input = input()

            # Allowing user to replay the game or quit
            if u_input in ['y','Y']:
                print("User has decided to play again")
                continue
            else:
                print("User has decided to exit the game")
                break
    if error_flag == 1:
        print("Max no of retries have been reached")

if __name__ == "__main__":
    main()