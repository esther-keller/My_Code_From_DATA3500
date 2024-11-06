#programming activity 1

def welcome_fctn(name):
    return print("Welcome " + name)
    
your_name = input("Input your name. ")  
welcome_fctn(your_name)
#print(welcome_fctn(your_name))


#programming activity 2

def welcome_fctn(name):
    welcome_message = ("Welcome " + name)
    print(welcome_message)
    
your_name = input("Input your name. ")  
welcome_fctn(your_name)


#programming activity 3

def welcome_fctn(name, age, favorite_color):
    return print("Welcome " + name + " you are" + " " + age + " " + "years old, and " + favorite_color + " is your favorite color")
    
your_name = input("Input your name. ")  
your_age = int(input("Input your age."))
your_favorite_color = input("Input your favorite color.")
welcome_fctn(your_name, str(your_age), your_favorite_color)
