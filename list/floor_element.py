# WAP to display the index of the floor element in a given sorted array of the provided target

# floot element : It is the largest or equal value which is smaller than the target 

# arr = [1, 3, 5, 5, 7, 9, 10, 15, 22, 26];
# target = 11 ==> floor = 10
# target = 9 ==> floor = 9
# target = 27 ==> floor = 26
# target = 0 == > floor = -1

def binary_asc_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start+end)//2
        if target == lst[mid]:
            return mid
        elif target < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

def main():
    arr = list(map(int, input().split()))
    target = int(input("Enter the target: "))
    res = binary_asc_search(arr, target)
    print(res)

main()