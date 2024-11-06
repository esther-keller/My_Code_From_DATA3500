# #theme: spies

# #sentinal values / marker variable

# invaders = 0

# while invaders != 5:
#     print("This is the log for logging invaders.")
#     print("Please enter the nubmer of invaders that you see.")
#     invaders = int(input("Enter the number of invaders you see:"))
#     if invaders < 5:
#         print("There is no threat to national security.")
#     elif invaders == 5:
#         print("This is a problem.")
#     else:
#         print("This is a problem.")
# else:
#     print("Alert the CIA")
    
    
# #break and continue

# bomb_timer = 60
# diffuse_knowledge = True

# while bomb_timer >= 0:
#     print(bomb_timer)
#     bomb_timer -= 1
#     if diffuse_knowledge == True and bomb_timer == 5:
#         #print("Wow, you diffused that just in time! We almost died...")
#         continue
# else:
#     print("You're probably dead now.")
    

# #for loop
# secrets_stolen = 0 
# for i in range (100):
#     print('You have stolen', secrets_stolen, "secrets.")
#     secrets_stolen += 1
#     if i == 24:
#         print("That's enough secrets")
#         break
    
# #Boolean Variables
# #True or False

# are_you_a_spy = False
# are_you_a_student = True

# isRaining = False
# isStolen = False
# isWednesday = True

# if isStolen == True:
#     pass
# if isStolen:
#     pass

# while isWednesday == False:
#     pass
# while isWednesday:
#     pass


# good_spy = secrets_stolen > 25 #secrets_stolen is 24


#and 
print(True and True)
print(True and False) #if there's a false anywhere, it will be false!!!!
print(False and False)

isWednesday = True
isGoodSpy = False
if isWednesday and isGoodSpy:
    print("so cool.")

#or
print(True or False) #1+0 = 1
print(True or True) #1+1 = 1 #if there is ANY true, it will take it and be true
print(False or False) #0+0=0

if isWednesday or isGoodSpy:
    print("so cool")

#not
if not isWednesday: #not is always looking for false!
    print("yay")
    
if isWednesday and not isGoodSpy:
    print("I'm not sure how i feel about that.")