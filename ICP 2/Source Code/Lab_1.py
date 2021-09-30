# Create first list and output as well as Const for CM conversion num
l1 = [5.2, 5.4, 5.6, 6.1]
output = []
TO_CM = 30.48

# For all items in list
for i in l1:
    # Take the var
    hold = i
    # Times it by the constant
    hold *= TO_CM
    # Round to on decimal
    hold = round(hold,1)
    # Add it to output list
    output.append(hold)

# Print
print(output)