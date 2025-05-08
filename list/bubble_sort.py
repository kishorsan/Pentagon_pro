def create_list():
    lst = []
    while True:
        try:
            lst.append(int(input("Enter a num: ")))
        except:
            return lst

def bubble_sort(arr, isasc):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if (arr[j] > arr[j+1]) and isasc :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif not isasc and arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = create_list()
print(arr)
bubble_sort(arr, 1)
print(arr)
bubble_sort(arr, 0)
print(arr)