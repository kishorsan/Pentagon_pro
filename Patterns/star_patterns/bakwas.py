n = 7

print("In recursion I guess!\n")

def inner(n):
    if n <= 0:
        return
    print("*",end=' ')
    inner(n-1)

def pattern(n):
    if n <= 0:
        return
    inner(n)
    print()
    pattern(n-1)


    
pattern(n)