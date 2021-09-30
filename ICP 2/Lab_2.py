print("Find out how many steps it take to reduce to 0")
# Input the number you want to use
number = input("Please enter a number: ")
# Create a counter and convert number string to an int
count = 0
number = int(number)
# While the number is not 0
while number != 0:
    # If the number is even
    if number % 2 == 0:
        # Divide num by 2
        number /= 2        
    else:
        # Subtract 1 because odd
        number -= 1        
    # Add a step to the count
    count += 1
# Print amount of steps
print( "Steps: ", count)