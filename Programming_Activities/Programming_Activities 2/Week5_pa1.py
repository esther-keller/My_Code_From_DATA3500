#Programming Activity 1
user_input = int(input('Please enter any 3 digit number'))
first_number = user_input // 100
last_number = user_input % 10
if first_number == last_number:
    print("palindrome!!!!")
else:
    print("not palindrome!")
    

#Programming Activity 2
"""
Programming Activity 2

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""

#Programming Activity 2
number = 2
total = 0

for i in range (1,1001):
    total += (1/number)
    number *= 2
print('total:', total)