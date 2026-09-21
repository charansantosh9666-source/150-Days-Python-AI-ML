#Day-07

#Object Oriented Programmin (OOP):-

#1.Creating and Using a Class
#creating a Dog Class
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


def main():
    my_dog=Dog("luky",20)
    your_dog=Dog("husky",9)
    print(f"The name of Dog is {my_dog.name}")
    print(f"The age of my Dog is {my_dog.age}")
    my_dog.sit()
    my_dog.roll_over()


if __name__ == "__main__":
    main()

#2.Creating Multiple Instances
class Student:
    def __init__(self,roll_no,name,age):
        self.roll=roll_no
        self.name=name
        self.age=age

    def info(self):
        print(f"The roll number of student is {self.roll}")
        print(f"The Name of Student is {self.name}")
        print(f"The age of student is {self.age}")

def main():
    stud1=Student(101,"charan",18)
    stud2=Student(102,"bhavani",40)
    stud3=Student(103,"srinivasu",50)
    stud1.info()
    stud2.info()
    stud3.info()

if __name__=="__main__":
    main()


"""
pratice
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.RName=restaurant_name
        self.Cuisin=cuisine_type

    def describe_restaurant(self):
        print(f"The Restaurant Name is {self.RName}")
        print(f"The Cuisine Type is {self.Cuisin}")

    def open_restaurant(self):
        print("Indicating that the restaurant is open.")

def main():
    restaurant1=Restaurant("Holly brid","Good")
    restaurant2=Restaurant("Happy brid","Super")
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()


if __name__=="__main__":
    main()


"""
pratice
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both meth-
ods for each user.
"""

class User:
    def __init__(self,first_name,last_name):
        self.FName=first_name
        self.LName=last_name

    def describe_user(self):
        print(f"The first name of the user is {self.FName}")
        print(f"The last name of the user is {self.LName}")

    def greet_user(self):
        print(f"Good morning {self.FName} {self.LName}")

def main():
    user1=User("Charan","Santosh")
    user2=User("Likitha","Karinki")
    user3=User("Adhi","Penukonda")
    user1.describe_user()
    user1.greet_user()
    user2.describe_user()
    user2.greet_user()
    user3.describe_user()
    user3.greet_user()

if __name__=="__main__":
    main()

#3.Working with Classes and Instances
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

def main():
    my_new_car=Car("audi","a4",2024)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

if __name__=="__main__":
    main()


"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
class User:
    def __init__(self,name):
        self.name=name
        self.login_attempt=0

    def increment_login_attempts(self):
        self.login_attempt+=1

    def resert_login_attempts(self):
        self.login_attempt=0

def main():
    user1=User("charan")
    user2=User("santosh")
    n=True
    while(n):
        name=input("Enter username : ")
        print("1.Login")
        print("2.Reset the login attempt")
        print("3.Exit")
        a=int(input("Enter the choice (1 or 2 or 3): "))
        print(a)
        if a==1:
            if name==user1.name:
                user1.increment_login_attempts()
                print(f"The {name} is login in {user1.login_attempt} times")
            elif name==user2.name:
                user2.increment_login_attempts()
                print(f"The {name} is login in {user2.login_attempt} times")
            else:
                print("The enter user name is invalid")
        elif a==2:
            if name==user1.name:
                user1.resert_login_attempts()
                print(f"Now the user Login in {user1.login_attempt} times")
            elif name==user2.name:
                user2.resert_login_attempts()
                print(f"Now the user Login in {user1.login_attempt} times")
            else :
                print("The user name is invalid")
        elif a==3:
            n=False
            print(f"Thank you {name} viste agin")
        else:
            print("The choice is invalid ")

if __name__=="__main__":
    main()
        
            

