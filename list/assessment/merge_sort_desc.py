from .CreateaList import createList

def merge_sort(arr1, arr2):
    res = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        try:
            if arr1[i] > arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        except:
            if i < len(arr1):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
    return res

def main():
    print("Enter first array: ")
    arr1 = createList()
    print("Enter second array: ")
    arr2 = createList()
    out = merge_sort(arr1, arr2)
    print(f"Final Array: {out} ")

if __name__ == '__main__':
    main()