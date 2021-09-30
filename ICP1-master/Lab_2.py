# Main function
def change_python():
    # Create temp and final structures for sentence
    holder = []
    final = []
    
    # Take in the sentence provided as string
    sentence = input("Please enter your sentence: ")
    # Convert string to a list of char
    sentence = list(sentence)
    # Add a space to end to mark end of sentence
    sentence.append(' ')
    # Run through full list
    for i in sentence:
           # If space convert sentence holder list to one word and add to final list
           if i == ' ':
               holder = ''.join(holder)
               final.append(holder)
               holder = []
           # Add char to word holder list    
           else:
               holder.append(i)
    # Run through all the words
    for i in range(len(final)):
        # If the word is any form of python
        if final[i].lower() == 'python':
            # Convert word to list of char in temp
            temp = list(final[i])
            # Add s to list and recombine
            temp.append('s')
            temp = ''.join(temp)
            # Replace in postion in word list
            final[i] = temp
    # Combine into full string with spaces then print         
    final = ' '.join(final)
    print(final)

# Driver function
change_python()