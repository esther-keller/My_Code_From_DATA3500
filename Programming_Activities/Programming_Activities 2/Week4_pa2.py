#programming activity 3

a = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
for b in a:
    print(b)

print()

#programming activity 3 pt2
for i in range (5,96):
    confirm_5 = i%5
    if confirm_5 == 0:
        print(i)

print()

#programming activity 4
x = 5
while True:
    print(x)
    if x == 95:
        break
    else:
       x += 5

"""       
2. Write a Python program to reverse a given three or more digit integer 
WITHOUT using lists (hint, use // and % to isolate numbers)
"""
print()
print()
#additional challenge 1
pnumbers = [1,2,3,5,7,11,13,17,23]
for i in range(1,26):
    for pnumber in pnumbers:
        if i == pnumber:
            print(i)
            
            
#additional challenge 2
