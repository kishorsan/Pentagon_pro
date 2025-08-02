def create_list():
    l1 = []
    while True:
        try:
            l1.append(int(input("Enter a number: ")))
        except Exception as ValueError:
            return l1
        
def binary_serch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid
        else:
            start = mid
    return -1

def binary_search_asc_desc(arr, target, flag=False):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        if flag and arr[mid] > target:
            start = mid + 1
        elif flag:
            print(end)
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def main():
    print("Enter a list: ")
    arr = create_list()
    target = int(input("Enter a target number to find: "))
    # print(f"Target element found at index : {binary_serch(arr, target)}")
    type = input("Descinding ?")
    print(f"Target element found at index : {binary_search_asc_desc(arr, target, type)}")

main()


