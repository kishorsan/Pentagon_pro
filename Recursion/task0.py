# For Output : 1 2 3 4
def increment(n):
    if n <= 0:
        return
    # print(n)
    increment(n - 1)
    print(n)

n = int(input("Enter a number : "))
increment(n)
