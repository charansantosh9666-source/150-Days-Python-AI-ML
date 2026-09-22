# 🐍 Day 08 — Inheritance in Python

Today I learned about **Inheritance in Python**, an important concept of Object-Oriented Programming (OOP).

## 📚 Topics Covered

* What is Inheritance?
* Parent Class and Child Class
* Single Inheritance
* Multilevel Inheritance
* Multiple Inheritance
* Method Overriding
* `super()` Function
* Method Resolution Order (MRO)
* Constructors in Inheritance

## 🔹 What is Inheritance?

Inheritance allows a class to **reuse the properties and methods of another class**.

The class being inherited from is called the **Parent/Base class**, while the class that inherits from it is called the **Child/Derived class**.

### Basic Syntax

```python
class Parent:
    def show(self):
        print("This is the parent class")


class Child(Parent):
    pass


obj = Child()
obj.show()
```

## 🔹 Types of Inheritance

### 1. Single Inheritance

One child class inherits from one parent class.

```text
Parent
   ↓
Child
```

### 2. Multilevel Inheritance

A class inherits from another child class.

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

### 3. Multiple Inheritance

One child class inherits from multiple parent classes.

```text
Parent1     Parent2
    \         /
       Child
```

## 🔹 Method Overriding

A child class can provide its own implementation of a method that already exists in the parent class.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()
```

Output:

```text
Dog barks
```

## 🔹 `super()` Function

The `super()` function is used to access methods or the constructor of the parent class.

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


student = Student("Rahul", 101)

print(student.name)
print(student.roll_no)
```

## 🔹 Method Resolution Order (MRO)

MRO determines the order in which Python searches for methods and attributes when inheritance is involved.

We can check the MRO using:

```python
print(ClassName.mro())
```

or:

```python
print(ClassName.__mro__)
```

## 🧠 Key Learnings

* Inheritance promotes **code reusability**.
* A child class can use methods and attributes from its parent class.
* Child classes can **override** parent methods.
* `super()` helps access parent-class functionality.
* Python supports **multiple inheritance**.
* MRO determines the method lookup order.

## 📝 Practice

Today I practiced inheritance using examples involving:

* `Animal` and `Dog`
* `Person` and `Student`
* `Vehicle`, `Car`, and `SportsCar`
* Multiple inheritance
* Method overriding
* `super()`

## 🚀 Conclusion

Day 08 helped me understand how **Inheritance** works in Python and how it can be used to build reusable and organized OOP programs.

> **Day 08 Complete ✅ — Keep Learning, Keep Coding! 🐍🔥**
