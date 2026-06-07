#dictonary
# used to store data values in key:value pair
#they are unordered mutable & dont allow dubicate keys

info = {
          "key" : "value",
          "name" : "sharva",
          "marks" : [98,97,96],
          "age" : 19,
          "is an adult" : True,
          848.08 : 421,


}

print(type(info))

print(info["name"])
info["name"] = "sharvaM"     #mutable
info["surname"] = "Motegaonkar"   #added from outside

print(info)

null_dictonary = {}
null_dictonary["name"] = "apna collage"
print(null_dictonary)

#nested dictonary
# , noko visrus
student = {
    "name":"sharva",
    "subjects" : {
         "phy" : "49",
         "maths" : "49",
         "chem" : "xyz",

    }

}
print(student)
print(student["subjects"])
print(student["subjects"]["phy"])

print(student.keys())
print(student.values())
print(student.items())
print(list(student.items()))       #gives tupple of items
print(student.get("name"))        #it works just like.values but if key is not present we won't get error and output will be "none" and the whole code won't be jeopardized
new_dict={"city": "Chh sambhaji nagar"}
student.update(new_dict)
print(student)
pair = list(student.items())
print(pair[0])               #directly print nhi kru shakat adhi konchaya variable la toh tupple assign krawa lagel

#dictonary methods
"""myDict.keys()      # returns all keys

myDict.values()    # returns all values

myDict.items()     # returns all (key, val) pairs as tuples

myDict.get("key")  # returns the value for the given key

myDict.update(newDict)  # inserts the specified items into the dictionary"""

#set
#it's a collection of unordered items each element in the set must be unique and mutable
"""sets can have boolean, integer,float,string,tupple, it does NOT include list and dictonary"""

collection = {1, 2, 2, 2, "hello", "world", "world"}

print(collection)
print(type(collection))   #notice how its unordered
print(len(collection))


# to create an empty set
abc = set()
print(type(abc))



s = {2,3,4,5}
s.add(7)        # adds an element
s.remove(3)     # removes the element
s.pop()          # removes an random value
s.clear()        # empties the set

print(s)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))  # {1, 2, 3, 4}
print(set1)
print(set2)

print(set1.intersection(set2))

