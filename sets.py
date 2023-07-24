thisset = { "apple", "banana", "cherry"}
print("banana" in thisset)

thisset.add("grape")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = [ "kiwi", "orange"]
thisset.update(mylist)
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

for y in thisset:
    print(y)

#--------------------------------------------------------------------------------------
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}

set3 = set1.union(set2)
print(set3)
print(set1) #set unchanged
print(set2) #set unchanged

set1.update(set2)
print(set1) #set changed
print(set2) #set unchanged

#---------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = { "goolge", "apple", "microsoft"}
x.intersection_update(y)
print(x)