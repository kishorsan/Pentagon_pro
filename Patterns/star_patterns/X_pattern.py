n = int(input("Enter a number : "))
noc = 1
nor = n*2 - 1
for i in range(1,n*2):
    for j in range(1,n*2):
        if noc == j or nor == j:
            print("*",end=' ')
        else:
            print(" ", end=' ')
    if i < n:
        noc += 1
        nor -= 1
    else:
        noc -= 1
        nor += 1

    
    print()
    