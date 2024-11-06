



#using lists as arguments

import random

colors = ['blue', 'green', 'pink']

random.shuffle(colors)


while True: 
    answer = []
    correct = 0
    question1 = input("What is your first color?")
    answer.append(question1)
    
    question2 = input("What is your second color?")
    answer.append(question2)
   
    question3 = input("What is your third color?")
    answer.append(question3)
   
   if colors[0] == answer[0]:
        correct += 1
    else: 
        correct += 0
   
    if colors[1] == answer[1]:
        correct += 1
    else: 
        correct += 0
   
    if colors[2] == answer[2]:
        correct += 1
    else: 
        correct += 0




        
if correct == 3:
    print("You win.")

else:
    ("You didn't guess correctly. You lose.")
      
# print(colors)































mylist = ['blue', 'green', 'pink']


def print_list(mylist):
    for i in mylist:
        print(i)
        
print_list(mylist)


colors = [1,3,4,5,6]


def average_list(my_list):
    return sum(my_list) / len(my_list)
    
print(average_list(colors))


list1 = ["blue", 'green']
list2 = ['hamburger',"pizza", 'tacos', 'pizza', 'hamburger', 'nuggets']

def con_list(list1, list2):
    return list1 + list2
    
print(con_list(list1,list2))
    
    
print(list2.index("hamburger" , 1,5))


try: 
    print(list2.index("grapes"))
except ValueError:
    print("grape isn't in our list")


numbers = [6,4,2,8,1,6,4,9,10,7]
numbers.sort(reverse = True)
print(numbers)


list2 = ['hamburger',"Pizza", 'tacos', 'pizza', 'Hamburger', 'nuggets']

list2.sort(key = str.lower) #sort is case sensitive it will put upper case before lowercase
print(list2)