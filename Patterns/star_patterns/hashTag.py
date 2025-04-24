n = int(input("Enter a number : "))

for i in range(n*2, 0, -1):
    print(" "*i, end='')
    for j in range(1, n*2+1):
        if i%3 == 0 or j %3 == 0:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

