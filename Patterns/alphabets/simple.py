'''
'A' - 'Z' => 65 - 90
'a' - 'z' => 97 - 122
' ' => 32
'0' - '9' => 48 - 57
'''

n = int(input("Enter a number : "))

for i in range(65, 65 + n):
    for j in range(1, n+1):
        print(chr(i), end=' ')
    print()

print("\n")

for i in range(97, 97 + n):
    for j in range(1, n+1):
        print(chr(i), end=' ')
    print()

print("\n")
csr = 97
for i in range(0, n):
    for j in range(0, n):
        if j <= i:
            print(chr(csr-j), end=' ')
        else:
            print(chr(32), end=' ')
    csr += 1
    print()


print("\n")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print(chr(96+i), end=' ')
        else:
            print(chr(96+j), end=' ')
    print()

print("\n")
for i in range(1, n+1):
    for j in range(n, 0, -1):
        print(chr(64+j), end=' ')
    print()

print("\n")

for i in range(1, n+1):
    for j in range(1, n+1):
        if i <= j:
            print(chr(96+i), end=' ')
        elif j <= i:
            print(chr(96+j), end=' ')
        else:
            print(chr(32), end=' ')
    print()

print("\n")
for i in range(1, n+1):
    for j in range(1, i+1):
        if i%2 != 0:
            print(chr(96+j), end=' ')
        else:
            print(chr(64+j), end=' ')
    print()

print("\n")
csr = 97
shift = n - 1
for i in range(1, n+1):
    print("  "*(shift), end=' ')
    for j in range(1, i*2):
        if j%2 != 0:
            print(chr(csr), end=' ')
            csr += 1
        else:
            print(chr(32), end=' ')
    print()
    shift -= 1

print("\n")
csr = 97
shift = 0
for i in range(n, 0, -1):
    print("  "*shift, end=' ')
    for j in range(1, i*2):
        if j%2 != 0:
            print(chr(csr), end=' ')
            csr += 1
        else:
            print(chr(32), end=' ')
    print()
    shift += 1

print("\n")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j%2 != 0:
            print(chr(101 - j), end=' ')
        else:
            print(chr(69 - j), end=' ')
    print()

print("\n")
for i in range(1, n+1):
    for j in range(n, i-1, -1):
        if j%2 != 0:
            print(chr(64+j), end=' ')
        else:
            print(chr(96+j), end=' ')
    print()

print("\n")
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i + j)%2 == 0:
            print(chr(64+j), end=' ')
        else:
            print(chr(96+j), end=' ')
    print()


print("\n")

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i%2 != 0 != j%2 or i == j:
#             print(chr(64+j), end=' ')
#         else:
#             print(chr(96+j), end=' ')
#     print()
csr = n
for i in range(1, n*2):
    for j in range(1, csr+1):
        print(chr(96+j), end=' ')
    print()
    if i < n:
        csr -= 1
    else:
        csr += 1

print("\n")
csr = n
move = 0
for i in range(1, n*2):
    # print("  "*(move), end='')
    for j in range(1, csr+1):
        print(chr(96+j), end=' ')
    print()
    
    if i < n:
        move += 1
        csr -= 1
        print("  "*(n-csr), end='')
    else:
        move -= 1
        csr += 1
        print("  "*(n-csr), end='')
    

print("\n")

noc = n - 1
plus = 0
for i in range(1, n*2):
    for j in range(1, n+1):
        if j > noc:
            print(chr(97+plus), end=' ')
        else:
            print("-", end=' ')
    print()
    if i < n:
        plus += 1
        noc -= 1
    else:
        plus -= 1
        noc += 1

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