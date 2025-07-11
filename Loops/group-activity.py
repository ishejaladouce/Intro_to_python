#Define a function that takes three arguments two numbers and an operator(+,-,*,/)
# define calculator
def main ():
    calculator()
    
def calculator():
    
    print("")
    while True:
        
        input1 = input("Enter the first number: ")
        if input1.isdigit():
            num1 = int(input1)
            break
        else:
            print("Invalid input!")

    print("")
    while True:
        input3 = input("Choose operator (+,-.*,/): ")
        print("")
        if input3 not in ["+","-","*","/"]:
            print("Wrong operator")
        else:
            operator = input3 
            break
    while True:
        input2 = input("Enter the second number: ")
        if input2.isdigit():
            num2 = int(input2)
            break
        else:
            print("Invalid input!")

    #perfom calculation based on the operator
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
    
    else:
        print ("Wrong operator")
        print("")
        print ("Choose between (+,-,*,/)")
    
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == '__main__':
    main()