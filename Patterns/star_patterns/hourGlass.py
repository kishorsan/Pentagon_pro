n = int(input("Enter a numbe : "))
noc = n
for i in range(1,n*2):

    for k in range(n, noc, -1):
        print(" ", end='')    
    
    for j in range(noc):
        print("*", end=' ')
    print()

    
    if i < n:
        noc = noc - 1
    else:
        noc = noc + 1