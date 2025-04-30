from CreateaList import createList

def AscList(arr1, arr2):
    i = len(arr1) - 1 
    j = len(arr2) - 1
    res = []
    while i >= 0 or j >= 0:
        try:
            if i == -1 or j == -1:
                raise Exception("one list's index is -1")
            elif arr1[i] < arr2[j]:
                res.append(arr1[i])
                i -= 1
            else:
                res.append(arr2[j])
                j -= 1
        except:
            if i >= 0:
                res.append(arr1[i])
                i -= 1
            else:
                res.append(arr2[j])
                j -= 1
    return res

def main():
    print("Enter first list: ")
    arr1 = createList()
    print("Enter second list: ")
    arr2 = createList()
    print("Merged list in ascending order: ", AscList(arr1, arr2))

if __name__ == "__main__":
    main()