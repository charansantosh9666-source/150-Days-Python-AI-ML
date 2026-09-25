#Day-09
#Learning and coding
#1.Encapsulation

#Exercise 1 — Student
#Using Method get_marks(),set_marks()

class Student:
    def __init__(self,marks):
        self.__marks=marks
        self._name="charan"

    def get_mark(self):
        return self.__marks

    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
def main():
    s=Student(50)
    s.set_marks(10)
    print(s.get_mark())
    print(s._name)

if __name__=="__main__":
    main()

#Exercise 2 — BankAccount
#Using methods deposit(),withdraw(),get_balance()

class BankAcoount:

    def __init__(self,money):
        self.__money=money

    def get_balance(self):
        return self.__money

    def deposit(self,val):
        if 0 < val<=100000:
            self.__money+=val

    def withdraw(self,val):
        if 0<val<=self.__money:
            self.__money=self.__money-val

def main():
    bank=BankAcoount(10000)
    bank.deposit(100)
    print(bank.get_balance())
    bank.withdraw(10000)
    print(bank.get_balance())

if __name__=="__main__":
    main()


#Exercise 3 — Employee
#Create: 
# get_salary() 
# set_salary() 
# Don't allow a negative salary.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,val):      
        self.__salary=val

def main():
    emp1=Employee("charan",20000)
    emp2=Employee("santosh",50000)
    print(f"The employee 1 name is {emp1.name} there salary is {emp1.get_salary()}")
    print(f"The employee 2 name is {emp2.name} there salary is {emp2.get_salary()}")
    emp1.set_salary(50000)
    emp2.set_salary(100000)
    print(f"Now The employee 1 name is {emp1.name} there salary is {emp1.get_salary()}")
    print(f"Now The employee 2 name is {emp2.name} there salary is {emp2.get_salary()}")

if __name__=="__main__":
    main()

#Exercise 4 — @property
class Student:
    def __init__(self,marks):
        self.__marks=marks

    @property

    def get_marks(self):
        return self.__marks

    @get_marks.setter

    def set_marks(self,val):
        if 0<=val<=100:
            self.__marks=val

def main():
    st=Student(99)
    print(st.get_marks)
    st.set_marks=10
    print(st.get_marks)

if __name__=="__main__":
    main()


#Exercise 5 — School
# Create: class Student
# Class variable:
# school = "ABC School"
# Instance variables:
# name
# age
# Create 3 students and print their information.

class Students:
    school="ABC school"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
def main():
    st1=Students("Charan",18)
    st2=Students("Santosh",20)
    print(st1.name,end=" ")
    print(st1.age,end=" ")
    print(st1.school)
    print(st2.name,end=" ")
    print(st2.age,end=" ")
    print(st2.school)


if __name__=="__main__":
    main()

#Exercise 2 — Car
# Create:
# Car
# Class variable:
# wheels = 4
# Instance variables:
# brand
# model
# Create 3 cars.

class Car:

    wheels=4

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

def main():
    car1=Car("toyata","as23")
    car2=Car("BMW","A4")
    print(car1.brand.title(),end=" ")
    print(car1.model.title(),end=" ")
    print(car1.wheels)
    print(car2.brand.title(),end=" ")
    print(car2.model.title(),end=" ")
    print(car2.wheels)

if __name__=="__main__":
    main()

#Exercise 3 — Employee Company
# Create:
# Employee
# Class variable:
# company = "TechCorp"
# Instance variables:
# name
# salary
# Create 3 employees.
# Print:
# Name
# Salary
# Company

class Employee:
    company="TechCorp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

def main():
    emp1=Employee("charan",200000)
    emp2=Employee("Santosh",300000)
    print(emp1.name,end=" ")
    print(emp1.salary,end=" ")
    print(emp1.company)
    print(emp1.name,end=" ")
    print(emp1.salary,end=" ")
    print(emp1.company)

if __name__=="__main__":
    main()


#Exercise 4 — Object Counter ⭐
# Create:
# Student
# Class variable:
# count = 0
# Every time a Student object is created, increase count.

class Student:
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1

def main():
    std1=Student("Charan")
    std2=Student("Santosh")
    std3=Student("Likitha")

    print(Student.count)

if __name__=="__main__":
    main()
        