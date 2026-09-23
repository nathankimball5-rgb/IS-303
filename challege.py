numbers = [5, 16, -3, 0, 12]

current_number = 0
pos_numbers = 0
neg_numbers = 0
zero_numbers = 0

for i in range(0,4):
    current_number = numbers[i]
# Ask the computer to check each of the numbers to see if it is postiive
    if i < 0:
        neg_numbers += 1
    # Ask to see if it is < 0
    elif i > 0:
        pos_numbers += 1
    # Ask if it is equal to 0
    else:
        zero_numbers += 1
    #write out the totals 

print(int(neg_numbers))
print(int(pos_numbers))
print(int(zero_numbers))
