"""
    Day-05 : code
"""

#pratice 


#1.Slicing a list

#reverce a list using slice
players=["charles","martina","florence","eli"]
print(players[::-1]) 

#looping through a slice
print("Here are the frist three playes on my team: ")
for p in players[:3]:
    print(p)

#Copying a list
co=players
print(co)
#or 
co=players[:]
print(co)

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
•Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
•Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
•Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list.

"""

#4-10
list=["dog","cat","fish","buffolo","donkey","mom","charan","likitha"]
print("frist there element are : ")
print(list[:3])
print('Middle there element are : ')
print(list[3:6])
print("Last there item are : ")
print(list[-3:])

#2.tuple
#Use a for loop to print each food the restaurant offers
food_menu=("egg","fish","chicken")
for item in food_menu:
    print(item.title())

#The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
print("Food menu is ")
for item in food_menu:
    print(item.title())
print("Food menu after replacing :")
food_menu=("egg","Mutton","francs")
for i in food_menu:
    print(i)

#3.conditional statements

#Alien colors #1
print("Color Game is ")
print("1.green")
print("2.yellow")
print("3.red")
user=input("Choice any one color in the above :")
if(user=="green"):
    print("The player earned 5 points")
elif(user=="yellow"):
    print("You just earned 10 points")
elif(user=="red"):
    print("You just earned 15 points")
else:
    print("Your chocies is wrong")

#Stage of life
n=int(input("Enter your age : "))
if(n>0):
    if(n<2):
        print("baby")
    elif(n<4 and n>=2):
        print("Toddler")
    elif(n<13 and n>=4):
        print("Kid")
    elif(n<20 and n>=13):
        print("Teenager")
    elif(n<65 and n>=20):
        print("Adult")
    else:
        print("Elder")
else:
    print("the enter age is wrong")

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.
•If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
"""
n=input("Enter user name :")
if(n!="admin"):
    print(f"Hello {n},thank you for logging in again")
elif(n=="admin"):
    print(f"Hello {n}, would you like to see a status report?")
else:
    print("The username is invalid")


"""
Ordinal Numbers: Ordinal numbers indicate their position in a list, such as
1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•
Store the numbers 1 through 9 in a list.
•
Loop through the list.
•
Use an if-elif-else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
8th 9th", and each result should be on a separate line.
"""
num=[x for x in range(1,10)]
for x in num:
    if x == 1:
        print(f"{x}st")
    elif x == 2:
        print(f"{x}nd")
    elif x==3:
        print(f"{x}rd")
    else:
        print(f"{x}th")

"""
    Electricity Bill Calculator
    Calculate the bill based on units:
    * 0–100 → ₹2/unit
    * 101–200 → ₹3/unit
    * 201–500 → ₹5/unit
    * Above 500 → ₹8/unit
"""
bill=int(input("Enter your unit (that how many unit you got): "))
if(bill>0):
    if(bill<=100):
        print(f"The Electricity bill is ₹{bill*2} ")
    elif(bill<=200):
        print(f"The Electricity bill is ₹{bill*3} ")
    elif(bill<=500):
        print(f"The Electricity bill is ₹{bill*5} ")
    else:
        print(f"The Electricity bill is ₹{bill*8} ")
else:
    print("Your enter ")
