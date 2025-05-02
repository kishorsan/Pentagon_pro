def createList(): # creating an integer array dynamically 
    lst = []
    while True:
        try:
            lst.append(int(input()))
        except:
            return lst # returnig after the exception is raised

def AscList(arr1, arr2):
    i = j = 0 # initial values of i and j 
    arr3 = []
    # Initial comparition 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    # For extra values from array 1
    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    # For extra values from array 2
    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1
    
    return arr3 # returnig the array

def inOneLoop(arr1, arr2):
    res = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1) or j >= len(arr2):
            if i < len(arr1):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        elif arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    return res

if __name__ == '__main__':
    print("Enter first array: ")
    arr1 = createList() # first array
    print("Enter second array: ")
    arr2 = createList() # second array
    res = AscList(arr1, arr2)
    print(f"Final Array: {res} ")
    res1 = inOneLoop(arr1, arr2)
    print(f"Final array: {res1}")
