n = int(input("Enter a number : "))

'''
* * * * * 
  * - - *
    * - *
      * *
        *
'''

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or i == 1 or j == n:
            print("* ", end='')
        elif j > i:
            print("- ", end='')
        else:
            print("  ", end='')
    print()

print("\n")

'''
*
* *
* - *
* - - *
* * * * *
'''

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or i == n or j == 1:
            print("* ",end='')
        elif j < i:
            print("-", end=' ')
        else:
            print(" ", end=' ')
    print()

print("\n")

'''
* * * * *
* - - *
* - *
* *
*
'''

nor = n
for i in range(1, n+1):
    for j in range(1, n+1):
        if i+j == n+1 or j == 1 or i == 1:
            print("* ", end='')
        elif j < nor:
            print("- ", end='')
        else:
            print("  ", end='')
    print()
    nor -= 1

print("\n")


'''
        *
      *   *
    *   -   *
  *   -   -   *
*   *   *   *   *
'''

noc = n
for i in range(1, n+1):
    for k in range(1, noc):
        print("  ", end='')
    for j in range(1, i*2):
        if j%2 == 0:
            print(" ", end=' ')
        elif j == 1 or j+1 == i*2 or i == n:
            print("* ", end='')
        else:
            print("- ", end='')
    noc -= 1
    print()


print("\n")

'''
*   *   *   *   *
  *   -   -   * 
    *   -   *
      *   *
        *
'''

noc = 1
for i in range(n, 0, -1):
    for k in range(1,noc):
        print(" ", end=' ')
    for j in range(1,i*2):
        if j%2 == 0:
            print(" ", end=' ')
        elif j == 1 or j+1 == i*2 or i == n:
            print("*", end=' ')
        else:
            print("-", end=' ')
    noc += 1
    print()

print("\n")

'''
        *
      * *
    * - *
  * - - *
* * * * *
'''

noc = n
for i in range(1, n+1):
    for k in range(1,noc):
        print(" ", end=' ')
    
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print("*", end=' ')
        else:
            print("-", end=' ')
    print()
    noc -= 1

print("\n")

'''
* * * * *
* - - *
* - *
* *
*
* *
* - *
* - - *
* * * * * 
'''

noc = n
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j == 1 or j == noc or i == 1 or i+1 == n*2:
            print("*", end=' ')
        else:
            print("-", end=' ')
    if i < n:
        noc -= 1
    else:
        noc += 1
    print()

print("\n")

'''
*
* *
* - *
* - - *
* - - - *
* - - *
* - *
* *
*
'''

noc = 1
for i in range(1, n*2):
    for j in range(1,noc+1):
        if j == 1 or j == noc:
            print("*", end=' ')
        else:
            print("-", end=' ')
    if i < n:
        noc += 1
    else:
        noc -= 1
    print()


print("\n")

'''
        *
      *   *
    *   -   *
  *   -   -   *
*   -   -   -   *
  *   -   -   *
    *   -   * 
      *   *
        *
'''

noc = n
nor = 1
for i in range(1,n*2):
    for k in range(1,noc):
        print(" ", end=' ')
    for j in range(1,nor*2):
        if j%2 == 0:
            print(" ", end=' ')
        elif j == 1 or j+1 == nor*2:
            print("*", end=' ')
        else:
            print("-", end=' ')
    if i < n:
        noc -= 1
        nor += 1
    else:
        noc += 1
        nor -= 1
    print()