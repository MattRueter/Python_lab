mytuple = ("apple", "banana", "cherry", "orange","kiwi", "melon", "mango")
if "apple" in mytuple:
    print("yes, apple is in mytuple")

#Tuples are inmutable but there are workaround
x = ("matt", "victoria", "michael")
y = list(x)
y[1]= "kiwi"
print(y)
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry", "orange","kiwi", "melon", "mango")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)
print(thistuple)

fruits = ("apple", "banana", "cherry")
(one, two, three) = fruits
print(one)
print(two)
print(three)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "orange")
(one, two, *three) = fruits
print(one)
print(two)
print(three)
print("_____________________________________________________________________________________________________________")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "orange")
(one, *two, three) = fruits
print(one)
print(two)
print(three)
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////")
fruits = ("apple", "banana", "cherry")
myTuple = fruits * 2
print(myTuple)
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////")
fruits = ( "banana", "cherry", "apple","strawberry", "raspberry", "apple", "orange")
print(fruits.count("apple"))
print(fruits.index("apple"))
f = open("variables.py", "r")
