n = int(input("Enter a num: "))
noc = 0
ncr = n
for i in range(1, n*2):
    print("  "*noc, end='')
    for j in range(1, ncr*2):
        print("*", end=' ')
    print()
    if i < n:
        ncr -= 1
        noc += 1
    else:
        noc -= 1
        ncr += 1