def createList():
    l1 = []
    while True:
        try:
            num = int(input("Enter a number : "))
        except:
            return l1
        l1.append(num)

def maxNum(l1, max, index):
    for i in range(len(l1)):
        if max < l1[i]:
            max = l1[i]
            index = i
    return (max, index)

def minNum(l1, min, index):
    for i in range(len(l1)):
        if min > l1[i]:
            min = l1[i]
            index = i
    return (min, index)

def maxNumre(l1, max, index, i):
    if i >= len(l1):
        return (max, index)
    if max < l1[i]:
        max = l1[i]
        index = i
    return maxNumre(l1, max, index, i+1)

def minNumre(l1, min, index, i):
    if i >= len(l1):
        return (min, index)
    if min > l1[i]:
        min = l1[i]
        index = i
    return minNumre(l1, min, index, i+1)

# print(-2**31)
if __name__ == '__main__':
    max = -2**31
    maxIndex = -1
    lst = createList()
    out = maxNum(lst, max, maxIndex)
    if out[1] == -1:
        print("No max element as it is an empty list")
    else:
        print(f"Max element is {out[0]} and is at index {out[1]}")
    
    out1 = maxNumre(lst, max, maxIndex, 0)
    if out1[1] == -1:
        print("No max element found as it is an empty list")
    else:
        print(f"Max element: {out1[0]}\nIndex is: {out1[1]} ")
    

    min = (2**31)-1
    minIndex = -1
    result = minNum(lst, min, minIndex)
    if result[1] == -1:
        print("No min element as it is an empty list")
    else:
        print(f"Min element os {result[0]} and is at index {result[1]}")

    result1 = minNumre(lst, min, minIndex, 0)
    if result1[1] == -1:
        print("No max element found as it is an empty list")
    else:
        print(f"Max element: {result1[0]}\nIndex is: {result1[1]} ")