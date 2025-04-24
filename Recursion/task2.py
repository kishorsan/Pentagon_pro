# For Output : 1 2 3 4 4 3 2 1
def printNum(n, i=1):
    if i > 4:
        return
    print(i)
    printNum(n, i + 1)
    print(i)
    

n = int(input("Enter a number: "))
printNum(n)

