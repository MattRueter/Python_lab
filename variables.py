print("/////////////////////////////////////////////////////////////")
x, y, z = "Matt", "Victoria", "Mike"
print(x,y,z)

print("---------------------------------------------------------")
x=y=z = "changed"
print(x,y,z)

print("---------------------------------------------------------")
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x,y,z)

print("---------------------------------------------------------")
#Global variables 
x = "open"

def myfunc():
    x = "closed"
    print("Python is",x)

print(x)
#myfunc()

#Global variable declared within function block
def otherfunc():
    global x
    x = "new thing"
otherfunc()
print(x)
print("/////////////////////////////////////////////////////////////")