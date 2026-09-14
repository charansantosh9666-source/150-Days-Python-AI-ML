#DAY-1. coding and Exercise  



#Question 1: Personal Information
# Write a Python program that asks the user for their personal information.
# Your program should take:
# Full name
# Age
# City
# Country
# Phone number
# Email
# Height in cm
# Whether they are a student (True/False)
# Then display the information in a clean format.


name=input("Enter your name : ")
age=int(input("Enter your age : "))
city=input("Enter your city : ")
coutry=input("Enter your country name : ")
phone=int(input("Enter your phone number :"))
email=input("Enter your emal : ")
h=int(input("Enter your height in cm : "))
print("\n\n=================== PERSONAL INFORMATION ===================\n\n")
print(f"Name           : {name}")
print(f"Age            : {age}")
print(f"City           : {city}")
print(f"Country        : {coutry}")
print(f"Phone          : {phone}")
print(f"Email          : {email}")
print(f"Height         : {h}")
print("\n\n============================================================")

#Question 2: Simple Calculator
# Create a calculator program.
# Ask the user for:
# First number
# Second number
# Then ask:
# Enter operation (+, -, *, /)

f=int(input("Enter frist number : "))
s=int(input("Entyer secound number : "))
print("Enter any operator form these (+,-,*,/) : ",end=" ")
o=input()
if("+"==o):
    print(f"The sum of {f} and {s} is equal to {f+s}")
elif("-"==o):
    print(f"The subtraction of {f} and {s} is equal to {f-s}")
elif("*"==o):
    print(f"The multiply of {f} and {s} is equal to {f*s}")
elif("/"==o):
    if(s!=0):
        print(f"The division of {f} and {s} is equal to {f/s}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

    

#Question 3: Calculator With More Operations
# Upgrade your calculator.
# Support:
# +
# -
# *
# /
# %
# **
# //



def inp():
    a=int(input("Enter frist number : "))
    b=int(input("Enter secound number : "))
    return a,b
def add(a,b):
    print(f"Adding the {a} and {b} is equal {a+b}")
def sub(a,b):
    print(f"Subtrating the {a} and {b} is equal {a-b}")
def mul(a,b):
    print(f"Multiplying the {a} and {b} is equal {a*b}")
def div(a,b):
    print(f"Division the {a} and {b} is equal {a/b}")
def mod(a,b):
    print(f"Modulus the {a} and {b} is equal {a%b}")
def po(a,b):
    print(f"Power the {a} and {b} is equal {a**b}")
def flo(a,b):
    print(f"Floor division the {a} and {b} is equal {a//b}")
def ex():
    n=False
    return n

def main():
    n=True    
    while(n):
        print("\n=============== MENU ==============\n")
        print("1.Adding(+)")
        print("2.Subtrating(-)")
        print("3.Multiplying(*)")
        print("4.Division(/)")
        print("5.Modulus(%)")
        print("6.Power(**)")
        print("7.Floor division(//)")
        print("8.Exit\n")
        num=int(input("Enter Your Choice : "))
        if(num==1):
            a,b=inp()
            add(a,b)
        elif(num==2):
            a,b=inp()
            sub(a,b)
        elif(num==3):
            a,b=inp()
            mul(a,b)
        elif(num==4):
            a,b=inp()
            div(a,b)
        elif(num==5):
            a,b=inp()
            mod(a,b)
        elif(num==6):
            a,b=inp()
            po(a,b)
        elif(num==7):
            a,b=inp()
            flo(a,b)
        elif(num==8):
            print("Thank you !!!!!")
            n=ex()
        else:
            print("Invalid choice   !!!!!!!")


main()



#Question 4: Simple Interest Calculator
# Write a program that calculates Simple Interest.
# Formula:
# Simple Interest = (P × R × T) / 100
# Where:
# P = Principal amount
# R = Rate of interest
# T = Time

def checkP(p):
    if(p>0):
        return p
    else:
        print("Invalid Principal amount")
        p=int(input("Enter princial amount : "))
        p=checkP(p)
        return p

def checkR(r):
    if(r>0):
        return r
    else:
        print("Invalid interest rate !!")
        r=int(input("Enter princial amount : "))
        r=checkR(r)
        return r
def main():
    p=int(input("Enter princial amount : "))
    r=int(input("Enter Rate of interest : "))
    t=int(input("Enter Time in year : "))
    p=checkP(p)
    r=checkR(r)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    si=(p*r*t)//100
    TAm=p+si
    print(f"\nPrincipal      : ${p}")
    print(f"Rate           : {r}%")
    print(f"Time           : {t}years")
    print(f"Interest       : ${si}")
    print(f"Total          : ${TAm}")


main()



#Question 5: Basic Login Validation
# Create a login system.
# Store these values in your program:
# Username: admin
# Password: python123
# Ask the user:
# Enter username:
# Enter password:
# If both are correct:
# Login successful!
# Welcome, admin.
# If username is wrong:
# Invalid username.
# If username is correct but password is wrong:
# Invalid password.

def check(a,b,s):
    if(a==b):
        return 1
    else:
        print(f"Invalid {s}")
        return 0

def main():
    userName="admin"
    password="python123"
    name=input("Enter username : ")
    passw=input("Enter password : ")
    s="username"
    if(check(userName,name,s)):
        s="password"
        if(check(password,passw,s)):
            print("Login successful!")
            print(f"Welcome, {userName}")


main()



#Question 7: Login Validation System
# Create these variables:
# correct_username
# correct_password
# account_active
# Ask the user for username and password.
# Rules:
# Rule 1
# If username is incorrect:
# Invalid username.
# Rule 2
# If username is correct but password is incorrect:
# Invalid password.
# Rule 3
# If username and password are correct but account is inactive:
# Your account is inactive.
# Rule 4
# If everything is correct:
# Login successful!
# Welcome back.



"""
Your decision structure should roughly behave like:

Username correct?
│
├── NO → Invalid username
│
└── YES
      │
      Password correct?
      │
      ├── NO → Invalid password
      │
      └── YES
            │
            Account active?
            │
            ├── NO → Account inactive
            │
            └── YES → Login successful

"""

def use(user,enter):
    if(user==enter):
        return True
    else:
        print("Invalid Username")
        enter=input("Enter Username : ")
        return use(user,enter)

def pas(passw,enter):
    if(passw==enter):
        return True
    else:
        print("Invalid Password")
        enter=input("Enter Password : ")
        return pas(passw,enter)

def main():
    username="charan"
    password="charan@123"
    account_active=False
    enter=input("Enter username : ")
    if(use(username,enter)):
        enter=input("Enter password : ")
        if(pas(password,enter)):
            if(account_active):
                print("Login successful!")
                print(f"Welcom {username}")
            else:
                print("Your account is inactive.")


main()



#Level 1 — Variables and Print
#Exercise 1
# Create variables for:
# name
# age
# city
# Print them in one sentence.

name=input("Enter your name:")
age=int(input("Enter your age:"))
city=input("Enter your city name:")
print(f"Your name is {name}")
print(f"Your age is {age}")
print(f"Your City name is {city}")


#Exercise 2
#Create:
#a = 10
#b = 20
#Print:
#30
#-10
#200
#0.5
#using expressions.

a , b= 10,20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Exercise 3
#Create a variable called is_student and store a boolean in it. Print its type.



is_student=True
print(type(is_student))


#Level 2 — Strings
#Exercise 4
#Given:
#word = "Python"
#Print:
#P
#n
#Py
#thon



s="Python"
print(s[0])
print(s[-1])
print(s[:2])
print(s[2:])




#Exercise 5
# Create:
# first_name = "Ada"
# last_name = "Lovelace"
# Print:
# Ada Lovelace
# using an f-string.


first_name="Ada"
last_name="Lovelace"
print(f"{first_name} {last_name}")


# Exercise 6
# Predict:
# print("ha" * 4)

print("ha" *4)


  
#Level 3 — Conditions
# Exercise 7
# Ask for a number and print:
# Positive
# Negative
# Zero


num=int(input("Enter any number :"))
if(num==0):
    print("The number is Zero")
elif(num>0):
    print("The number is positive")
else:
    print("The number is negative")


#Exercise 8
# Ask for age and print:
# Adult
# when age is 18 or above; otherwise:
# Minor

age =int(input("Enter your age :"))
if(age>=18):
    print("Adult")
else:
    print("Minor")

#Exercise 9
# Ask for a number and determine whether it is even or odd.
# Hint:
# number % 2

num=int(input("Enetr a number : "))
if(num%2==0):
    print("It is Even number")
else:
    print("It is Odd number")

    

#Exercise 10
# Given:
# age = 25
# has_id = True
# Print "Allowed" only if both are true:
# age >= 18
# has_id

age, has_id=25,True
if(age>=18 and has_id):
    print("Allowed")
else:
    print("Not Allowed")

