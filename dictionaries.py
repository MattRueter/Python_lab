thisdict = {
    "brand":"Alfa Romeo",
    "model": "spider",
    "year": "1965"
}
print(thisdict["brand"])
print(thisdict.items())
if "model" in thisdict:
    print("Yes, `model` is one of the keys in thisdict")

print("-------------------------------------------------------------------------------")
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

print("-------------------------------------------------------------------------------")
print(thisdict.keys())
print(thisdict.values())

print("-------------------------------------------------------------------------------")
for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

print("-------------------------------------------------------------------------------")
#loop through both keys and values using items() method.
for x, y in thisdict.items():
    print(x, y)

print("-------------------------------------------------------------------------------")
#dictionaries are mutable. To create inmutable copies use the following two methods.
#1
copy = thisdict.copy();
print(copy)
#2
altCopy = dict(thisdict)
print(altCopy)