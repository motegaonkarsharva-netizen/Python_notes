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