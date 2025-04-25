def sorting(arr):
    n = len(arr)
    cmi = 0
    ai = n - 1
    if arr[cmi] > arr[ai]:
            arr[cmi], arr[ai] = arr[ai], arr[cmi]
    for i in range(n-1):
        ai = n - 1 - i
        for j in range(n-1-i):
            cmi = j    
            if arr[cmi] > arr[ai]:
                arr[cmi], arr[ai] = arr[ai], arr[cmi]

def main():
    arr = list(map(int, input().split()))
    sorting(arr)
    print(arr)
    
main()