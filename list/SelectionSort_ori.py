def main():
    arr = list(map(int, input("Enter an arr: ").split()))
    selectionSort(arr)
    print(arr)

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        accI = n - i - 1
        cMaxI = -1
        cMax = -2**31
        for j in range(0, n - i - 1):
            if cMax < arr[j]:
                cMax = arr[j]
                cMaxI = j
        arr[cMaxI], arr[accI] = arr[accI], arr[cMaxI]



if __name__ == '__main__':
    main()