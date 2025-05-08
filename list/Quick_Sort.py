# Philosophy - bring the lowest element to the begining 
# if pivote is smaller than end bring down end and if pivote is greater than end make it a violation
# if piote is smaller than start make it a violation and stop there

def createList():
    lst = []
    while True:
        try:
            lst.append(int(input("Enter a num: ")))
        except:
            return lst
        

def Quick_Sort(arr, low, high):
    if low >= high:
        return
    start = low
    end = high
    mid = (start + end )//2
    pivot = arr[mid]
    while start < end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    Quick_Sort(arr, low, end)
    Quick_Sort(arr, start, high)

# def Quick_Sort(arr, low, high):
#     if low >= high:
#         return
#     start = low
#     end = high
#     mid = (start + end )//2
#     pivot = arr[mid]
#     while start <= end:
#         while arr[start] < pivot:
#             start += 1
#         while arr[end] > pivot:
#             end -= 1
#         if start > end:
#             break
#         if arr[start] >= arr[end]:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1
#     if arr[start] == pivot:
#         high -= 1
#     elif arr[end] == pivot:
#         low += 1
#     Quick_Sort(arr, low, high)

def main():
    # arr = createList()
    arr = [-1, -99, 567, 98, 3, 8, 55, -11, 9, 76, 4]
    print(arr)
    Quick_Sort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == '__main__':
    main()