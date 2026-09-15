#========= Day-2 ===========
#Exercises
#1.Create a list of integers [5, 10, 15, 20, 25] and print the sum of its elements.

a=[5,10,15,20,25]
sumA=0
for i in a:
    sumA+=i
print(sumA)
print(sum(a))

#2.Given a list ["red", "green", "blue", "yellow"], remove the third item using .pop() and print the list.

color=["red","green","blue","yellow"]
print(color.pop(2))
print(color)

#3.Use slicing to reverse the list [1, 2, 3, 4, 5].

l=[1,2,3,4,5]
print(l[::-1])

#4.Merge two lists, e.g. [1, 3, 5] and [2, 4, 6], sort the result, and print it.

a=[1,3,5]
b=[2,4,6]
a+=b[:]
a.sort()
print(a)

#5.Given numbers = [1, 2, 3, 4, 5], create a new list of their squares using a list comprehension.
a=[1,2,3,4,5]
ans=[]
for i in a:
    ans.append(i*i)
print(ans)

#6.Define a tuple of three strings and print the last element.

tup=("charan","santosh","adhi")
print(tup[-1])

#7.Unpack a tuple t = (100, 200, 300) into three variables and print them.
t=(100,200,300)
x,y,z=t
print(x,y,z)

#8.Demonstrate concatenating two tuples, e.g. (1,2) + (3,4)
a=(1,2)
b=(3,4)
print(a+b)

#9.Create a set from the list [1, 2, 2, 3, 3, 3] and print it (duplicates should vanish).
a=[1,2,2,3,3,3]
print(set(a))

#10.Given sets A={1,2,3} and B={3,4}, compute and print A | B (union) and A & B (intersection).
a={1,2,3}
b={3,4}
print(a | b)
print(a & b)

#11.Use a loop to print all elements of {"apple", "banana", "cherry"}.
se={"apple","banaba","cherry"}
for i in se:
    print(i)

#12.Given a string "abracadabra", use a set to find the unique letters.
se="abracadabra"
print(set(se))

#13.Create a dictionary mapping three country names to their capitals. Print one capital by its country key.
con={"ind":1,"usa":2,"aus":3}
print(con["ind"])

#14.Given d = {"a": 1, "b": 2}, update the value for key "a" to 10 and then print d.
d={"a":1,"b":2}
d["a"]=10
print(d["a"])

#15.Loop over a dictionary {'x':10, 'y':20} and print each key and value.
d={'x':10,'y':20}
for i in d:
    print(f"{i} : {d[i]}")

#16.Check for a key in a dictionary (if key in d:) and safely get a value with .get().
d={"a":1,"b":2,"c":3}
key="c"
if key in d:
    print(d.get(key))

#17.Use a dictionary comprehension to map numbers to their squares for 1–5 (e.g. {x: x*x for x in range(1,6)}).
d={x:x*x for x in range(1,6)}
print(d)

#Coding Tasks 
"""
1. Student Marks Program
Problem Statement: Write a program to store student marks (0–100) for a class, then compute the average and assign a grade. Grade thresholds: 90–100 = A, 80–89 = B, 70–79 = C, 60–69 = D, below 60 = F.

Input/Output Example:
Input: Marks = [88, 76, 90, 69, 95]
Output: "Average = 83.6, Grade = B"
"""
a=[88,76,90,69,95]
ava= sum(a) / len(a)
if ava<=100 and  ava>=90 :
    grade='A'
elif ava<90 and ava>=80:
    grade='B'
elif ava<80 and ava>=70:
    grade='C'
elif ava<70 and ava>=60:
    grade='D'
else:
    grade='F'

print(f"Grade = {grade}")

"""
2. Remove Duplicates from a List
Problem Statement: Given a list of values (e.g. integers or strings), remove all duplicate entries. Do this in two ways: (a) preserving the original order, and (b) not preserving order (using a set).

Input/Output Example:

Input List: [1, 2, 2, 3, 1, 4]
Output (preserve order): [1, 2, 3, 4]
Output (ignore order): any order of {1,2,3,4}, e.g. [1,3,4,2] (since set is unordered)
"""

li=[1,5,2,2,3,1,4]
unq=[]
seen=set()
for i in li:
    if i not in seen:
        unq.append(i)
        seen.add(i)

print(unq)
print(list(set(unq)))

"""
3. Simple Student Database
Problem Statement: Create a simple student database supporting add, search, update, and delete operations. Each student record has a unique ID, a name, and marks. Store this using an appropriate data structure (e.g. a dictionary mapping IDs to records).

Input/Output Example:

Add: { 'id': 1, 'name': 'Alice', 'marks': 85 }
Search: Input ID=1 → Output "Alice has 85 marks."
Update: Change ID=1 marks to 90.
Delete: Remove ID=1 record.
"""
student={}
student[1]={'name':'charan','marks':95}
student[2]={'name':'santosh','marks':99}

sid=2
if sid in student:
    a=student[sid]
    print(f"{a['name']} has {a['marks']}")
else:
    print("Student not found")

student[1]['marks']=90
print(student[1])

del student[2]
print(student)

