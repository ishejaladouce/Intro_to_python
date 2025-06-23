# Example 1: this will print "Hello world" 9 times
for i in range (1, 10):
    print ("Hello world")

#Example 2": this will print odd numbers from 1 to 9
for i in range (1, 10, 2):
    print (i)

#Example 3: this will print "Hello world" 5 Times
for i in range (1, 10, 2):
    print ("Hello world")

# Example 4: this will print names in the list
name = ["Eric", "John", "Mary", "Alice"]
for i in name:
    print (i)

#Example 7: This will ask the user to enter a number and then uses for loop to print the multiplication of that number from 1 to 10
number = int(input("Enter a number: "))
for i in range(1, 11, 1):
    print(number * i)

#Example 8: This will ask the user to enter a number and then uses for loop to print the multiplication of that number from 1 to 10
myNum = int(input("Enter a number: "))
for i in range(1, 11):
    print(myNum * i)
    i += 1

#Example 7: This will ask the user to enter a number and then uses for loop to print the multiplication of that number from 1 to 10
myNumber = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{myNumber} * {i} = {myNumber * i}")
    i += 1