'''
*       *
* *   * *
*   *   *
* *   * *
*       *
'''


n = int(input("Enter a numeber : "))

if n%2 == 0:
    n+= 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or i+j == n+1 or j == 1 or j == n:
            print("* ", end='')
        else:
            print("  ", end='')
    print()