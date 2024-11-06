'''
loop (for loop probably)
changing variables on interations of the loop
variables
math 
augmented assignment
range function
if statement ?

'''

#set the variables - denominator, numerator, counter, pi
#start with a for loop -not sure what to loop over yet
#calculate pi - do the math
# divide 4 by denominator
# add 2 to denominator each interation of the loop
# augment assignment to flip the sign
# total it all together
# print it to the console increment our counter

#visually identify where we see 3.14 and 3.141 twice

numerator = 4
denominator = 1
count = 1
total = 0
# print(f"{numerator} / {denominator}")


for i in range (1,3001):
    pi = (numerator / denominator)
    if count % 2 == 0:
        total -= pi
    else:
        total += pi
        
    print (f"Iteration:{count} pi:{total}")
    denominator += 2
    count += 1
    

#3.14 @ 627 and 628

#3.141 @ 2424 an 2425































# numerator = -4
# counter = 1
# denominator = 1
# pi = (numerator / denominator)*-1


# for denominator in range(1,3001):
#     print(pi)
#     pi = pi + (numerator / (denominator + 2))*-1
#     counter += 1
    
    
    
'''
counter = 1
total = 0
numerator = 4 

for denominator in range (1, 6000, 2):
    if counter % 2 == 0:
        total -= (numerator / denominator)
    else: 
        total += numerator / denominator
    print("Iteration:", counter, ",Pi:", total)
    conter += 1
    
#3.14 twice ina row at interations 627 and 628
#3.141 twice in a row at interations 2454 and 2455
    
'''