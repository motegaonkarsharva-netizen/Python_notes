# To print 2 lines together
print("abcd", "xyz")
# ata 2nhi 1kach line madhe print hoil

# To define a variable u dont need()
# = sign mhange tu right side chi value left la assign krto we can use ''or ""
x = "sharva"
y = 7 # "" not needed for number

# jar variable chay adhi kahi lihaicha asel tar
x = 7
print("My age is :", x)

# variation la variation pn assign kru shakto ani variable sathi pn "" nhi lagat
# variable dosent have space n special characters and digits at starting are not allowed(1variable cant be a variable but variable1 can)
age = 19
age2 = age
print(age2)

#type comand sangto ki aplaya variable chay assigned value cha type kye aahe
#here int stands for integer,str for string and z for float these are data types
#there are 5 data types
x = 7
y = "abcd"
z= 2.4
print(type(x))
print(type(y))
print(type(z))


# other 2 types are
#boolean remember T and F and N are capital
age = 23
old = False
print(type(old))
#None
a = None
print(type(a))

#Keywords
#these words can't be used as variables(identifiers)
##Keywords
#and as assert break class continue def del elif else except finally False for from global if import in is lambda nonlocal None not or pass raise return True try with while yield

#sum(same with all basic calculations)
a = 2
b = 3
sum = a + b
print(sum)

#Punchuators
#symbols which organise the code
#=-+/ wagera wagera


#tyes of language
#Implicit( does not need to mention type ) eg- python
#explicit eg- java

#Expression exicution
# aplayala code dyu shaktat ani tyacha output nhi tar error vicharu shaktat
#If you can imagine putting it on the right side of = and it makes sense → it’s an expression.
#Concatination- 2 string + sign ni join hotat
#string and numeric values can operate together with *(not with - and/)
#for + u need both to be string we can simply put a number in "4" to continue
A,B=1,3
txt="@"# ithe @ string aahe apan kahi pn taku shakto
print(A*txt*B)

C,D="4",5
txt="@"
print((C+txt)*D)

# when it comes to only integer all operators can be used
A,B=2,3
C=2
print(A*B*C)

A,B=10,5.00
print(A*B)  #if any value is float then the output will come out to be in float

A,B=1.5,3
C=A//B       # // conters shows only whole number (0.9 la pan 0) and -5.2 cha -6 hoil, 5.0 cha 5
print(C,A/B)

#this is a bit weird weird one
#Remainder is negative only when denominator is negative and numerator is positive Btw % is used to find remainder
A,B=-5,2
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C)