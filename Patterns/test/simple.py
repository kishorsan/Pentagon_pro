n = int(input("Enter a number : "))

cot = 0
for i in range(n, 0, -1):
    print("  "*cot, end=' ')
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
    cot += 1

print("\n")
cot = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(f"{cot:2}", end=' ')
        cot += 1
    print()

print("\n")

# cot = 1
# csr = n
# for i in range(1, n+1):
#     print("  "*csr, end=' ')
#     for j in range(1, (i*2)):
#         if i == n:
#             print(f"{cot:3}", end=' ')
#             cot += 1
#             continue
#         elif j == 1 or j+1 == i*2:
#             print(f"{cot:3}", end=' ')
#             cot += 1
#         else:
#             print(" ", end='')
#     csr -= 1
#     print()

print("\n")
noc = n
for i in range(1, n+1):
    print(" "*noc*2, end=' ')
    for j in range(1,i*2):
        if i == n and j%2 != 0:
            print("*", end=' ')
        elif j == 1 or j+1 == i*2:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    noc -= 1
    print()

print("\n")
# noc = 0
# for i in range(1, n+1):
#     if i >= 3:
#         noc += 1
#     print(" "*(noc*2), end=' ')
#     for j in range(1, n+2):
#         if (i+j)%2 == 0:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()