"""Multiline comment can be written like this""" #use then when u have to write multiple lines
X=1
print(X)

#Input- they ask you in output to put in the data
name=input("name : ")
age=int(input("age : "))  #int
price=float(input("price : "))   #float

print("my name is ", name, "and my age is ",age, "i put price of my dihh as", price ) #ithun actual code suru hot aahe please take this seriously

"""Types of Operators
• Arithmetic Operators

+ , - , * , / , // , % , **

• Relational / Comparison Operators

== , != , > , < , >= , <=

• Assignment Operators            (next cell shows how this works)

= , += , -= , *= , /= , %= , //= , **=

• Logical Operators

not , and , or

• Membership Operators

in , not in

• Identity Operators

is , is not

• Bitwise Operators
& , | , ^
(AND, OR, XOR)"""

num = 10
num = num +10  #is the same as assignment operator num+=10
print(num)

xyz=20
xyz+=20
print(xyz)

#logical operators
print(not False)
a=50
b=70
print(not a>b)
val1= True
val2= False
print("AND operator:",val1 and val2)
print("OR operator:",val1 or val2)
print("OR operator:",a==b or a<b )

#Operator precedence
"""
1.  ()                → Parentheses (pehle solve hota hai)
2.  **                → Power (exponent)
3.  +x, -x, ~x        → Unary (sign change / bitwise NOT)        (~x = -(x + 1))
4.  *, /, //, %       → Multiply / Divide / Floor / Mod
5.  +, -              → Add / Subtract
6.  <<, >>            → Bitwise Shift (left/right)     (x << n = x × (2^n)) and (x >> n = floor(x ÷ (2^n))
7.  &                 → Bitwise AND          (multiply binary versions of numbers)
8.  ^                 → Bitwise XOR          (uk the difference btw or and xor right?)
9.  |                 → Bitwise OR           (add binary versions of numbers)
10. ==, !=, >, <, >=, <=  → Comparison (True/False)   (!=asks weather lhs and rhs are different)
11. not               → Logical NOT (reverse)          (not True → False ,not (5 > 3) → False   # because (5 > 3) is True)
12. and               → Logical AND (both true)        (True and True → True ,True and False → False ,(5 > 3) and (2 < 4) → True)
13. or                → Logical OR (any one true)"""

#python ke rules ko syntax kehete hai
import sys

#if-elif-else

"""
if(condition1)
    statement1
elif(condition2)
    statement2
    .
    .
    .
elif(conditionN)
    statementN"""
light = input("colour : ")
if (light=="red"):
    print("stop")
elif (light=="yellow"):    # : wisru nokos
    print("ready")
elif (light=="green"):
    print("go")
else:
    print("wrong colour")




marks = int(input("marks : "))           #ithe int basically marks la integer madhe convert krta and it's imp cause >= eaka string ani integer madhe nhi lagu shakat
if (marks >= 90):                        # uk or kasa kam krta
    print("A")
elif (marks >= 80 and marks <90):
    print("B")
elif (marks >= 70 and marks<80):
    print("C")
elif (marks >= 60 and marks<70):
    print("D")
else:
    print("F")

#nesting
int(input("age of the person is :", ))
if(age >= 18):
    if(age>=80):
        print("cannot drive")        #adhi atli condition barobar hoti ka baghtatpn print lagech krat nhi tya nantar baher chi condition baghtat
    else:
        print("can drive")
else:
    print("can drive")





# WAP to find if a number is odd or even
num = int(input("enter a number: " , ))
rem = num%2
if(rem==0):
    print("number is even")
else:
    print("number is odd")


#WAP to find the greatest of 3 numbers given input of
num1 = int(input("enter 1st number: " , ))
num2 = int(input("enter 2nd number: " , ))
num3 = int(input("enter 3rd number: " , ))

if(num1>num2):
    if(num1>num3):
        print("num1 is greatest", num1)
    else:                                             #if both the if are false then this else will be used
        print("num3 is greatest",num3)

elif(num2>num3):
    print("num2 is greatest",num2)
else:
    print("num3 is greatest",num3)




        #OR
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest", c)


#WAP to check if a number is a multiple of 7
num = int(input("enter a number: " , ))
rem = num%7
if(rem==0):
    print("number is miltiple of 7")
else:
    print("number is not multiple of 7")


#there are more types to run if else statements
#<var>=<val1>if<condition>else<val2>
food = input("food : ")   #-> hee line tar lagel atch
eat = "yes" if food=="cake" else "no"
print("eat")



#<stt1>if<condition>else<stt2>           basically apan variable la value assign krnaya aaiwaji direct print kela
food = input("food :")
print("yes") if food =="cake" or food =="sweet" else print("no")


#<var>=(false_val,true_val) [<condition>]

age = int(input("age :"))
vote = ("yes","no") [age<=18]
print(vote)



#to find tax 10% for 0 to 50k and 20%for 50k+
sal = float(input("sal :"))
tax = sal*(0.1,0.2) [sal>=50000]
print(tax)

"""BEST PRACTICES
~simple instruction
~one instruction per task
~short& meanfull variable names
~use appropriate comments
~avoid comeplex expression
~code single line madhe lihina avoid kr"""


#simple instrest (SI)= P*R*T/100
#P= principle, R= rate ,T= time


#type conversion
a=2
b=4.2
sum=a+b #6.2
c=sum-b
print(c)

#if a= "2"(ie if we convered to string )error would have come

#type casting(basically type conversion but with special function)
a=3
b=5.6
c=int(b)
print(a+c)   #3+5=8

a,b=1,"2"    #possible only with number not with
c=float(b)
print(a+c)

#how to take input
name=input("whats you name: ")
print("welcome :",name)

name1=input("enter your name: ")
age=input("enter your age: ")
marks=float(input("enter your marks: "))

print(name1,"is",age,"years old",marks,"scored")



#type casting cha continuatation

val=input("enter your value : ")  # 34 now becoms a string/ float whatever we want for float just add float ()before input
print(type(val),val)

#practice
#1)write a program to input 2 numbers and add them

num1=int(input("enter value of 1st variable:" ))
num2=int(input("enter value od 2nd variable:" ))

c= num1+num2
print(c)

#or u can do
print("sum=", num1+num2)


#2)write a program to input side of a square& print it's area

side= int(input("the side of the square Is: "))
print("area = ", side**2)


#3) write a program to input 2 floating point numbers and write their average

a=float(input("first: "))
b=float(input("second: "))

print("average is" , (a+b)/2)


#4) write a program to input 2 int numbers a and b ptint true if a is greater or equal to b if not print false

a=int(input("first is: "))
b=int(input("second is: "))

print("true" if a>=b else "false")

#but u dont need to do all of this even if u

print(a>=b)