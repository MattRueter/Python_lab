this_list = [ "apple", "banana", "cherry", "apple", "cherry" ]
print(this_list)
print(len(this_list))
print(type(this_list))
new_list = list(("dog", "fish", "monkey"))
print(new_list)
if "monkey" in new_list:
    print("Yes, Monkey is in the list.")
else:
    print("No. Monkey is not in the list.")

print("ACCESSING ITEMS-------------------------------------------------------------------------")
my_list = ["opera", "sol", "gran via", "sevilla", "banco de españa", "retiro", "goya"]
print(len(my_list[2:5]), " items: ", my_list[2:5])


print("CHANGING VALUES-------------------------------------------------------------------------")
my_list = [ "goya", "colon", "alonso martinez", "bilbao" ]
print(my_list)
my_list[1:2] =["ventura rodriguez", "argüelles"]
print(my_list)
my_list[1:2] =["test" , "testing"]
print(my_list)

my_list = [ "goya", "velazquez","colon" ]
my_list[1:3]= [ "test" ]
print(my_list)

my_list.append("ventura rodriguez")
print(my_list)

my_list = ["goya", "colon", "alonso martinez", "bilbao"]
my_list.insert(1, "velazquez")
print(my_list)

#extend Combines 2+ lists or other iterable objexts (tuples, sets, dictionaries, etc.).
this_list = ["matt", "victoria", "mike"]
other_list = ["jay", "ben", "brendan", "alistair", "oliver"]
this_list.extend(other_list)
print(this_list)

thistuple = ("kiwi", "orange")
print(thistuple)
this_list.extend(thistuple)
print(this_list)

this_list.pop(9)
print(this_list)

print("DELETING and EMPTYING LISTS-------------------------------------------------------------")
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)

this_list = ["apple", "banana", "cherry"]
print(this_list)
del this_list
#print(this_list) #throws error

print("LOOPING---------------------------------------------------------------------------------")
this_list = ["apple", "banana", "cherry"]
print(this_list)

for x in this_list:
    print(x)

print("//////////////////////////////////////////")
for i in range(len(this_list)):
    print(this_list[i])

print("//////////////////////////////////////////")
i = 0
while i < len(this_list):
    print(this_list[i])
    i = i + 1
#OR in reverse 
i = len(this_list) -1
while i >= 0:
    print(this_list[i])
    i = i - 1

print("LIST COMPREHENSION//////////////////////////////////////////")

[print(x) for x in this_list]

new_list = [x for x in this_list if "e" in x]
#newlist = [expression for item in iterable if condition == True]
print(new_list)

new_list = [x for x in range(10)]
print(new_list)
new_list = [x for x in range(10) if x%2 == 0]
print(new_list)
new_list = [x for x in range(10) if x%2 != 0]
print(new_list)
new_list = [x*3 for x in range(10) if x%2 == 0]
print(new_list)
new_list = ["got one." for x in range(10) if x%2 == 0]
print(new_list)
new_list = [x if x != "banana" else "strange fruit" for x in this_list]
print(new_list)
new_list = [x if x == "banana" else "strange fruit" for x in this_list]
print(new_list)


print("LIST SORTING//////////////////////////////////////////")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [100, 50, 65, 82, -5, 23]
numlist.sort()
print(numlist)

#reversing
thislist.sort(reverse = True)
numlist.sort(reverse = True)
print(thislist)
print(numlist)

#case insensitive
thislist = ["orange", "mango", "kiwi", "Pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(key=str.lower)
print(thislist)

#reversing regardless of alphabet or criterira. Hard reverse
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.reverse()
print(thislist)

#customize sort
numlist = [100, 50, 65, 82, -50, 23]
def myfunc(n):
    return abs(n - 50)
numlist.sort(key=myfunc)
print(numlist)

names = [ "matt", "victoria", "mike", "chema", "Miki", "jay", "audrey", "barbarbarbarbarbaranne", "eddie"]
def namefunc(name):
    return (len(name))
names.sort(key=namefunc)
print(names)

print("COPY A LIST///////////////////////////////////////////////////////////////////////////////////")
thislist = ["apple" , "banana", "cherry"]
newlist = thislist.copy()
print(thislist, "//////", newlist)
thislist.insert(0, "test")
print(thislist, "//////", newlist)
newlist.insert(len(newlist),"testing")
print(thislist, "//////", newlist)

thislist = ["apple" , "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("JOIN LISTS ///////////////////////////////////////////////////////////////////////////////////")
list1 = ["a","b","c"]
list2 =[ 1,2,3 ]
list3 = list1 + list2
print(list3)
#OR
for x in list2:
    list1.append(x)
    print(list1)
#OR
list1 = ["a","b","c"]
list2 =[ 1,2,3 ]
list1.extend(list2)
print(list1)
