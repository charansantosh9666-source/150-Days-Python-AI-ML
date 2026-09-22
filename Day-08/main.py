#Day-08

#Inheritance
class Parent:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def info(self):
        print(f"{self.year} {self.make} {self.model}")

class Child(Parent):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

def main():
    mybike=Child("nissan","leaf",2024)
    mybike.info()

if __name__=="__main__":
    main()

#Defining Attributes and Methods for the Child Class

class Parent:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.parent=10

    def info(self):
        print(f"{self.year} {self.make} {self.model}")

class Child(Parent):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.ke=20


    def chan(self):
        print(f"{self.parent} from parent, {self.ke} from child")

def main():
    mybike=Child("nissan","leaf",2024)
    mybike.info()
    mybike.chan()

if __name__=="__main__":
    main()

#With Overriding Methods from the Parent Class
class Parent:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.parent=10
        self.milage=40

    def info(self):
        print(f"{self.year} {self.make} {self.model}")

    def showMilage(self):
        print(f"the milage is {self.milage} this is from the parent class")

class Child(Parent):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.ke=20


    def chan(self):
        print(f"{self.parent} from parent, {self.ke} from child")

    def showMilage(self):
        print("There is nothing about milage in child class")
def main():
    mybike=Child("nissan","leaf",2024)
    mybike.info()
    mybike.chan()
    mybike.showMilage()

if __name__=="__main__":
    main()

#With out Overriding Methods from the Parent Class
class Parent:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.parent=10
        self.milage=40

    def info(self):
        print(f"{self.year} {self.make} {self.model}")

    def showMilage(self):
        print(f"the milage is {self.milage} this is from the parent class")

class Child(Parent):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.ke=20


    def chan(self):
        print(f"{self.parent} from parent, {self.ke} from child")

    def showMilage(self):
        return super().showMilage()
def main():
    mybike=Child("nissan","leaf",2024)
    mybike.info()
    mybike.chan()
    mybike.showMilage()

if __name__=="__main__":
    main()

#Instances as Attributes

class roll:
    def __init__(self):
        self.rollNumber="AU"

    def rollMetho(self):
        print("This is from the class roll but not inheritanc , Instances as Attributes in class sample")

class sample:
    def __init__(self):
        self.name="charan"
        self.age=18
        self.roll=roll()

    def info(self):
        print(f"The name of Student is {self.name} the age is {self.age}")


def main():
    myclass=sample()
    print(myclass.roll.rollNumber)
    myclass.roll.rollMetho()


if __name__=="__main__":
    main()

"""
Q1.Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""
class IceCream:
    def __init__(self):
        self.flavor=["Venila","Staberry","Chocklet"]

    def flavors(self):
        print("The Ice Creaam Flavors are")
        a=1
        for i in self.flavor:
            print(f"{a}.{i}",end=" ")
            a+=1

class Restaurant:
    def __init__(self,Restaurant_Name,Restaurant_Place):
        self.RName=Restaurant_Name
        self.RPlace=Restaurant_Place
        self.icecream=IceCream()

    def info(self):
        print(f"The Restaurant Name is {self.RName}")
        print(f"The Place of Restaurant is {self.RPlace}")
        self.icecream.flavors()

def main():
    restaurant=Restaurant("HotPiza","Hyb")
    restaurant.info()

if __name__=="__main__":
    main()



"""
Q2. Single Inheritance
Create a class Animal with a method sound() that prints "Animal makes a sound".
Create a class Dog that inherits from Animal and add a method bark() that prints "Dog barks".
Create a Dog object and call both methods.
"""
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("\nDog barks")

def main():
    dog=Dog()
    dog.bark()
    dog.sound()

if __name__=="__main__":
    main()

