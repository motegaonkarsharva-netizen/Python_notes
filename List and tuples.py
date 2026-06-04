#List
marks=[23, 34, 56,78]
print(type(marks))
print(marks[0])
print(len(marks))

#python can store elements of different types

#list are mutable while strings are not

student=["sharva" , 97, "abc"]
print(student[0])
student[0]="sharva2"
print(student)


#slicing in list is same as slicing in string also negative indexs work the same

lst = [2, 1, 3]

# adds one element at the end
lst.append(4)
print(lst)  # [2, 1, 3, 4]

# sorts in ascending order
lst.sort()
print(lst)  # [1, 2, 3, 4]

# sorts in descending order
lst.sort(reverse=True)
print(lst)  # [4, 3, 2, 1]

# reverses list
lst.reverse()
print(lst)  # [1, 2, 3, 4]

# insert element at index
lst.insert(1, 99)
print(lst)  # [1, 99, 2, 3, 4]

#removes element at first occurence
lst.remove(2)
print(lst)

# removes element at index
lst.pop(1)
print(lst)


lst = ['a', 'd', 'e', 'b', 'c']

lst.sort()
print(lst)   # ['a', 'b', 'c', 'd', 'e']


#tuple
#similer to string but inmutable just like strings
#it can also be empty
tup = ()
print(tup)
print(type(tup))


tup = (1,)
print(tup)
print(type(tup))

tup = (1,2,3)
print(tup)
print(type(tup))

tup = ("sharva",5,7)
print(tup)
print(type(tup))

tup = (1)
print(tup)
print(type(tup))


tup = (1.0,1.3,1.5)
print(tup)
print(type(tup))


#slicing works the same way as strings and list

#WAP to ask user to input names of their favourate movies and put them in a list

mov1 = input("name of movie1 :", )
mov2 = input("name of movie2 :", )
mov3 = input("name of movie3 :", )

list = [mov1,mov2,mov3]

print(list)




#WAP to check if the list has palindrome of elements


list1=[1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("its a palindrome")
else:
    print("its not a palindrome")


#WAP to count the number of students with A grade in the following tupple

tupp = ( "a","b","c","a","c","b","a")

tupp.count("a")


#WAP to store above values in a list and sort them from A to C

list = [ "a","b","c","a","c","b","a"]

list.sort()
print(list)

