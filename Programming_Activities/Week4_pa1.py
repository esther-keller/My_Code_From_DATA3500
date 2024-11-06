
#Programming Activity 1
year_born = int(input("Please enter the year you were born."))

if year_born >= 1997:
    print("you are a zoomer.")
elif year_born >= 1981:
    print('you are a millenial.')
elif year_born >= 1965:
    print("you are a gen x.")
elif year_born >= 1946:
    print("you are a baby boomer.")
else:
    print("who the heck are you? you're old!")


#programming activity 2
print()
age = int(input("What is your age?"))
current_year = 2024

while age > 0:
    print("You were alive in", current_year)
    current_year -= 1
    age -= 1
else: 
    current_year -= 1
    print("You were born in", current_year)
    
