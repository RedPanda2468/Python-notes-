 '''


print("Hello world")
print (5)
print("5")
print (17 * 15)
print ("I am a good boy\nand i eat apple everyday")
#Hey i am a good boy
"""
# used triple quoting twice to run latest code 

hey i am a good boy
and i eat apple everyday
 

"""



print("Hey i am a \"good boy\"\nand this viewer is also a good boy")
#OR
# print ('Hey i am "Good boy"\nand this viewer is also a good boy')
print("Hey",6,7,sep="and")
a= "Hey i eat apple everyday"
print(a)
'''
'''
apple = 9
#b = "apple"
#print(b)
'''
#Exercise 1 creating basic calculator
'''
a= int(input("Enter the first value:"))
b= int(input("Enter the second value:"))
print('The value of', a ,"+",b, "is:",a+b)
print("The value of",a,"-",b, "is:", a-b)
print ("The value of", a,"*",b, "is:",a*b)
print ("The value of",a,"/",b, "is :",a/b)
print ("The value of", a,"//",b, "is:", a//b)
print ("The value of",a,"%",b, "is:", a%b)
'''

# a= 3
# b= 6
# print(a+b)
# print(int(a)+int(b))
# a= input("Enter your name:")
# print("Hi",a,"welcome to the website")
# x= input("Enter your first number:")
# y= input("Enter your second number:")
# print(int(x)+ int(y))
#indexing
'''
name= "Apple"
print (name[0])
print(name[1])
print (name[2])
print(name[4])
'''
#Looping
'''
name= "apple"
for character in name:
  print(character)
  
p= "i am a good boy"
for character in p:
  print(character)
'''
'''
names= "Rohan,Shubham"
print(names[0:8])

print(len(names))
fruit= "mango"
print(fruit[0:-3])
'''

#String methods
'''
a="apple"
print(a.upper())
print(a.lower())
b= "thanK yOu foR visiting this wEbsIte"
print(b.capitalize())

d= "apple"
print(d.replace("apple","mango"))
print(d)

print(b.replace("visiting","No"))
print(b.replace("thanK yOu foR visiting this wEbsIte", "Thank you for visiting this website"))
print(b.find("foR"))
print(b. find("ishh"))
print(b.find("is"))
'''

#Conditional operator
'''
a=int(input("Enter your age:"))
print("Your age is:",a)
print(a>18)
print(a<18)
print (a>=18)
print (a>=18)
print (a==18)
print (a!=18)
'''

#If else conditionals
'''
a= int(input("enter your age:"))
print("Your age is:",a)
if (70>=a>=18):
    print("You can drive")
    print("Yes")

else:
  print("You cannot drive")
  print("No")
'''

#If elif else conditionals
'''
num=int(input("Enter the value of num:"))
if (num<0):
  print("Number is negative")
elif (num==0):
  print("Number is zero")
elif (num==999):
  print("Number is special")
'''

#Time pass game
'''
print("which one of these would you choose?")
  
a = "1:short haircut"
b = "2:girl with bottle" 
c = "3:Rashmi"  
d = "4:Mrunal"
print(a)
print(b)
print(c)
print(d)

ans= int(input("so which one of these would you choose:"))
if (ans==1, ans==2, ans==3, ans==4):
   print("oops!!! you are too fat", ans, "rejects you")

'''

#Indentation under condition
'''
num = int(input("Enter any number:"))
if (num<0):
   print("Number is negative")
elif (num>0):
  if (num<=10):
   print("Number is between 1-10")
  elif (num>10 and num<=20):
         print("number is between 11-20")
  else:
   print("Number is greater than 20")
else:
   print("Number is zero")
'''

#time module
'''
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime ('%H')
print(timestamp)
timestamp= time.strftime('%M')
print(timestamp)
timestamp= time.strftime('%S')
print(timestamp).
'''
#exercise Good morning sir
'''
import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
if (timestamp<'12:00:00'):
  print("Good morning sir")
elif ('18:00:00'>timestamp>='13:00:00'):
  print("Good evening sir")
else:
  print("Good night sir")
 '''

#Match case statement
'''
x= int(input("enter the value of x:"))
match x:
     case 0:
        print("x is zero")

     case 4:
        print("case is 4")

     case _ if x!=90:
          print(x,"is not 90")
     case _ if x!=80: 
          print(x, "is not 80")
     case _
  
   '''
#Looping
'''
name = "Apple"
for i in name:
    print(i)

for i in name:
    print(i,end= ",")

for i in name:
  print(i)
if (i=="e"):
      print("This is something special")
  

colours=["red", "green", "blue", "yellow"]
for i in colours:
   print(i)
   for v in i:
      print(v)

for k in range(5):
   print(k)

for t in range(1,200):
   print(t)
   '''

#while loop
'''
i=0 
while(i<7):
      
  print(i)
  i=i+1

count=5
while (count>0):
  print(count)
  count= count-1
b= 3
while(b>0):
  print(b)
  b=b-1
  '''
'''
i= int(input("enter your age:"))
while (i<32):
  i=int(input("enter your age"))
  print(i)
print("done with the loop")
'''
#Else with while loop
'''
count = 5
while(count>0):
  print(count)
  count=count-1
else:
  print("I am inside else")
  '''

#Break/continue statement
'''
for i in range(12):
  if (i == 11):
   break

  print("5X", i + 1, "=", 5 * (i + 1))

for i in range(12):
  if (i == 10):
    print("skip the iteration")
    continue
  print("5X", i, "=", 5 * i)
'''

#Functions in python
'''
a=9
b=8
gmean1= (a*b)/(a+b)
print(gmean1)

c=6
d=7
gmean2= (c*d)/(c+d)
print(gmean2) 
'''
#OR Using function
'''

def calculategmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)
a= 9
b= 8
calculategmean(a,b)

c=6
d=7
calculategmean(c,d)
'''
'''
a=6
b=8

if (a>b):
  print("a is greater than b")
else:
  print("b is greater than a")

#OR
def compare(a,b):
  if (a>b):
    print("First number is greater")
  else:
    print("second number is greater")

a=9
b=7
compare(a,b)

c=6
d=8
compare(c,d)

#Function arguments 
def average(a,b):
  print("The average is", a+b/2)

average(5,6)
'''

#Introduction to lists
'''
marks= [3,5,6, "apple", True]
print(marks)
print(type(marks))
print(type(marks[0]))
print(type(marks[1]))
print(type(marks[2]))
print(type(marks[3]))

mango= [3,5,6,"apple",True,6,7,2 ,32,345]

print(mango)
print(mango[1:8])
print(mango[1:8:2])
print(mango[:])
'''

#List comprehension
'''
a= [i*i for i in range(10)]
print(a)
b= [i*i for i in range(10) if i%2==0]
print (b)
'''

#List methods
'''
l= [11,45,1,2,4,6,1,1]
print(l)

l.insert(1,899)
print (l)

m=[900,1000,1100]
l.extend(m)
print(l)
'''

#Adding of list
'''
l= [2,3,4,"mango", True, False,]
m= [4,5,6,7]
k= l+m
print(k)
l[0]=81
print(l)
'''
#Tuples
'''
a= (2,3,4,4,7,8,3,5,3)
#a[0]=1, tuples are not iterable
print(a)

print(type(a),a)
print(len(a))
print(a[0])
print(a[-1])
b= a[1:4]
print(b)
'''
#operations in tuple
'''
tuple= (3,5,3,6,3,8,9)
res= tuple.index(5)
print("Count of 5 in tuple is:", res)

c= tuple.index(8)
print("Count of 8 in the tuple is",c)

tuple1= (0,1,2,3,2,3,2,3,2,3)
res = tuple1.index(3,4,8)
print("Count of 3 between number 4 and 8 is",res)
'''
#Exercise Make KBC game
'''

a= ["1. India is a federal union comprising twenty-eight states and how many union territories?"]
a1= "1).6"
a2="2).7"
a3 = "3).8"
a4 = "4).9"
print(a)
print(a1)
print(a2)
print(a3)
print(a4)
ans= int(input("enter your answer or press 0 to quit:"))
if (ans==0):
  print("your take home money is 0")
  break
if (ans==3):
  print("Answer is correct\nYou won 5000/- rupees")
  b= ["2. Which of the following is the capital of Arunachal Pradesh?"]
  b1="1)itnagar"
  b2= "2)Dispur"
  b3= "3)imphal"
  b4= "4) panaji"
  print(b)
  print(b1)
  print(b2)
  print(b3)
  print(b4)
  ans=int(input("Enter the correct answer or press 0 to quit:"))
if (ans==0):
  print("Your take home money is 0")
  break
  if (ans==1):
    print("answer is correct\nyou won 10000/- rupees")
    c="[3) Which of the following is the capital of Arunachal Pradesh?"]
    c1= "Odia and Telugu"
    c2= "Telugu and Urdu"
    c3= "Telugu and Kannada"
    c4="All of the above languages"
    print(c)
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    ans=int(input("enter the correct answer or press 0 to quit:"))
    if (ans==0):
      print("your take home money is zero")
      break
    if (ans==4):
      print("Answer is correct\nand you won 100000/-")
      d= ["Q4. Which river among the following starts its Journey and ends its journey in India itself?"]
      d1="1)Indus"
      d2="2)Brahmaputra"
      d3="3)Chambal"
      d4="4)Kosi"
      print(d)
      print(d1)
      print(d2)
      print(d3)
      print(d4)
      ans= int(input("enter the correct answer or press 0 to quit:"))
    if (ans==0):
      print("your take home money is zero")
          break
      if (ans==3):
         print("Answer is correct\nyou won 500000/-")
      else:
         print("incorrect answer\nyou won 100000/-")
    else:
      print("incorrect answer\nyou won 10000/-")
  else:
    print("incorrect answer\nyou won 1000")
else:
  print("Incorrect answer\nyou lost")

'''

#String formatting
'''
letter= "Hey my name is {}, and i'm from {}"
name= "Yash"
country= "India"
print (letter.format(name,country))
#Using curly braces
print(f"Hey my name is {name}, and i'm from {country}")
    #To retain curly brackets use double sign
print(f"hey my name is {{name}}, and i'm from {{country}}")

price= 49.0999
txt=f"for only {price:.2f} dollars!"
print(txt)
'''

#Recursion in python
'''
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
n= int(input("Enter the value to calculate factorial:"))
print(factorial(n))
'''

#Sets in python
'''
s= {2,4,6,8,2,8}
print (s)

info={"carla",19,False, 5.9,19}
print(info)
'''
#For empty set
'''
apple= set()
print(apple)

s1= {3,4,6,7,8}
s2= {3,6,9,9}
print(s1.union(s2))
print(s1.update(s2))

print(s1)
s1.add(5)
print(s1)


a={"Tokyo", "madrid","Berlin","delhi"}
b= {"Tokyo","Seoul", "kabul","madrid"}
cities= a.union(b)
print(cities)

a={"Tokyo", "madrid","Berlin","delhi"}
b= {"Tokyo","Seoul", "kabul","madrid"}
cities= a.intersection(b)
print(cities)

a.intersection_update(b)
print(a)
'''

#Dictionaries
'''
dic= {
  12: "apple",
  13: "Mango",
  14: "cities",
  344: "tokyo",
}
print(dic[14])
print(dic[344])



info= {'name': 'karan', 'age':22, 'eligible':True}
print(info['name']) 
print(info['age'])
print(info['eligible']) 

for key in info.keys():
  print(info[key])

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")


ep1= {122:45, 123:89,567:69,670:69}
ep2= {222:67, 566:90}
ep1.update(ep2)
print(ep1)



ep1.pop(122)
print(ep1)

ep1.clear()
print(ep1)
'''

#For loop with else
'''
for i in range(5):
  print(i)
else:
  print("sorry no i")


for a in []:
  print(a)
else:
  print("sorry no i")

for i in range(6):
  print(i)
  if i==7:
   break
else:
  print("sorry no i") 
  '''

#While Loop
'''

i=0
while (i<11):
  print(i)
  i=i+1
else:
  print("sorry no i")

for x in range(5):
  print("iteration no. {} in for loop".format(x+1))
else:
  print("block in loop")

print("Out of loop")
'''

#Exception handling
'''
a= int(input("enter the number:"))
print(f"Multiplication table of {int(a)} is:")
try:
  for i in range(1,11):
    print(f"{int(a)} X {i}= {int(a)*i}")
except:
  print("Invalid input")

print("some imp.lines of code")
print("end of program")



try:
  num=int(input("Enter an integer:"))
  a= range(10000000)
  print(a[num])
except ValueError:
  print("Number entered is not integer")
except IndexError:
  print("index error")

  '''

#Finally clause
'''
try:
  l= [1,2,3,4,5,6,7,8]
  a= int(input("Enter the index:"))
  print(l[a])
except:
  print("Some error occured")
finally:
  print("I am always executed")
'''

# There's difference in finally, when we use def function.

'''
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input('enter the numberL:'))
    print(l[i])
    return 1

  except:
    print("Some error occured")
    return 0

  print("I am always executed")

x= func1()
print(x)
'''
#OR
'''
def func2():
  try:
    l=[1,5,6,7]
    i=int(input("Enter the number:"))
    print(l[i])
    return 1

  except:
    print("Some error occured")
    return 0
  finally:
    print("I am always executed")

a= func2()
print(a)
'''


#Raising custom error
'''
a= int(input("enter any number between 5 and 9:"))

if (a<5 or a>9):
  raise ValueError("Number should be between 5 and 9")
else:
  print("You are eligible for membership")

'''

#Exercise
'''
a= input("enter any number:")
if (a=="quit"):
  print("you are out!")
else:
  try:
    number= int(a)
    print(a)
  except:
    raise ValueError("Input value is not integer")
    '''


#In KBC to get options in 2 rows
'''

print("Which of the following is the capital of arunchal pradesh?")
question= ("itanagar", "dispur","imphal","panaji")
print(f"a.{question[0]}             b.{question[1]}")
print(f"c.{question[2]}               d.{question[3]}")

'''

#Short hand if else statement
'''
a= int(input("enter any integer:"))
b= int(input("enter any integer:"))
print("A") if (a>b) else print("=") if (a==b) else print("B")

c=9 if a>b else 0
print(c)
'''

#Enumerate function
'''

marks= [12,56,32,98,12,45,1,4]
index= 0
for mark in marks:
  print(mark)

  if (index==3):
     print("you are awesome")
  index=index+1
  '''


  #OR 
'''
for index, mark in enumerate(marks):
  print(mark)
  if (index==3):
    print("you are awesome")

for index, mark in enumerate(marks,start=1):
   print(mark)
   if (index==3):
    print("awesome!")
    '''
    




#How import works
'''
import math
a= math.sqrt(9)*math.pi
print(a)  
'''

 #Or by using keyword
'''
from math import sqrt,pi
c= sqrt(9)*pi
print (c)

from math import pi, sqrt as s
c= s(9)*pi
print(c)

import math as m
b= m.sqrt(9)*m.pi
print(b)


import math
print(dir(math))
'''


#If __name__=="__main__" in python 

'''
import apple
apple.welcome()
'''
#INCOMPLETE

#OS MODULE (INCOMPLETE ) Pg no.14 in notes


#Local v/s Global variable 
'''
x=10
def function():
  y=5
  print(y)
function()
print(x)
print(y)     #error since y is local variable, while x is global 
'''
'''
x=10
def function():
  global y
  y=5
  print(y)
function()
print(x)
print(y)
'''

#File IO
#made myfile.txt containing 'you are awesome'
'''
f= open('myfile.txt','r') #Reading
text=f.read()
print(text)
f.close()
'''
'''
f=open('myfile02.txt','w') #Writing
text= f.write("Hello world!")
f.close()
'''
'''
f= open('myfile02.txt', 'a')
text= f.write("Hii")
f.close()
'''

#Read,readline(), & Other methods
       #Made myfile3.txt written

             #Python course is great
             #and this tutorial is also awesome
             #this is also good


'''
f= open('myfile3.txt','r')
while True:
  text=f.readline()
  if not text:
    break
  print(text)
  '''

'''
f=open('myfile4.txt','r')
i=0
while True:
  i=i+1
  line=f.readline()
  if not line:
    break
  m1=line.split(",") [0]
  m2=line.split(",") [1]
  m3=line.split(",") [2]
  print(f"marks of student{i} in maths is: {m1}")
  print(f"marks of student {i} in english is: {m2}")
  print(f"marks of student {i} in SST is: {m3}")

print(line)


f= open('myfileX.txt','w')
lines= ('line1\n', 'line2\n','line3\n')
f.writelines(lines)
f.close()
'''

#Seek, tell and other functions
'''
with open('myfile.txt','r') as f:
  print(type(f))

  f.seek(10)
  data= f.read()
  print(data)
  '''

#Lambda function
'''
def double(x):
  return(x*2)

print(double(5))
       #OR


avg= lambda x,y,z:(x+y+z)/3
double= lambda x: x*2
cube= lambda x: x*x*x

print(double(5))
print(cube(5))
print(avg(3,5,10))
'''



#Passing function into function
'''

def appl(fx,value):
  return 6+fx(value)

print(appl(lambda x:x*x*x,2))
print(appl(lambda x:x*x,2))
'''


#Map, Filter, Reduce 


'''
def cube(x):
  return x*x*x
print(cube(2))
'''
'''
l=[1,2,4,6,4,3]
newl=[]
for item in l:
  newl.append(cube(item))
print(newl)
'''
#OR By using MAP

l=[1,2,4,6,4,3]
'''
newl=list(map(cube,l))
print(newl)
'''



#filter
'''
def filter_function(a):
  return a>2
newnewl= list(filter(filter_function,l))
print(newnewl)
'''

#Reduce
'''
from functools import reduce 
numbers= [1,2,3,4,5]
def mysum(x,y):
  return x+y
sum=reduce(mysum,numbers)
print(sum)
'''


#'is'  v/s  '=='
'''
a=4
b='4'
print(a is b)
print(a==b)

a=[1,2,43]
b=[1,2,43]
print(a is b)
print(a==b)

a=3
b=3
print(a is b)
print(a==b)

a='apple'
b='apple'
print(a is b)
print(a==b)

a=(1,2)
b=(1,2)
print(a is b)
print(a==b)

a=None
b=None
print(a is b)
print(a==b)
'''

#[****OBJECT ORIENTED PROGRAMMING****]

#Classes and objects in python
'''
class person:
  name= 'apple'
  occupation= 'software developer'
  networth= '10'
  

a= person()
a.name= 'mango'
a.occupation= 'accountant'
print(a.name, a.occupation)
'''



#Using self
'''
class person:
  name= 'apple'
  occupation= 'software developer'

  def info(self):
    print(f"{self.name} is a {self.occupation}")

a= person()
b= person()
a.name= 'shubham'
a.occupation= 'accountant'
b.name= 'nitika'
b.occupation= "HR"
a.info()
b.info()
'''

#Constructors in python
'''
class person:
  def __init__(self,n,o):
    print("Hey im a person")
    self.name= n
    self.occupation= o
  def info(self):
      print(f"{self.name} is a {self.occupation}")
      

a= person("Harry","developer")
b= person("Shubham", "Accounant")
a.info()
b.info()
'''
#Decorators in python
'''
def greet(fx):
  def mfx():
    print ("good morning")
    fx()
    print("Thanks for using this functions")
  return mfx

@greet
def hello():
  print("Hello world")

hello()
  '''


#Decorators in python (if theres argument)
'''
def greet(fx):
  def mfx(*args,**kwargs):
    print("good morning")
    fx(*args,**kwargs)
    print("Thanks for using this function")

  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a,b):
  print(a+b)

hello()
add(1,2)
'''
#Getters and setters
'''

class Myclass:
  def __init__(self,value):   
    self._value = value  

  def show(self):
    print(f"value is {self._value}")

  @property
  def value(self):
    return self._value


  @property
  def ten_value(self):
    return 10*self._value
    

  @ten_value.setter
  def ten_value(self,new_value):
    self._value= new_value/10




obj= Myclass(10)
obj.ten_value= 67
print(obj.ten_value)
obj.show()
'''

#Inheritance in python
'''
class Employee: 
  def __init__(self,name,id):
    self.name= name
    self.id= id

  def showdetails(self):
    print(f"The name of employee {self.name} is {self.id}")

class programmer(Employee):
  def showlanguage(self):
    print(f"The default language for {self.id} named {self.name} is python") 


e1= Employee("rohan", 302)
e2= Employee("karan", 156)
e3= programmer("rahul", 328)

e1.showdetails()
e2.showdetails()
e3.showlanguage()
'''

#Access modifier 
'''

class employee():
  def __init__(self):
    self.__name= "apple"

a= employee()
#print (a.__name) cannot be accessed directly
print(a._employee__name) # can be accessed directly.
'''

#SNAKE WATER GUN EXERCISE 
'''
import random

comp= random.randint(0,2)
user= int(input("0 for snake, 1 for water, 2 for gun:\n"))

def check(comp,user):
  if comp==user:
    return 0
    
  if (comp==0 and user==1):
    return -1
    
  if (comp==1 and user==2):
    return -1
    
  if (comp==2 and  user==0):
    return -1
  else:
    return 1

print("You", user)
print("Comp", comp)

score = check(comp,user)

if (score==0):
  print ("Its draw")
  
elif (score ==-1):
  print("You lose")
  
else:
  print("You won")
'''

#Static Method
'''
class math:
  @staticmethod
  def add(a,b):
    return a + b

result= math.add(5,6)
print(result)
'''

#Instance Variable (v/s) Class variable
'''
class employee:
  companyname = "apple"
  noOfEmployee= 0
  def __init__(self,name):
    self.name= name
    self.raise_amount= 0.02
    self.company= "Apple"
    employee.noOfEmployee+=1

  def showdetails(self):
    print(f"The name of employee is {self.name} and the raise amount in {self.company}  is {self.raise_amount}") 

emp1= employee("Shubam")
emp1.raise_amount= 0.8
emp1.companyname=("Apple,India")
emp1.showdetails()
'''

#Clear the clutter exercise left

#Class methods in python
'''

class employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and the company is {self.company}")

  @classmethod
  def changecompany(cls,newcompany):
    cls.company= newcompany

e1=employee()
e1.name= "Mango"
e1.show()
e1.changecompany("Tesla")
e1.show()
print(employee.company) #Due to classmethod decorator whole class got changed
'''

#Class methods as Alternative constructor
'''
class employee:
  def __init__(self,name,salary):
    self.name= name
    self.salary= salary

string="John-12000"
e1= employee(string.split("-")[0],string.split("-")[1])
print(e1.name)
print(e1.salary)
           #But you aint gonna do it for every object , do you?

class employee:
  def __init__(self,name,salary):
    self.name= name
    self.salary= salary

  @classmethod
  def fromstr(cls,string):
    return cls(string.split("-")[0],string.split("-")[1])

string= "John-12000"
e1= employee.fromstr(string)
print(e1.name)
print(e1.salary)
'''

#dir, __dict, help method

#dir
'''
x= [1,2,3]
print(dir(x))
print(x.__add__)
'''
#__dict__
'''
class person:
  def __init__(self,name,age):
    self.name= name
    self.age= age

p= person("John",22)
print(p.__dict__)
#help
print(help(person))
'''

#Superkeyword in python
'''
class parentclass:
  def parent_method(self):
    print("This is parenet class")

class childclass(parentclass):
  def child_method(self):
    print("This is child method") 
    super().parent_method()

child_object= childclass()
child_object.child_method() 
'''

#Method overiding
#Emerge the PDF exercise

#Function caching
'''
import functools
@functools.lru_cache(maxsize=None)
def fib(n):
  if n < 2:
    return n
  return fib(n-1)+fib(n-2)
print(fib(1))
'''


  


    
    

  




  


  









 



  
  


  










    
 

  

      
    
    






  









  











































  



  











  
  