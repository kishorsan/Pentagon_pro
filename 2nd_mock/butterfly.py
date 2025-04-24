n = int(input("enter a number: "))

plus = 0
noc = 1
ncr = n*2
for i in range(1, n*2):
    for j in range(1, n*2):
        if j <= noc or j+1 >= ncr:
            print(chr(97+plus), end=' ')
        else:
            print(chr(32), end=' ')
    print()
    if i < n:
        plus += 1
        noc += 1
        ncr -= 1
    else:
        plus -= 1
        noc -= 1
        ncr += 1