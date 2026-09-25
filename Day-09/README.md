# Day-09 – Python OOP Practice

This project contains my Day-09 Python practice programs focused on **Encapsulation and Class Variables** in Object-Oriented Programming (OOP).

## Topics Covered

### 1. Encapsulation

The project demonstrates how to protect and control access to data inside a class.

Concepts practiced:

* Private attributes using `__`
* Protected attributes using `_`
* Getter methods
* Setter methods
* Data validation
* Controlling access to object data

### 2. Student Class – Encapsulation

A `Student` class is created to practice private attributes and getter/setter methods.

Features include:

* Private `__marks` attribute
* Protected `_name` attribute
* `get_mark()` method
* `set_marks()` method
* Validating marks between `0` and `100`

Example:

```python
class Student:
    def __init__(self, marks):
        self.__marks = marks
        self._name = "charan"
```

### 3. BankAccount Class

A `BankAcoount` class is created to practice encapsulation with a private balance.

Features include:

* Private `__money` attribute
* `get_balance()` method
* `deposit()` method
* `withdraw()` method
* Deposit validation
* Withdrawal validation

The program demonstrates how the account balance can be changed through methods instead of directly accessing the private attribute.

### 4. Employee Class

An `Employee` class is used to practice private salary data.

Features include:

* Employee name
* Private `__salary` attribute
* `get_salary()` method
* `set_salary()` method
* Creating multiple employee objects
* Updating employee salaries

### 5. Using `@property`

The project also includes an example of Python's `@property` decorator.

Concepts practiced:

* `@property`
* Property getter
* Property setter
* Private attributes
* Validating values through a setter

### 6. Class Variables

The project demonstrates the difference between **class variables** and **instance variables**.

Concepts practiced:

* Creating class variables
* Accessing class variables
* Instance variables
* Shared data between objects
* Using `ClassName.variable`

### 7. Student Class – Class Variable

A `Students` class is created with:

* Class variable: `school`
* Instance variable: `name`
* Instance variable: `age`
* Creating multiple student objects

Example:

```python
class Students:
    school = "ABC school"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### 8. Car Class

A `Car` class is created to practice class and instance variables.

Features include:

* Class variable `wheels`
* Instance variable `brand`
* Instance variable `model`
* Creating multiple car objects

Example:

```python
class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

### 9. Employee Company

An `Employee` class is created to practice a shared company value.

Features include:

* Class variable `company`
* Instance variable `name`
* Instance variable `salary`
* Creating multiple employee objects
* Accessing shared company information

### 10. Object Counter

The project demonstrates how a class variable can be used to count the number of objects created.

Example:

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
```

Each time a `Student` object is created, the `count` class variable is increased.

## Practice Exercises

The project includes exercises based on:

* Encapsulation
* Private attributes
* Protected attributes
* Getter methods
* Setter methods
* Data validation
* `@property`
* Class variables
* Instance variables
* Multiple objects
* Object counting

## Key OOP Concepts Practiced

* Classes
* Objects
* Instance variables
* Class variables
* Encapsulation
* Private attributes
* Protected attributes
* Getters
* Setters
* `@property`
* Data validation
* Shared class data
* Object counters
* Multiple instances
* `self`
* `ClassName.variable`

## Class Variable vs Instance Variable

| Class Variable           | Instance Variable                                |
| ------------------------ | ------------------------------------------------ |
| Belongs to the class     | Belongs to an individual object                  |
| Shared between objects   | Can be different for every object                |
| Defined inside the class | Usually defined using `self` inside `__init__()` |
| Example: `Student.count` | Example: `self.name`                             |
| Example: `Car.wheels`    | Example: `self.model`                            |

## File Structure

```text
Day-09/
│
├── README.md
└── main.py
```

## How to Run

Make sure Python is installed on your system.

Run the program using:

```bash
python main.py
```

## Learning Goal

The goal of this practice is to strengthen my understanding of Python OOP by practicing **Encapsulation, private and protected attributes, getters, setters, `@property`, class variables, instance variables, and object counters** through small practical programs.

# Day-09 Completed ✅