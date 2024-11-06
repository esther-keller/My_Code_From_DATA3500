"""
array of intigers and return a new array so that ll the new numbers are the products of the origional numbers

"""

import nypy




#use numpy for hw4


import numpy as np

prices = [82,65,10.52]
#create numpy array
np_prices = np.array(prices)

#np ones

#np zeros

#use placeholders and change them
arr = np.ones(4)
print("array:",arr)

counter = 0
for num in arr:
    arr[counter] = counter
    counter += 1
print("arr:",arr)


#arr = np.append(array , what we want to add)
arr = np.append(arr,37)
print("arr:",arr)


#random
import random
# random.randing()
# random.randrange()

np_randoms = np.random.randint(1, 11, 10) #(lower, uppper, total numbers) #non inclusive
print(np_randoms)

#statistics
mean = np.mean(np_randoms)
std = np.std(np_randoms)

print("mean:", mean)
print("std:", std)



