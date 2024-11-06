list1 = [24,12,17]
list2 = [17,12,24]

list1.sort()
list2.sort()

if list1 == list2:
    print("they're the same.")
else:
    print("They are not the same")
    
    
    
    
    
    
    
    
    
#Python Review
'''write code which will calculate a 3 day moving verage for the list
below in a for loop'''

lst = [1,2,3,4,5,6,7,8,9]

for i in range(len(lst)-2):
    average = (lst[i] + lst[i+1] + lst[i+2]) / 3
    print("Three item moving average:", average)
    
    
'''output the following numbers witha. comma and space seperating each 
number in a for loop'''

lst = [1,10,2,20,3,30,4,40,5,50]
lst2 = []
for l in lst:
    lst2.append(l)
print(lst2)


lst = [2,4,6,8,10,12,14,16,20]
for l in lst:
    print(l, end=" ")
    

# lst = []    
# ui = input("please enter your favorite color.") 
# lst.append(ui)
# print(lst)

age = ("please enter your age")
age += 1
print(f"On your next birthday, you will be {age}.")

