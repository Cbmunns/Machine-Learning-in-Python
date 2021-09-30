# Open the file to read
file = open('Input.txt', 'r')
#file = open('Input_2.txt', 'r')
# Create a word dictionary
words = {}
# Function to either make a new key for a new word or add to a previous word
def dictionary(word):
    if words.get(word) == None:
        words[word] = 1
    else:
        words[word] += 1
# Create a temp hold list
temp = []
# For every line in the file
for line in file:
    # Convert line into list of char
    list(line)
    # For every letter in the line
    for letter in line:
        # If space or next line, word is found
        if letter == ' ' or letter == '\n':
            # If the temp char list is not empty
            if temp != []:
                # Join the list to a string
                temp = ''.join(temp)
                # Run it through dict
                dictionary(temp)
                temp = []
        else: 
            # If no new word found
            temp.append(letter)
# Last word is left hanging, catch it and run it
temp = ''.join(temp)
if temp != '':
    dictionary(temp)
temp = []
# Close for reading session
file.close()
# Open to append the output at the end
file = open('Input.txt', 'a')
#file = open('Input_2.txt', 'a')
# Add next line and title
file.write('\n\n')
file.write('Output: \n')
print('Output: \n')
# Iterate through dict and print the key and value
for key in words:
    result ='\n' + key + ': ' + str(words[key])
    print(key + ': ' + str(words[key]))
    file.write(result)
# Close when done
file.close()