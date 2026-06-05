#string is a data type that stores a type of characters

#basic operations
str1="This is a string"
str2="this is another one"

str_final=(str1+" "+str2)   #space also counts
print(str_final)

len(str_final)  # here too space counts
print(len(str_final))

#we can use  "" , ' ' , """ """ for strings too

#\n is used to print following part in next line

str3="This is a string. \nwe are creating it in python"
print(str3)

#\n se tab ka space aaiga
str4="This is how tab string would work. \t it should create tabular space"
print(str4)

#indexing
str1 = ("sharva Santosh Motegaonkar")
print(str1[6])    # space pn count hoti
print(str1[3])
print(str1[2])
#str1[6]=@    # this will not work becouse we cant manipulate


#slicing(-ve index fakt slicing madhe asta)
str=("sharva")
print(str[1:4])
print(str[ :6])    # empty space means 0 or last one
print(str[1: ])

#negative index when we go from right to left we use -ve indexes
#it dosen't start with 0 it starts with -1
# in this case last one get's ignored
str=("apple")
#apple
#-5to-1
str[-3:-1]



"""
str.endswith("va")           returns true if string actually ends with va
str.capitalize()             capitalizes first character
str.replace(old,new)         replaces all occurancs of old with new
str.find(word)               returns 1st index of 1st occurrence
str.count("sharva")          counts the occurrance of sub str in string
"""
str = "sharva"
print(str.find("a"))     #"" lavna noko visrus
str.replace("a","r")

#practice
#write a problem to take input of user and print its length

name=str(input("enter the name: "))
print(len(name))


#WAP to to find occurance of $ in a string

str = "Hi,im sharva"
str.count("a")