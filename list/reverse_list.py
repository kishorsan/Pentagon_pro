def main():
    arr = createList()
    print(arr)
    n = len(arr)
    shift = int(input("Enter the shift: "))
    shift %= n
    choise = int(input("For rotation: Right(0), Left(1) :- "))
    if choise == 1: 
        rotateLogic(arr, n, shift)
        reverse(arr, 0, n - 1)
    else:
        rotateLogic(arr, n, shift)
        reverse(arr, 0, n - 1)
    print(arr)

def rotateLogic(arr, n, shift):
    reverse(arr, 0, n - 1)
    reverse(arr, 0, shift - 1)

def createList(): 
    print("Enter your array")
    lst = []
    while True:
        try:
            lst.append(int(input("Enter a num : ")))
        except:
            return lst

def reverse(arr, i, j):
    if i > j:
        return
    arr[i], arr[j] = arr[j], arr[i]
    reverse(arr, i+1, j-1)


    
main()