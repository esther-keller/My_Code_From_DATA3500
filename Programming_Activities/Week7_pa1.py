#Programming Activity 1

#Create the list and assign the values.
#For loop through the values in the list.

colors = ['red', 'blue', 'green']
for color in colors: 
    print(f"Color:{color}")
    
#Programming Activity 2 
# ested for loop, to iterate through the characters in each color.

colors = ['red', 'blue', 'green']
for color in colors: 
    print()
    for x in color:
        print(x)


print()

#Programming Activity 3

#Create an empty list.
#For loop 10 times and append a random number each time.

import random
integers = []

for i in range(1,11):
    i = random.randint(1,10)
    integers.append(i)
    print(i)

"""
Programming Activity 4 

Using the list you generated in programming activity 3, 
extend your program to check if there are 2 even numbers 
in a row. If there are two even numbers in a row, print 
the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and 
      check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number 
and next number are both even.
"""
print()
import random
integers = []

for i in range(1,11):
    i = random.randint(1,10)
    integers.append(i)
print(integers)

for i in integers:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print(integers[0])
#integers [0:2]
if integers[0] % 2 == 0 and integers[1] % 2 == 0:
    print(f"{integers[0]} and {integers[1]} are even")
else:
    print(f"{integers[0]} and {integers[1]} are not even")

#integers [1:3]
if integers[1] % 2 == 0 and integers[2] % 2 == 0:
    print(f"{integers[1]} and {integers[2]} are even")
else:
    print(f"{integers[1]} and {integers[2]} are not even")
    
#integers [2:4]
if integers[2] % 2 == 0 and integers[3] % 2 == 0:
    print(f"{integers[2]} and {integers[3]} are even")
else:
    print(f"{integers[2]} and {integers[3]} are not even")
    
#integers [3:5]
if integers[3] % 2 == 0 and integers[4] % 2 == 0:
    print(f"{integers[3]} and {integers[4]} are even")
else:
    print(f"{integers[3]} and {integers[4]} are not even")

#integers [4:6]
if integers[4] % 2 == 0 and integers[5] % 2 == 0:
    print(f"{integers[4]} and {integers[5]} are even")
else:
    print(f"{integers[4]} and {integers[5]} are not even")
    
#integers [5:7]
if integers[5] % 2 == 0 and integers[4] % 2 == 0:
    print(f"{integers[5]} and {integers[6]} are even")
else:
    print(f"{integers[5]} and {integers[6]} are not even")
    
#integers [6:8]
if integers[6] % 2 == 0 and integers[7] % 2 == 0:
    print(f"{integers[6]} and {integers[7]} are even")
else:
    print(f"{integers[6]} and {integers[7]} are not even")
    
#integers [7:9]
if integers[7] % 2 == 0 and integers[8] % 2 == 0:
    print(f"{integers[7]} and {integers[8]} are even")
else:
    print(f"{integers[7]} and {integers[8]} are not even")
    
#integers [8:10]
if integers[8] % 2 == 0 and integers[9] % 2 == 0:
    print(f"{integers[8]} and {integers[9]} are even")
else:
    print(f"{integers[8]} and {integers[9]} are not even")


#integers [0:2]
if integers[0] % 2 == 0 and integers[1] % 2 == 0:
    print("yes")
else:
    print('no')

#integers [1:3]
if integers[1] % 2 == 0 and integers[2] % 2 == 0:
    print("yes")
else:
    print("no")
    
#integers [2:4]
if integers[2] % 2 == 0 and integers[3] % 2 == 0:
    print("yes")
else:
    print('no')
    
#integers [3:5]
if integers[3] % 2 == 0 and integers[4] % 2 == 0:
    print("yes")
else:
    print('no')
    
#integers [4:6]
if integers[4] % 2 == 0 and integers[5] % 2 == 0:
    print("yes")
else:
    print('no')
    
#integers [5:7]
if integers[5] % 2 == 0 and integers[4] % 2 == 0:
    print("yes")
else:
    print('no')
    
#integers [6:8]
if integers[6] % 2 == 0 and integers[7] % 2 == 0:
    print("yes")
else:
    print('no')
    
#integers [7:9]
if integers[7] % 2 == 0 and integers[8] % 2 == 0:
    print("yes")
else:
    print('no')
    
#integers [8:10]
if integers[8] % 2 == 0 and integers[9] % 2 == 0:
    print("yes")
else:
    print('no')
