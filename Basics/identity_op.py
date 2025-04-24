a = 10
b = 5 * 2
c = 20
d = (5 * 2 )+ 10
print(a is b)
print(a is d)
print(c is not b)

print(id(a))
print(id(b))
print(id(c))
print(id(d))

# Heap will always provide a new memory - and will work the samw with List, stirng, tupple, dictionary, set because all of these are objects

# all DS are assigned in Heap the special ones are Tupple and String

l1 = [10, 20] # list is an object and it's memory is allocated on the heap 
l2 = [10, 20]
print(l1 is l2)
print(l1[0] is l2[0])
print(id(l1))
print(id(l2))

# IMMUTALE objects the memorry is provided differently

# does not work with string is immutable
s1 = "Baba"
s2 = "Baba"
print(id(s1),id(s2))
print(s1 is not s2)

tu1 = (1,2,3,4,5)
tu2 = (1,2,3,4,5)
print(tu1 is tu2) # tupple is also a special object soo tupple is immutable


#MUTABLE Objects
se1 = {1,2,3,4}
se2 = {1,2,3,4}
se2[0] = 3
print(se1 is se2) #set is also mutable and is stored in heap and the memorry allocated to both same value pare sets is different

dict1 = {1:1, 2:4, 3:9}
dict2 = {1:1, 2:4, 3:9}
print(dict1 is dict2)  # dict is mutabele and is stored in heap and the memory allocation is different

