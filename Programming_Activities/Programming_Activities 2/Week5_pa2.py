#try 1
age = int(input("Please enter your age:"))
weight = int(input("Please enter your weight:"))

if age >= 12:
    print("You can sit in the front!")
elif age == 11 and weight > 90:
    print("You can sit in the front!!")
elif age < 11 and weight > 100:
    print("You can sit in the front!!!")
else:
    print("I'm sorry, you can't sit in the front seat:(")
 
 
print()
print()
#try 2
age = int(input("Please enter your age:"))
weight = int(input("Please enter our weight:"))

criteria_1 = age >= 12
criteria_2 = age == 11 and weight > 90
criteria_3 = age < 11 and weight > 100

if criteria_1 or criteria_2 or criteria_3:
    print("You can sit in the front!!!")
else:
    print("You can't sit in the front:(")