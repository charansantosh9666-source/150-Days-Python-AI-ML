# 🐍 Day 3 – Python AIML Learning

📚 Topics Covered

Today I continued my Python learning journey for AI/ML and focused on writing reusable, organized, and efficient Python code.

1. Functions
Creating and calling functions
Parameters and arguments
Multiple parameters
Default parameters
Returning values using return
Difference between print() and return
2. Scope
Local variables
Global variables
Understanding variable accessibility
Using the global keyword
3. Modules
What are Python modules?
Importing built-in modules
import
from ... import
Using aliases with as
Creating and importing custom modules
4. List Comprehensions
Creating lists using comprehensions
Applying conditions with if
Using if-else
Filtering data efficiently

Example:

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

Output:

[2, 4, 6]
5. Strings
String indexing
Negative indexing
String slicing
upper() and lower()
strip()
replace()
split()
join()
startswith() and endswith()
count()
Checking values using in
Finding string length using len()
💻 Coding Practice
🧮 1. Calculator Using Functions

Created calculator operations using separate functions for:

Addition
Subtraction
Multiplication
Division

The goal was to practice functions, parameters, and return values.

🌡️ 2. Temperature Converter

Created a temperature conversion program to practice:

Functions
Parameters
Mathematical operations
Return values

Conversions include:

Celsius → Fahrenheit
Fahrenheit → Celsius
🧰 3. Utility Module

Created a custom Python utility module containing reusable functions.

Practiced:

import utility

and using functions from another Python file.

🔢 4. Even / Odd Number Filter

Used list comprehensions to filter numbers into:

Even numbers
Odd numbers

Example:

even = [x for x in numbers if x % 2 == 0]

odd = [x for x in numbers if x % 2 != 0]
📝 5. Text Analyzer

Created a text analysis program to practice string operations.

The analyzer works with:

Character counting
Word counting
Vowel counting
Consonant counting
String processing
🧠 Key Learnings

Today I learned that functions make code:

♻️ Reusable
🧹 Cleaner
🧩 Modular
🐛 Easier to debug

I also learned how Python modules help organize larger programs and how list comprehensions can make simple data-processing tasks more concise.

📂 Day 3 Structure
Day-3/
│
├── calculator.py
├── main.py
├── temperature_converter.py
├── utility.py
├── even_odd.py
├── text_analyzer.py
└── README.md


Python Fundamentals → Functions → Modules → Data Processing → AI/ML

Day 3 completed ✅