# sort program
# creates random shuffled list from 0-9 
# algorithm sorts from lowest to highest
# nicholas mamais 9/21/2021

import random

# Makes list then shuffles it
unordered = list(range(10))
ordered = []
random.shuffle(unordered)

# checks to see if list is still shuffled
while unordered:
    # takes random number from 0-9 thats index zero sets that as minimum
    minimum = unordered[0]
    # checks to see how x relates to the minimum   
    for x in unordered: 
        if x < minimum:
            minimum = x
    ordered.append(minimum)
    unordered.remove(minimum)    

print(ordered)