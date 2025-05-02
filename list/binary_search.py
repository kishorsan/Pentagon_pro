from mergeLstAsc import createList

def main():
    # arr = createList()
    # target = int(input("Enter target: "))
    # res = binary_search_asc(arr, target)
    # if res != -1:
    #     print(f"Target element {target} found at index {res}")
    # else:
    #     print("Not found")

    # arr = [100, 99, 88, 77, 66, 55, 44, 33, 11, 10, 1]
    # target = 33
    # res = binary_search_desc(arr, target)
    # if res != -1:
    #     print(f"Target element {target} found at index {res}")
    # else:
    #     print("Not found")

    arr = list(map(int, input().split()))
    target = int(input("Enter the target: "))
    res = order_agnostic_binary_search(arr, target)
    print(res)

def binary_search_asc(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_search_desc(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start+end)//2
        if target == lst[mid]:
            return mid
        elif target > lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def order_agnostic_binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    flag = lst[start] < lst[end]
    while start <= end:
        mid = (start+end)//2
        if target == lst[mid]:
            return mid
        elif flag and target < lst[mid]:
                end = mid - 1
        elif flag:
                start = mid + 1
        elif target > lst[mid]:
                end = mid - 1
        else:
                start = mid + 1
    return -1

main()