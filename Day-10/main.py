#Day-10

#1.class method 
#class example
class Student:
    def study(self):
        print("Student is studying")

def main():
    s1 = Student()
    s1.study()

if __name__=="__main__":
    main()

#class method example
class Student:

    @classmethod
    def hello(cls):
        print("Hello")

def main():
    s1 = Student()
    s1.hello()

if __name__=="__main__":
    main()

#Simple example
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

def main():
    
    Student.show_school()

if __name__=="__main__":
    main()

#using the cls
class Student:

    school="ABC School"

    @classmethod
    def chang_school(cls,new_student):
        cls.school=new_student

def main():

    print(Student.school)
    Student.chang_school("XYZ School")
    print(Student.school)

if __name__=="__main__":
    main()

#Class methods can access class variables
class Car:

    wheels = 4

    @classmethod
    def show_wheels(cls):
        print(cls.wheels)

def main():
    Car.show_wheels()

if __name__=="__main__":
    main()


#Class methods cannot directly use instance variables
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))
    
def main():
    s1 = Student.from_string("Rahul-20")
    print(s1.name)
    print(s1.age)

if __name__=="__main__":
    main()


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2026
        age = current_year - birth_year
        return cls(name, age)

def main():
    p1 = Person.from_birth_year("Rahul", 2005)
    print(p1.name)
    print(p1.age)

if __name__=="__main__":
    main()

#Q1.What is the purpose of @classmethod?
# A. Creates an object
# B. Makes a method receive the class as its first argument
# C. Makes a method private
# D. Makes a method static

#ans=B

#Q2.Create a class called Employee.
# It should have:
# name
# salary
# company
# Create a class method that changes the company name.

class Employee:
    name="cha"
    salary=2000000
    company="abc"

    @classmethod
    def change_company(cls,com):
        cls.company=com

def main():
    
    Employee.change_company("def")
    print(Employee.company)
    
if __name__=="__main__":
    main() 

#Q12 ⭐ Challenge
# Create:
# class Product:
# with:
# name
# price
# Then create a class method:

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show(self):
        print(self.name,self.price)

    @classmethod
    def from_string(cls,data):
        name,price=data.split("-")
        return cls(name,price)

def main():
        e1=Product.from_string("chai-20")
        e1.show()

if __name__=="__main__":
    main()


#Polymorphism
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

def main():
    dog=Dog()
    cat=Cat()
    dog.speak()
    cat.speak()

if __name__=="__main__":
    main()


#Duck Typing
class Dog:

    def speak(self):
        print("Woof")


class Cat:

    def speak(self):
        print("Meow")


class Robot:

    def speak(self):
        print("Beep")

def make_sound(obj):
    obj.speak()

def main():
    make_sound(Dog())
    make_sound(Cat())
    make_sound(Robot()) 

if __name__=="__main__":
    main()


#Polymorphism with inheritance

class Animal:

    def speak(self):
        print("Animal sound")

class Dog(Animal):

    def speak(self):
        print("Woof")

class Cat(Animal):

    def speak(self):
        print("Meow")

def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        animal.speak()

if __name__=="__main__":
    main()


# Method overriding vs polymorphism
#Real-world example:-
class UPI:
    def pay(self,amount):
        print(f"Paid ${amount} using UPI")

class CreditCard:
    def pay(self,amount):
        print(f"Paid ${amount} using CreditCard")

class Cash:
    def pay(self,amount):
        print(f"Paid ${amount} using Cash")

def process_payment(method,amount):
    method.pay(amount)

def main():
    process_payment(CreditCard(), 500)
    process_payment(UPI(), 500)
    process_payment(Cash(), 500)  

if __name__=="__main__":
    main()

