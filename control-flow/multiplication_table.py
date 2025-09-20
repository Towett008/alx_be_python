#multiplication_table


#prompt the user for the input
number = int(input("Enter a number to see its multiplication tabkle:  "))

# Use a for loop to print the multication table from 1 to 10

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
    