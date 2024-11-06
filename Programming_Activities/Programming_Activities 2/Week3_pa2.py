# current_pres_num = 46

# print("Type:", type(float(current_pres_num)))
# print("Type:", type(str(current_pres_num)))
# print("Type:", type(bool(current_pres_num)))
# print("Type:", type(int(current_pres_num)))

# print()

# days_left = 54
# day = input("How many days until election day?")
# if day - days_left == 0:
#     feeling = input("How do you feel about that?")


#number of votes
# votes_required = 270
# d_trump_votes = 0
# k_harris_votes = 0
# s_dogg = 538

# if d_trump_votes >= votes_required:
#     print("Congrats Donald!")
# elif k_harris_votes >= votes_required:
#     print("Congrats Kamala!")
# else:
#     print("Congrats Snoop!")


#how to determine an election year
# last_election_year = int(input("In what year was the last election?"))
# next_election = last_election_year +4
# print("The next election will be held in the year", next_election)
# current_year = int(input("What is the currrent year?"))
# if current_year == next_election:
#     print("OMG,"current_year, "is an election year! Go vote!")



#programming activity 2
while True:
    current_age = input("Please input your current age.")
    try:
        current_age = eval(current_age)
        confirm = input(f"Please confirm your current age is {current_age} by entering 'y' or 'n'.")
        if confirm == 'y':
            break
        else:
            pass      
    except:
        print("Error. Please try again.")
            
while True: 
    death_age = input("Please input the age you would like to live until.")
    try: 
        death_age = eval(death_age)
        confirm2 = input(f"Please confirm your current age is {death_age} by entering 'y' or 'n'.")
        if confirm2 == 'y':
            break
        else:
            pass
    except:
        print("Error. Please try again.")
print("Unfortunatly, you have", death_age - current_age, "years to live.")


#programming activity 3
print() #clearly define the new problem
while True:
    grade = input("Please input your grade in this class as a 2 digit number")
    try:
        grade = eval(grade)
        break
    except:
        print("Error. Please try again.")
if grade >= 93: 
    print("Congratulations you have an A in the class!")
else: 
    print("You are a great person!")