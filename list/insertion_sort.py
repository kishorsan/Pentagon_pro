def create_arr():
    lst = []
    while True:
        try:
            lst.append(int(input("Enter a num: ")))
        except:
            return lst
        

def insertion_sort(arr, isAsc):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1] and isAsc:
                arr[j], arr[j-1] = arr[j-1], arr[j] 
            elif not isAsc and arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = create_arr()
print(f"Array befor sorting: {arr}")
insertion_sort(arr, 1)
print(f"Array after ascending sort: {arr}")
insertion_sort(arr, 0)
print(f"Array after decemding sort: {arr}")