# For Output : 4 3 2 1
def printNum(n):
    if n <= 0:
        return
    print(n)
    printNum(n - 1)


n = int(input("Enter a number: "))
printNum(n)
# This program takes a number as input and prints all the numbers from that number down to 1 using recursion.
