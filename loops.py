#loops are used to repeat instructions
count = 1             #count variable is known as iterator
while count <=5 :     #while nantar condition asti
    print("hello")
    count=count+1    # or count+=1



#to print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i+=1
print("loop ended")

#for 5 to 1

i=5
while i >=1:
    print(i)
    i-=1
print("loop ended")

# practice
#WAP to print multiplication table of n
i=1
n=int(input("enter the number: "))
while i<=10:
    print(i*n)
    i+=1    # haa part i madhe 1 add krat jato
print("loop ended")


#WAP to print 1 4 9 ,etc
i=1
n=int(input("enter the number: "))
while i<=10:
    print(i*i)
    i+=1
print("loop ended")

#WAP to find the index of value of x in a tupple

num = (1,4,9,16,25,36,49,64,81,100,36)

x = 36

i=0
while i < len(num):
     if (num[i] == x):
         print("found at index:",i)
     else:
         print("not found")
     i+= 1

     #break
i = 1
while i <= 5:
    print(i)
    if i == 3:
        print("found at:", i)
        break          # if we don't do this it will continue till 5
    i += 1


#continue button
#continue mhange basically adhi chi process restart hoti ani pudhchi process skip hoti if that perticular condition is true
i = 0

while i <= 5:
    if i == 3:
        i += 1
        continue   # here continue act's as skip button for i=3

    print(i)
    i += 1




i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue   # skip even numbers

    print(i)
    i += 1

