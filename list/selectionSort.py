def sorting(arr):
    cmi = 0
    ai = len(arr) - 1
    if arr[cmi] > arr[ai]:
            arr[cmi], arr[ai] = arr[ai], arr[cmi]
    for i in range(len(arr)-1):
        ai = len(arr) - 1 - i
        for j in range(len(arr)-1-i):
            cmi = j    
            if arr[cmi] > arr[ai]:
                arr[cmi], arr[ai] = arr[ai], arr[cmi]
    return arr

def main():
    arr = list(map(int, input().split()))
    out = sorting(arr)
    print(out)
main()