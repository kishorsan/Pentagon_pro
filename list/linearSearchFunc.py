def linearFun(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return (i, True)
    return (-1, False)

def createList():
    lst = []
    while True:
        try:
            num = int(input("Enter a number: "))
        except Exception as e:
            return lst
        lst.append(num)

# lst = list(map(int, input("Enter a list: ").split()))
lst = createList()
target = int(input("Enter a target to find: "))
output = linearFun(lst, target, False)
if output[1]:
    print(f"{target} is found at index {output[0]}")
else:
    print(f"{target} is not found")