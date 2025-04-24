n = 4
for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    print()

for i in range(1,n):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("\n\n\n\n")

# for i in range(n*2):
#     if i >= n:
#         for j in range(i-n+1):
#             print("*", end=' ')
#         print()
#         continue

#     for j in range(i,n):
#         print("*", end=' ')
#     print()

n = int(input("Enter a number : "))
noc = n
for i in range(1, n*2):
    for j in range(noc):
        print("*", end=' ')
    print()
    # print(noc,n,i)
    if i < n:
        noc = noc - 1
    else:
        noc = noc + 1