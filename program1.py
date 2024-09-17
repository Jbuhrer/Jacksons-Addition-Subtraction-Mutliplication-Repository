# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate the sum
sum = add_numbers(num1, num2)

# Display the result
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
