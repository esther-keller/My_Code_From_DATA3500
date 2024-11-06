# #list
# flavors = ['vanilla', 'chocolate', 'cookie dough', 'cookie dough', 'aggie blue mint']
# print(flavors)

# print(flavors[0])
# print(flavors[3])

# #append
# flavors.append('huckleberry')
# print(flavors)
# #another way to add to a list
# flavors.insert(4, "strawberry")
# print(flavors)

# #remove items
# flavors.pop()
# print(flavors)

# flavors.append('lemon custard')
# flavors.append('bull tracks')
# flavors.append('pistachio')
# print(flavors)

# flavors.remove("lemon custard") #remove has to have an argument!!
# print(flavors)



# #slicing

# #slice opporator :
# calories = [128, 480, 1117, 2, 990, 854, 42]
# print("calories:", calories)
# calories_copy = calories [:]
# print('calories_copy', calories_copy)

# reverse = calories[::-1]
# print("reverse:", reverse)

# cal = calories[0:2] #this will print the first two items in a list
# print("cal:", cal)

# cal = calories[4:6] #this will print items four and five
# print("cal:", cal)


#random module
import random

rand_num = random.randint(1,3) #is inclusive
rand_num2 = random.randrange(1,3) #not inclusive!!

print(rand_num)
print(rand_num2)
