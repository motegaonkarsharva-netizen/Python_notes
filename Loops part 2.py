
#for loops
#A for loop is used when you want to go through a collection of items (like a list, string, set, etc.) one by one.
veggies = ["abc","bcd","cde"]

for veg in veggies:    #here veg is just a variable
    print(veg)

tup = (1,2,3,4,5)     #linear loop basically the one jisme eak eak krke elements ko dekha jata hai

for num in tup:
    print(num)

else:       #else is not compulsary here but in case of break function
    print("end")



str = "apnacollege"

for char in str:
    if char == 'o':
        print("o found")
        break
    print(char)

print("END")


nums = (1,4,9,16,25,36,49,64,81,100,49)
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("the number is found at index:",idx)
        break #break statement will be used when we want only 1st occurence
    idx+=1    #if this statement is inside if statement then output would be incorrect cause it will only work if if statement is true which we dont want in this case


#Range
#range fuctions returns a sequence of numbers starting from dfault,and increments by 1 from default and stops before a specific numbers
#range(start?,stop,step?)             ? shows that it's not complusary
print(range(5))


for el in range(5):         #it dosen't print the last one
    print(el)               #it's easier meathod

seq = range(10)
for i in seq:
    print(i)
    i+=1
print("end")



for i in range(10):  # range(stop)
     print(i)
print("end")
for i in range(2, 10):  # range(start, stop)
     print(i)
print("end")
for i in range(2, 10, 2):  # range(start, stop, step)
    print(i)
print("end")

# for reverse
for i in range(100,0,-1):
    print(i)


#WAP to make a table of number n
n = int(input("enter the number",))
i=0
for i in range(0,10):
    i+=1
    print(n*i)


#pass statement
#pass is a null statement that does nothing it is used as a placeholder for future codes
for el in range(10):
    pass       # if we dont use pass here the code wont work causewe need some task at this place
print("smth ")

#practice
#WAP to find sum of n numbers
num = 5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)


#by while loop
num = 5
sum=0
i=1
while i<=n :
    sum+=i
    i+=1
print(sum)



#WAP a find factorial natural numbers
num=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial is",fact)

#by while loop
num = 5
fact=1
i=1
while i<=n :
    fact*=i
    i+=1
print("factorial is", fact)

