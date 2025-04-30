l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
print("Before: ")
print("arr 1: ", l1)
print("arr 2: ", l2)


l3 = l1 + l2

print("After: ")
print("arr 1: ", l1)
print("arr 2: ", l2)
print("arr 3: ", l3)


# for i in l2:
#     l1.append(i)

# print("arr 1: ",l1)

l4 = l1[:]
n = len(l1)
for i in l2:
    l4.insert(n, i)
    n += 1

print("arr 4: ", l4)

#WAP to merge the given two arrays at alternate index

arr1 = [1,2,3]
arr2 = [10,19,18,17,16]
# n = len(arr1)  
# m = len(arr2) 
# if n > m:
#     n = m
# res = []
# count = 0
# for i in range(n+1):
#     if i == n:
#         res += arr2[count:]
#         break
#     res.append(arr1[count])
#     res.append(arr2[count])
#     count += 1
# print(res)

def createArr():
    l1 = []
    while True:
        try:
            l1.append(int(input()))
        except:
            return l1

def appendLogic():
    print("Enter array 1: ")
    arr1 = createArr()
    print("Enter array 2: ")
    arr2 = createArr()
    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)
    res = []
    for k in range(n+m):
        if i < n and k%2 == 0:
            res.append(arr1[i])
            i += 1
        elif j < m and k%2 != 0:
            res.append(arr2[j])
            j += 1
        else:
            if i < n:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
    print(res)

out = appendLogic()
print(out)

def insertLogic():
    print("Enter first array: ")
    arr1 = createArr()
    print("Enter second array: ")
    arr2 = createArr()
    n = len(arr1)
    m = len(arr2)
    res = []
    i, j = 0, 0
    for k in range(n+m):
        if i < n and k%2 == 0:
            res.insert(k,arr1[i])
            i += 1
        elif j < m and k%2 != 0:
            res.insert(k, arr2[j]) 
            j += 1
        else:
            if i < n:
                res.insert(k, arr1[i])
                i += 1
            else:
                res.insert(k, arr2[j])
                j += 1
    return res

out = insertLogic()
print(out)