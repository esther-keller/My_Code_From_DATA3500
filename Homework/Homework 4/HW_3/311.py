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

print()
total_mpg = (sum(miles_list) / sum(gallons_list))
print(f"You had a total of {round(total_mpg, 2)} mpg over a total of {tank} tanks.")







# print(sum(miles_list))
# print(sum(gallons_list))

# for mile in miles_list:
#     print(mile)
# print()
# for gallon in gallons_list:
#     print(gallon)



# print(f"You used a total of {tank} tanks of gas")
# print(f"You had a cumulative {total_miles} miles")
# print(f"You used a cumulative {total_gallons} gallons of gas.")
# print(f"Your total MPG is: {total_mpg}")
    
    

    
    

    