# theme of the day: Pirates

treasure = 0

treasure = treasure + 1
print("treasure:",treasure, "coin")

#augmented assignment
treasure += 1
print("treasure:",treasure, "coin")
treasure -= 2
print("treasure:",treasure, "coin")
treasure += 1000
treasure *= 100
print("treasure:",treasure, "coin")
treasure /= 100
print("treasure:",treasure, "coin")
treasure %= 10
print("treasure:",treasure, "coin")
treasure //= 3
print("treasure:",treasure, "coin")

#for loops
    #will only ever run over a range of values
#loop over lists, ranges, variables, objects, dictionaries, strings
#looping through string
print()
name = "Captian K"
for letter in name:
    print("letter:", letter)
#looping through a range
print()
for i in range(20): #range function is non inclusive on the right end of range
    print(i)
#looping through a list
print()
ships = ['The Black Pearl', 'The Flying Dutchman', "Queen Ann's Revenge"]
for ship in ships:
    print("ship:", ship)
    if ship == "The Flying Dutchman":
        print("Post the colors!!!")
        
#looting 25 islands
loot = 0
current_island = 1

#initalize treasure hold
for i in range(3)
    loot += 1
    print("Loot count:", loot)
    
#commence the robbery    
for i in range(25):
    print("Current island:", current_island, "robbing now.")
    loot *= 2
    print("Your treasure hold currently has" + str(loot) + "coins in it.")
    current_island += 1