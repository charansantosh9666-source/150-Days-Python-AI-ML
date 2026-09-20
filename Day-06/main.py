#Day-06
#pratice agin the last topics

# 1.DICTIONARIES:-

#Starting with empty dictionary 
dic={}
dic["color"]="green"
dic["points"]=5
print(dic)

#update the dictionaries key valuses and deleting key 
a={"c":0,"a":0}
a["c"]+=1
print(a)
del a["a"]
print(a)

#creating a dictionarie with using list and updating 
a=[1,2,3,1,2,3]
ans={x:0 for x in a}
print(ans)
for i in a:
    ans[i]+=1
print(ans)

#using get() to Access values
name={"charan":2,"santosh":1,"bhavani":4}
val=name.get("bhavani","There is no name like this")
print(val)
val=name.get("vamshi","There is no name like this in data base ")
print(val)


#1.Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each piece
#of information stored in your dictionary.
person={
    "Charan":{"Frist_Name":"Charan Santosh","Last_Name":"Karinki","Age":18,"City":"Hyb"},
    "Bhavani":{"Frist_Name":"Bhavani","Last_Name":"Karinki","Age":40,"City":"Kvr"},
    "Likitha":{"Frist_Name":"Likitha","Last_Name":"Karinki","Age":16,"City":"Mogg"}
}
n=input("Enter the name want to sherch : ")
val=person.get(n.title(),"There is no information about the persion")
print(val)


#2.Use a dictionary to store people’s favorite numbers.Think of five names,and use them as keys in your dictionary.
#  Think of a favoritenumber for each person, and store each as a value in your dictionary.
# Printeach person’s name and their favorite number.
fav_num={
    "Likitha":3,
    "Bhavani":3,
    "Charan":6,
}
for key in fav_num:
    print(f"The persion {key} fov number is {fav_num[key]}")

    
#3.Start with the program you wrote for Exercise 6-1 (pag3.e 98). Make
#two new dictionaries representing different people, and store all three dictionar-
#ies in a list called people. Loop through your list of people. As you loop through
#the list, print everything you know about each person.
person1={
    "Charan":{"Frist_Name":"Charan Santosh","Last_Name":"Karinki","Age":18,"City":"Hyb"},
}
person2={
    "Bhavani":{"Frist_Name":"Bhavani","Last_Name":"Karinki","Age":40,"City":"Kvr"},
}
person3={
    "Likitha":{"Frist_Name":"Likitha","Last_Name":"Karinki","Age":16,"City":"Mogg"}
}
person=[person1,person2,person3]
print(person)


# 2.Function:-

#1.Write a function called display_message() that prints one sen-
#tence telling everyone what you are learning about in this chapter. Call the
#function, and make sure the message displays correctly.
def display_message():
    print("what you are learning about in this chapter")

display_message()
display_message()

#2.Write a function called describe_city() that accepts the name of
#a city and its country. The function should print a simple sentence, such as
#Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the
#default country.
def describe_city(city,country):
    print(f"The {city.title()} is in {country.title()}")

describe_city("hyb","ind")
describe_city("reykjavik","irland")

#3. Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
album={}
def make_album(Aname,title):
    album[Aname]=title

make_album("charan","AI")
make_album("santosh","ML")
print(album)


#4.Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.
album={}
def make_album(Aname,title):
    album[Aname]=title

def Input_User():
    a=input("Enter Album's Name : ")
    b=input("Enter Album's Title : ")
    make_album(a,b)

def Display():
    for key,val in album.items():
        print(f"The Albums Name is {key.title()} and The title of Aldum is {val.title()} ")
    if album=={}:
        print("The Album is Empty!")

def main():
    n=True
    while(n):
        print("1.Make Aldum")
        print("2.Display Aldum")
        print("3.Exist")
        print("Enter your choice : ",end="")
        c=int(input())
        if c==1:
            Input_User()
        elif c==2:
            Display()
        elif c==3:
            n=False
        else:
            print("Invalid choice Enter agin")

main()

