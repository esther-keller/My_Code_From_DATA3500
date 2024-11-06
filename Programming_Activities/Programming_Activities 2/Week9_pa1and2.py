"""
Programming Activity 1

Write a program, and have the user enter their 
name and their favorite 
color, as two separate variables. Write the 
sentence to a file using the 
with command "<name>'s favorite color is 
<color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""

name = input("Please enter your name:")
color = input("Please enter your favorite color:")
with open("pa.txt", "w") as file:
    file.write(f"{name}'s favorite color is {color}.")
    
"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized 
to 0. Then, change the 
array from 0s to random numbers.
"""

import numpy
import random

np1 = numpy.zeros(100)
print(np1)

randoms = []
for i in range (100):
    randoms.append(random.randint(1,50))
#print(randoms)
rands = numpy.random.randint(50,size = 100)
print(rands)




"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. 
Then, change the array from 0s to random numbers.
"""
#numpy randoms for creating an entirely new array
import numpy 
import random
np_zeros = numpy.zeros(100)
print(np_zeros)

i = 0
for zero in np_zeros:
    np_zeros[i] = random.randint(1,101)
    i += 1
print(np_zeros)