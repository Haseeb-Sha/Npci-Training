dict={
    'a':'b',
    'c':'d',
    'e':2,
    'f':[1,2,3,4],
    'g':{"azaan":"khan", "adnan":"young"}
}
#print(dict)
print(dict['c'])
print(dict.keys())
print(dict.values())
print(dict.get("g"))
dict.update({"h":"i"})
print(dict)