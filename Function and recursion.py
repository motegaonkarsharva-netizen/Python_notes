#Function defination
#insted to repeting the code for the same task again and again we put it in a function and then call the function
#it reduces redendency
a=1
b=2
sum=(a+b)
print(sum)

# if we have to repete this code again n again
def calc_sum(a,b):    #parameters
    return a + b
sum = calc_sum(1,2)  #function call
print(sum)
sum = calc_sum(2,3)  #function call
print(sum)
sum = calc_sum(3,4)  #function call
print(sum)
sum = calc_sum(4,5)  #function call
print(sum)
sum = calc_sum(5,6)  #function call
print(sum)
sum = calc_sum(6,7)  #function call
print(sum)

#parat parat tech typ ekrat basaichi garaj nhi
#when there is no return then output gives out to be none
def print_hello():
    print("hello")

output = print_hello()
print(output)  # None

#to calc average
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return(avg)


print(calc_avg(4,5,6))

#built in function

#to combine 2 les in print
print("apnacollege", end=" ")   # sep = " "
print("shradhakhapra")          # end = "\n"

#print()
#len()
#type()
#range()

#are both built in function

# assigning a default value to parameters

def calc_prod (a,b):

    return(a*b)

print(calc_prod(a=2,b=4))

#def calc_prod (a,b):

    #return(a*b)

#calc_prod()    #it will come as error if we don't


#now let's assign default value
def calc_prod (a,b=2):

    return(a*b)

print(calc_prod(1))    #a ke andar 1 store ho jainga



#def calc_prod (a=2,b):        # this code won't run cause pahile non default aane chaiyee(a) aur last me default argument ana chaiyee(b)

   # return(a*b)

#calc_prod(1)



"""moral of the story:- default argument hamesha last se assign krna chaiyee"""


#Write a function to print the length of a list
#we also did an experiment here


cities = ["Mumbai", "pune","banglore","Hydrabad","delhi"]
print(cities[0], end=" ")
def print_len(list):   #here list is a parameter
    print(len(list))
print_len(cities)


#write a function to find factorial
def calc_fact(n):

    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(6)


#WAF to convert USD to INR
def doltoinr(USD):
    num = USD*95
    return USD*95
    print(num)
doltoinr(4)


#Recursion
#AKA loops ka aur bhi khatarnak version
#when function calls itself repetedly
"""all work done by loop can be done by recursion and vice versa"""
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("end")
show(5)
print("for reverse ")

def show(n):
    if n == 6:
        return
    print(n)
    show(n+1)

show(1)

#CAll stack
# Recursion layers (call stack)

#show(3)   # layer 1
#show(2)   # layer 2
#show(1)   # layer 3
#show(0)   # base case (stop)

#then it just starts going backwards to see if any work is remaining if not it prints nothing to prove this lets just add print("end") in recusion
# as we can see it printed "end" 5 times pro



#to find factorial
def fact(n):
    if n == 1 or n == 0:
        return 1

    return fact(n - 1) * n
fact(5)

#to calculate sum of n natural numbers
def calc_sum(n):
    if n==0:
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(5)
print(sum)


