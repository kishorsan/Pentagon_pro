def create_list():
    l1 = []
    while True:
        try:
            l1.append(int(input()))
        except Exception as ValueError:
            return l1
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
def main():
    arr = create_list()
    print(arr)
    bubble_sort(arr)
    print(arr)

main()