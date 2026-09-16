#Day-03 topic pratice and coding

import calculator

print(calculator.add(2,3))
print(calculator.sub(50,10))
print(calculator.mul(3,4))
print(calculator.square(7))

import math
print(math.sqrt(25))
"""
#Create a function called say_hello() that prints:
"""
def say_hello():
    print("Hello python")

say_hello()

"""
Create:

def is_even(number):

It should return:

True

if the number is even and:

False

if the number is odd.
"""
def is_even(num):
    if num%2==0:
        return True
    else:
        return False

print(is_even(33))
"""
Let's combine everything we've learned.

Create a function:

def calculate_bill(price, quantity):

It should:

Multiply price × quantity
Return the total
"""
def total_bill(price,qun):
    price*=qun
    return price
total=total_bill(100,3)
print(f"total bill is equal to {total}")


"""
#give an arr [0,7,0,3,6,0,2] push the zeros to last [7,3,6,2,0,0,0]
a=[0,7,0,3,6,0,2]
n=len(a)
j=0
for i in range(0,n):
    if(a[i]!=0):
        a[j]=a[i]
        j+=1
while j<n:
    a[j]=0
    j+=1
print(a)


#remove the duplicate from the arr [2,5,7,2,3,2,3,5]
a=[2,5,7,2,3,2,3,5]
ans=[]
d=[]
for i in range(0,len(a)):
    if a[i] not in ans:
        ans.append(a[i])
    elif a[i] not in d:
        d.append(a[i])
print(ans)


#count the duplicate in an array
def co(a,arr):
    count=0
    for i in range(0,len(arr)):
        if(arr[i]==a):
            count+=1
    return count
a=[2,5,7,2,3,2,3,5]
do=[]
for i in range(0,len(a)):
    if a[i] not in do:
        do.append(a[i])
        print(f"{a[i]} = {co(a[i],a)}")

"""

#numbers = [2, 4, 6, 8, 10]
# Create a new list containing the half of every number.
# Expected:
# [1.0, 2.0, 3.0, 4.0, 5.0]

numbers=[2,4,6,8,10]
div2=[x/2 for x in numbers]
print(div2)

num=[10,13,15,20,24,25,30,31,35,40]
gra=[x for x in num if x>20]
print(gra)

div5=[x for x in num if x%5==0]
print(div5)

num=[1,2,3,4,5]
num=["Even" if x%2==0 else "Odd" for x in num]
print(num)