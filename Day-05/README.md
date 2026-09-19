# 🐍 Python Learning Journey — Day 5

## 📚 Day 5: Slicing, Tuples & Conditional Statements

Today I practiced **list slicing, copying lists, tuples, conditional statements, user input, and decision-making in Python**.

### 📝 Topics Covered

* List slicing
* Reversing a list using slicing
* Looping through a slice
* Copying lists
* Creating and using tuples
* Modifying tuples by reassigning them
* `for` loops
* `if`, `elif`, and `else`
* Taking input from users with `input()`
* Converting input using `int()`
* Nested conditional statements
* f-strings
* List comprehensions

### 💻 Practice Exercises

Some of the programs I practiced today:

* Reversing a list using slicing
* Printing the first three items from a list
* Printing the middle three items
* Printing the last three items
* Copying a list
* Working with a restaurant food menu using tuples
* Changing a tuple by assigning a new tuple
* Alien color game
* Determining stages of life based on age
* Admin login greeting
* Printing ordinal numbers (`1st`, `2nd`, `3rd`, etc.)
* Electricity bill calculator based on units

### 🔥 Example — List Slicing

```python
players = ["charles", "martina", "florence", "eli"]

print(players[::-1])
print(players[:3])
print(players[-3:])
```

### 🔥 Example — Conditional Statements

```python
if user == "green":
    print("The player earned 5 points")
elif user == "yellow":
    print("You just earned 10 points")
elif user == "red":
    print("You just earned 15 points")
else:
    print("Your choice is wrong")
```

### ⚡ Mini Project — Electricity Bill Calculator

I also created a simple electricity bill calculator using conditional statements.

The calculation is based on the number of units:

| Units     |    Rate |
| --------- | ------: |
| 0–100     | ₹2/unit |
| 101–200   | ₹3/unit |
| 201–500   | ₹5/unit |
| Above 500 | ₹8/unit |

### 🧠 What I Learned

Today I learned how to extract specific parts of a list using **slicing**, work with **tuples**, and use conditional statements to make programs respond differently depending on the user's input.

I also practiced applying these concepts to small real-world problems like an **electricity bill calculator**.

### 📂 Files

```text
Day-5/
└── main.py
```

### 📈 Progress

**Day 5 ✅**

Learning Python one day at a time and building my programming fundamentals! 🐍💻
