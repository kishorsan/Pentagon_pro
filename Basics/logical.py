print(True and 0 and True)
print(((2+3)>(1**10))and(15<25))
print(((True+True)<True)and True)
print(True or True or True or False)
print((2+3)or(5+3))
print((0+0)or(9+1))
print(not(True and True))
print(not(((5>3)or(6<10))and((10>9)or(11<10))))

def push(arr):
    newarr = []
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1 
            continue
        newarr.append(arr[i] or arr[i+1])
    newarr += [0]*count 
    print(newarr)

arr = [1,2,0,3,0,4,6,0,9]
push(arr)