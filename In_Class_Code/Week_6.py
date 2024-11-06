# theme: spooky season

""" 
WHY USE FUNCTIONS????
- reusing code
- efficiency
-prevent bugs in our code
- breaking down into smaller pieces
- readability of code
- organization of code 
- testing code - smaller chunks of code
"""

"""
Building blocks of functions:
1 - Name
2 - Arguments (optional)
3 - Logic
4 - Regurn statement
"""

# print()
# range()
# len()
# int()
# str()
# bool()
# eval()
# input()

#write our own function!!!!!!

def is_spooky_season(month):
    if month == "October":
        return "It is spooky season."
        

current_month = input("What month is it")
print(is_spooky_season(current_month))


#temp converter

#F to C
def f_to_c(ftemp):
    ctemp = (ftemp-32)*(5/9)
    return ctemp

currenttemp = int(input("Please input the current temp."))
print(f_to_c(currenttemp))

#C to F
def c_to_f(ctemp):
    ftemp = ((ctemp / (5/9))+32)
    return ftemp

currentftemp = int(input("Please input the current temp."))
print(c_to_f(currentftemp))


#function argument defaults
# def what_is_your_costume(will_dress_up):
#     if will_dress_up:
#         print("that's a great costume!")
#     else:
#         print("Find a costume quick!")
        
# costume = bool(input("Are you dressing up for halloween: (True or False)"))

# what_is_your_costume(costume)


def can_sit_in_front(age = 0,weight = 0):
    if age >= 12:
        print("your child can sit in the front seat")
    elif age == 11 and weight > 90:
        print("your child can sit in the front seat")
    elif age < 11 and weight > 100:
        print("your child can sit in the front seat")
    else:
        print("no front seat for kid")
        
can_sit_in_front()