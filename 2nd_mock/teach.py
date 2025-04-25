
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

print("\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

print("\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
    
print("\n")
n = 4
for i in range(1,n+1):
    noc = 0
    for j in range(1,n+1):
        print(chr(64+i+noc),end=" ")
        noc += n
    print()
    
print("\n")