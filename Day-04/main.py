"""
    Day-04: code 
"""

#pratice 

#1.Assignment to variables

"""1. variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message."""

Fav_Num= int(input("Enter your favorite number"))
print(f"Your Favorite Number is {Fav_Num}")

"""2.Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”"""

Name_User=input("Enter your name : ")
print(f"Hello {Name_User.title()}, would you like to learn Python today")

#2.list

""" 1.Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time."""
Name=["charan","santosh","adhi","sunil","yogi"]
for i in Name:
    print(f"{i.title()}" ,end=" ")
print()
for i in Name:
    print(f"Hello {i.title()} wellcom")

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in
your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
•Use insert() to add one new guest to the beginning of your list.
•Use insert() to add one new guest to the middle of your list.
•Use append() to add one new guest to the end of your list.
•Print a new set of invitation messages, one for each person in your list.
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
•Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
•Print a message to each of the two people still on your list, letting them
know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""
def messsage(lis):
    for i in lis:
        print(f"Hey {i.title()} come to my party at 3pm")


#3-4
Guest=["charan","likitha","bhavani"]
messsage(Guest)

#3-5
Not_Comming=input("Enter the name that con't coming :")
Guest.remove(Not_Comming)
print(Guest)
Guest.append("Srinivasu")
print(Guest)
messsage(Guest)

#3-6
name=input("Enter the new guest name :")
Guest.insert(0,name)
l=len(Guest)
mid=l//2
name=input("Enter the new guest name :")
Guest.insert(mid,name)
name=input("Enter the new guest name :")
Guest.append(name)
print(Guest)
messsage(Guest)


"""
3-8. Seeing the World: Think of at least five places in the world you’d like
to visit.
•Store the locations in a list. Make sure the list is not in alphabetical order.
•Print your list in its original order. Don’t worry about printing the list neatly;
just print it as a raw Python list.
•Use sorted() to print your list in alphabetical order without modifying the
actual list.
•Show that your list is still in its original order by printing it.
•Use sorted() to print your list in reverse-alphabetical order without chang-
ing the order of the original list.
•Show that your list is still in its original order by printing it again.
•Use reverse() to change the order of your list. Print the list to show that its
order has changed.
•Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
•Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
•Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the number
of people you’re inviting to dinner.
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""

#3-8
world=["India","Japan","USA","Aus","Cheina"]
print("Original List :",end="  ")
print(world)
print("Sorted list in alpa order: ")
print(sorted(world))
print("There is an orginal list ")
print(world)
world.reverse()
print(world)
world.reverse()
print(world)
world.sort()
print(world)
world.sort(reverse=True)
print(world)

"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
•Modify your for loop to print a sentence using the name of the pizza,
instead of printing just the name of the pizza. For each pizza, you should
have one line of output containing a simple statement like I like pep-
peroni pizza.
•Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
4-2. Animals: Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
•Modify your program to print a statement about each animal, such as A
dog would make a great pet.
•Add a line at the end of your program, stating what these animals have in
common. You could print a sentence, such as Any of these animals would
make a great pet!
"""

#4-1
pizza=["Panner Pizza","Pepperoni Pizza","Chiken Pizza"]
for p in pizza:
    print(f"I like {p} ")
    print(f"I really love {p}")

#4-2
animal=["dog","cat","fish"]
for a in animal:
    print(f"{a} would make a great pet\n")

print("Any of these animal would make a great pet!")

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each in
"""

#4-3
for i in range(1,21):
    print(i)

#3.list comprehension

#4-5
list=[x for x in range(1,1000001)]
sum(list)

#4-6
list=[x for x in range(1,21) if x%2!=0]
print(list)

#4-7
list=[x for x in range(3,31) if x%3==0]
print(list)


# Use a list comprehension to generate a list of the first 10 cubes.
list=[x**3 for x in range(1,11)]
print(list)
