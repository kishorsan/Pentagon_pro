'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

n = int(input("Enter a value : "))
noc = n - 1
nor = 1
for i in range(1,n*2 + 1):
    for k in range(noc):
        print(" ", end=' ')
    
    for j in range(1,nor*2):
        print("*", end=' ')
    print()

    if i < n:
        noc -= 1
        nor += 1
    else:
        noc += 1
        nor -= 1