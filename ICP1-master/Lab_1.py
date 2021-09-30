
import random

# Delete random letter in list
def delete_random(list):
    # Find size of list
    size = len(list)-1
    # Create some random positon in the list to delete with size of list being accounted for
    delete = random.randint(0,size)
    # Pop the char from the list
    list.pop(delete)
    # Return new 
    return list

# Create function
def delete_reverse():
    # Declare how many letters to remove
    REMOVE = 2
    # Take in the word provided as string
    word = input("Please enter your word: ")
    # Convert string to a list of char
    word = list(word)
    # Delete however many letters you wanted
    for i in range(REMOVE):
        word = delete_random(word)    
    # Reverse the list
    word.reverse()
    # Convert back to string
    output = ''.join(word)
    # Print string
    print("You get: ", output)

# Driver function
delete_reverse()