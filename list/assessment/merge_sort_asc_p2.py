def main():
    l1 = [1, 22, 23, 45, 56, 67]
    l2 = [82, 67, 53, 35, 20, 6, 4, 2, 0] 
    
    print("Merged list Ascinding: ", merge_sort_asc(l1, l2))
    print("Merged list Descinding: ", merge_sort_desc(l1, l2))

def merge_sort_asc(arr1, arr2):
    i = 0
    j = len(arr2) - 1
    res = []
    while i < len(arr1) or j >= 0:
        try:
            if j == -1:
                raise Exception("one list's index is -1")
            elif arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j -= 1
        except:
            if i < len(arr1):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j -= 1
    return res

def merge_sort_desc(arr1, arr2):
    i = len(arr1) - 1
    j = 0
    res = []
    while j < len(arr2) or i >= 0:
        if i == -1:
            if i >= 0:
                res.append(arr1[i])
                i -= 1
            else:
                res.append(arr2[j])
                j += 1
        elif arr1[i] > arr2[j]:
            res.append(arr1[i])
            i -= 1
        else:
            res.append(arr2[j])
            j += 1
    return res
if __name__ == "__main__":
    main()