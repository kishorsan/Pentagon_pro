n = int(input("Enter a number : "))
'''
1 2 3 4 
1 2 3 4
1 2 3 4
1 2 3 4 
'''

for i in range(1, n+1):
    for j in range(1,n+1):
        print(j, end=' ')
    print()

print("\n")

# In an incrementing order
# Same as below
noc = n
for i in range(1, n+1):
    for j in range(1,i+1):
        print(noc, end=' ')
    print()
    noc -= 1

print("\n")

# In a decrementing order

'''
4
3 3
2 2 2 
1 1 1 1
'''

for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        print(i, end=' ')
    print()

print("\n")

'''
1 2 3 4 
1 2 3
1 2
1
'''

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

print("\n")

'''
      4 
    4 3
  4 3 2
4 3 2 1
'''

for i in range(n, 0, -1):
    for k in range(i-1):
        print(" ", end=' ')
    for j in range(n,i-1,-1):
        print(j, end=' ')
    print()

print("\n")

'''
      4
    3   3
  2   2   2
1   1   1   1 
'''

noc = n
for i in range(1, n+1):
    for k in range(1,noc):
        print(" ", end=' ')
    for j in range(1, i*2):
        if j%2 == 0:
            print(" ", end=' ')
            continue
        print(noc, end=' ')
    print()
    noc -= 1 

print("\n")
noc = 1
for i in range(1, n*2):
    for j in range(1, noc + 1):
        print(j, end=' ')
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1

print("\n")
noc = 1
nor = n
for i in range(1, n*2):
    for k in range(1, nor):
        print(" ", end=' ')
    for j in range(1, noc+1):
        print(j, end=' ')
    print()

    if i < n:
        noc += 1
        nor -= 1
    else:
        nor += 1
        noc -= 1

print("\n")

noc = 1
for i in range(1, n*2):
    for k in range(1, noc):
        print("-", end=' ')
    for j in range(n, noc-1, -1):
        print(j, end=' ')
    print()

    if i < n:
        noc += 1
    else:
        noc -= 1

print("\n")
noc = 1
for i in range(1, n*2):
    for j in range(noc, 0, -1):
        print(j, end=' ')
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1

print("\n")

noc = 1
nor = n
idk = 0
for i in range(1, n*2):
    for k in range(nor):
        print(" ", end=' ')
    for j in range(1, noc*2):
        if j <= noc:
            print(j, end = ' ')
            idk = j
        else:
            idk -= 1
            print(idk, end=' ')
        
    print()
    if i < n:
        nor -= 1
        noc += 1
    else:
        nor += 1
        noc -= 1

print("\n")
noc = 1
nor = n
for i in range(1, n*2):

    print("  "*nor, end='')

    for j in range(1, noc + 1):
        print(j, end=' ')

    for j in range(noc - 1, 0, -1):
        print(j, end=' ')
        
    print()
    if i < n:
        nor -= 1
        noc += 1
    else:
        nor += 1
        noc -= 1


print("\n")
noc = 1
nor = n - 1
for i in range(1,n*2):
    for j in range(noc, 0, -1):
        if j <= noc:
            print(j, end=' ')
        else:
            print(" ", end=' ')
    print("  "*(nor*2-1), end='')
    for j in range(1, noc+1):
        if j == 1 and i == n:
            continue
        print(j, end=' ')
        
    print()
    if i < n:
        noc += 1
        nor -= 1
    else:
        noc -= 1
        nor += 1


print("\n")
for i in range(1,n+1):
    for j in range(1, n+1):
        if i <= j:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()


print("\n")

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if i <= j:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

print("\n")

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            print(j, end=' ')
        else:
            print(i, end=' ')
    print()

print("\n")

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if i > j:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

print("\n")

for i in range(1, n+1):
    for j in range(1, i+1):
        if (i+j)%2 == 0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()


print("\n")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if (i+j)%2 == 0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

print("\n")
k = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{k:2}", end=' ')
        k += 1
    print()

print("\n")
count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i%2 != 0:
            count += 1
            print(f"{count:2}",end=' ')
            
        else:
            print(f"{count:2}", end=' ')
            count -= 1
    count += n
    print()

print("\n")
count1 = 1
count2 = 0
for i in range(1,n+1):
    for j in range(1, i+1):
        if i%2 != 0:
            print(f"{count1:2}", end=' ')
            count2 = count1
        else:
            print(f"{count2:2}", end=' ')
            count2 -= 1
        count1 += 1
    count2 += i + 1
    print()


print("\n")
count = n*n
for i in range(1, n+1):
    for j in range(1,n+1):
        print(f"{count:<2}", end=' ')
        count -= 1
    print()

print("\n")

count = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if i%2 != 0:
            count += 1
            print(f"{count:<2}", end=' ')
        else:
            print(f"{count:<2}", end=' ')
            count -= 1
    if i%2 == 0:
        count += i
    else:
        count += i + 1
    print()
# noc = 1
# for i in range(1, n*2):
#     noc = i
#     for j in range(1, n*2):
#         if i <= j or i+j <= n*2:
            
#             print(noc, end=' ')
#             noc -= 1
#         else:
#             print(" ", end=' ')
#     if i < n:
#         noc += 1
#     else:
#         noc -= 1
#     print()
# num = 0
# end = 0
# for i in range(1, n+1):
#     end = i
#     for j in range(1, end+1):
#         print(num, end=' ')
#         num -= 1
        
#     print()
#     num = i
#     end += i
#     # print(num)
    

    # print(f"{count:2}")