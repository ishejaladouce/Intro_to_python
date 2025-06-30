#Define a function that takes three arguments two numbers and an operator(+,-,*,/)
# define calculator
def main ():
    calculator()
    
def calculator():
    
    print("")
# Checking if the user has entered only numbers for the first number    
    while True:
        input1 = input("Enter the first number: ")
        if input1.isdigit():
            num1 = int(input1)
            break
        else:
            print("Invalid input!")
            print("Please, enter the number.")
            print("")
# Checking if the user has entered the correct operator    
    while True:
        input3 = input("Choose operator (+,-.*,/): ")
        if input3 not in ["+","-","*","/"]:
            print("Wrong operator")
            print("Choose between (+,-,*,/) and try again!")
            print("")
        else:
            operator = input3 
            break
        
# Checking if the user has entered only numbers for the second number      
    while True:
        input2 = input("Enter the second number: ")
        if input2.isdigit():
            num2 = int(input2)
            break
        else:
            print("Invalid input!")
            print("Please, enter the number.")
            print("")

# perform calculation based on the operator
    if operator == '+':
        result = num1 + num2
        print("")
    
    elif operator == '-':
        result = num1 - num2
        print("")
        
    elif operator == '*':
        result = num1 * num2
        print("")
    
    elif operator == '/':
        result = round(num1 / num2, 2)
        print("")
        
# Showing the Final Result
    print(f"{num1} {operator} {num2} = {result}")
    print("")

# Calling the main function
if __name__ == '__main__':
    main()