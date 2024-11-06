# 3.4 
for row in range(2):
    for col in range(7):
        print('@','', end="")
    print()

print() #insert a space to differentiate problems

#3.9
while True:
    number = input("Please enter a 7-10 digit number.")
    ui = len(number)
    if ui == 7:
        num = int(number)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    elif ui == 8:
        num = int(number)
        print((num%100000000)//10000000)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    elif ui == 9:
        num = int(number)
        print((num%1000000000)//100000000)
        print((num%100000000)//10000000)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    elif ui == 10:
        num = int(number)
        print((num%10000000000)//1000000000)
        print((num%1000000000)//100000000)
        print((num%100000000)//10000000)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    else:
        print('Error. Please enter a 7-10 digit number.') 
    

print() #insert a space to differentiate problems


#3.11
tank = 0
x = 0
miles_list = []
gallons_list = []

while x == 0:
    miles_driven = int(input("Please input your miles driven."))
    gallons_used = int(input("Please input the number of gallons used."))
    miles_per_gallon = miles_driven / gallons_used
    tank += 1
    miles_list.append(miles_driven)
    gallons_list.append(gallons_used)
    print(f"You are currently getting {miles_per_gallon} mpg on tank {tank}")
    
    stop = input("Would you like to continue? enter 'y' for yes or 'n' for no.")
    if stop == 'y':
        pass
    elif stop == 'n':
        x = 1
        break
    else: 
        print("Error. Please try again.")

print() #give a visual break so that you can clearly see the output
total_mpg = (sum(miles_list) / sum(gallons_list))
print(f"You had a total of {round(total_mpg, 2)} mpg over a total of {tank} tanks.")


print() #insert a break


#3.12
while True:

    ui = input("Please input a 5 digit number.")
    if len(ui) != 5:
        print("Error. Please try again.")
    else:
        pass
    ui = int(ui)
    if (ui // 10000) == (ui % 10) and (ui // 100000) == (ui % 1):
        print("Palindrome!")
        stop = input("Would you like to continue? Please input y for yes or n for no.")
        if stop == 'y':
            break
        else:
            pass
    else:
        print("Yikes. Not a Palindrome.")

#3.14

numerator = 4
denominator = 1
count = 1
total = 0

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