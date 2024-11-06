#2.3
#assign variables
while True:
    grade = input("Please enter your grade in this class. Please enter it as a 2 digit number.")
    try: #use try and except as a form of error handling to prevent users from braking code by entering in a string or float.
        grade = int(grade)
        if grade >= 90: 
            print("Congratulations! Your grade of", grade, "earns you an A in this course!")
            break
        elif grade <= 90:
            print("You're still a great person!")
            break
    except:
        print("You need to input your grade as a number. For example if you have a 94%, please enter 94.")

#2.4 
print() #insert a break to clearly define the start of a new problem
#assign variables
x = 27.5
y = 2

#addition
print("27.5 + 2 =",x+y)

#subtraction
print("27.5 - 2 =",x-y)

#multiplication
print("27.5 * 2 =",x*y)

#true division
print("27.5 / 2 =",x / y)

#floor division
print("27.5 // 2 =",x // y)

#exponant
print("27.5 ** 2 =",x ** y)

#2.5 
print() #insert a break to clearly define the start of a new problem
pi = 3.14159
r = 2 #radius

#diameter
diameter = 2 * r #d is the variable to represent diameter
print("Diameter is:",diameter)

#circumference
circumference = 2 * pi * r 
print("Circumference is:",circumference)

#area 
area = pi * (r **2)
print("Area is:",area)


#2.6
print() #insert a break to clearly define the start of a new problem
while True:
    x = input("Please input an integer.") #x is the input variable
    try: #using as a form of error handling to ensure the user inputs an integer
        x = int(x) #converting from a string to an integer
        if x % 2 == 0: 
            print(x,'is an even number.')
            break
        elif (x % 2 < 0) or (x % 2 > 0):
            print(x, 'is an odd number.')
            break
    except: #if no integer is entered, user will be asked to input again
        print('You did not enter an integer. Please try again.')
        

#2.7
print() #insert a break to clearly define the start of a new problem
#assign the variables
x = 1024 
y = 4
a = 10
b = 2

if x % y == 0:
    print('1024 is a multiple of 4.')
else:
    print('1024 is not a multiple of 4.')
    
if a % b == 0:
    print('2 is a multiple of 10.')
else: 
    print('2 is not a multiple of 10.')
    
    
#2.8  
print() #insert a break to clearly define the start of a new problem
#assign the variable (list)
numbers = [0, 1, 2, 3, 4, 5]
for x in numbers:
    print(f"{x} \t {x**2} \t {x**3}")