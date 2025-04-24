# range(max, min-1, -1) 
# range(min, max+1, 1) 

# Range function works in excluding w.r.t the step used !!!
# for +1 step we need to use range(1, n+1, 1)
# for -1 step we need to use range(n, 1-1, -1)
'''
for i in range(9, 1-1, -1):
    print(i,end=" ")
print("\nprogram ends!\n")


for i in range(ord('a'),ord('z')+1):
    print(chr(i), end=' ')
print("\n\n")


dict = { "name":"Ksi", "age":21, "student":True, "Gender":'M'}
for i,j in dict.items():
    print(i, " : ",j)
print("\n")


lst = ["RockHard", ["Hello", "Kitty"], "Fu", 99, [1,[2,[3,[4,[5,[6],7],8],9],10],11], 404, 200, "Network avail", "Hacked"]
for i in lst:
    print(i, end="\t")
print("\n\n")

nSet = {7,8,1,0,9,11,8,1111,902,83}
aSet = {1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0}
for i in aSet:
    print(i, end='  ')

'''

# FOR #
#-->  For loop is itterable, uses range() function with one, two and three arguments
#     ex :- range(10)   range(1,10)    range(1,10,2)

for  i in range(10):
    print(i,end=' ')
print()

for i in range(1,10):
    print(i,end=' ')
print()

for i in range(9,1-1,-1):
    print(i,end=' ')
print()
# range() function is not inclusive of the end value

#-->  For loop can also be used to itterated over collection of objects like - a list, string, dictonary, sets, tuples

for i in [1,2,3,4,5]:
    print(i, end=' ')
print()


dict = { "name":"Ksi", "age":21, "student":True, "Gender":'M'}
for i,j in dict.items():
    print(i, " : ",j)
print("\n")


aSet = {1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0}
for i in aSet:
    print(i, end='  ')
print()

#-->  for loop can take more than one input based on the itterable object used 
#     ex :- for a, b in (1,2), (3,4), (5,6):
aList = [('a','A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E')]
for small,Caps in aList:
    print(small, " : ", Caps)
    