# #2.3
# ''' replace code so that it will return:
# Congratulations! Your grade of 91 earns you an 
# A in this course.

# use the variable grade to store the value
# '''

# grade = int(input("Please enter your grade as a 2 digit number."))

# if grade >= 90:
#     print(f"Congratulations! Your grade of {grade} earns you an A in this course!")
# else: 
#     print("You do not have an A in this class, but you're still a great person!")
    
# print()

# #2.4
# '''
# use each arithmetic operator +,-,*,/,//,** and display the value of 
# an expression with 27.5 as left operand and 2 as right operand
# '''
# addition = 27.5 + 2
# print(f"addition: {addition}")

# subtraction = 27.5 - 2
# print(f"subtraction: {subtraction}")

# multiplication = 27.5 * 2
# print(f"multiplication: {multiplication}")

# divide = 27.5 / 2
# print(f"division: {divide}")

# floor = 27.5 // 2
# print(f"floor division: {floor}")

# exponent = 27.5 + 2
# print(f"exponent: {exponent}")

# print()

# #2.5
# '''
# display diameter, circumference, and area
# radius will be 2
# pi will be 3.14159
# use the normal formulas
# '''

# radius = 2
# pi = 3.14159

# diameter = 2 * radius
# print(f"diameter: {diameter}")

# circumference = 2 * pi * radius
# print(f"circumference: {circumference}")

# area = pi * (radius **2)
# print(f"area: {area}")

# print()

# #2.6
# '''
# use if statements to deterimine odd or even numbers
# remainders even is alwas a multiple of 2
# '''
# number = int(input("Please input a number"))
# num = number % 2
# if num == 0:
#     print(f"{number} is an even number!")
# else:
#     print(f"{number} is an odd number!")
    
# #2.7
# '''
# if statement to determine if
# 1024 is a multiple of 4 and if 
# 2 is a multiple of 10
# '''

# number1 =  1024
# number2 = 4
# number3 = 2
# number4 = 10

# combo1 = 1024 % 4
# combo2 = 2 % 10

# if combo1 == 0:
#     print(f"{number2} is a multiple of {number1}!")
# else:
#     print(f"{number2} is not a multiple of {number1}!")
    
# if combo2 == 0:
#     print(f"{number4} is a multiple of {number2}!")
# else:
#     print(f"{number4} is not a multiple of {number2}!")
    
# print()

# #2.8
# '''
# write a script that calculates the 
# squares and cubes of the numbers 0-5
# print in format shown
# use tab excape to achieve 3 column output
# '''

# for number in range(1,6):
#     square = number ** 2
#     cube = number **3
#     print(f"{number} \t{square} \t{cube}")
    

'''
HW 3
'''

#3.4
'''
fill in the missing code so that it shows 7 @
in 2 rows
'''

for x in range(1,8):
    for i in range(1,8):
        print('@')
        print()