#save fruit in a list
Fruits = ["Watermelon", "Apple", "Lemon", "Banana", "Passion"]

#ask user to add a new fruit
add_Fruit = input("Enter a new fruit: ")

#Print the current list of fruits
print("Current list of fruits:")
print("-----------------------")
# Loop through the list and print each fruit
for fruit in Fruits:
    print(fruit)

#add the new fruit to the list
Fruits.append(add_Fruit)
print("")
# Print the updated list of fruits
print("Updated list of fruits:")
print("-----------------------")
# Loop through the updated list and print each fruit
for fruit in Fruits:
    print(fruit)
