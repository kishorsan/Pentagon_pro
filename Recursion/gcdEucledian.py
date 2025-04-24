def main():
    n1 = int(input("Enter a number : "))
    n2 = int(input("Enter another number : "))
    gcd(n1, n2)
    print(gcd12(n1, n2))
    print(gcdMod(n1,n2))
    gcdLoop(n1,n2)

def gcd(n1, n2):
    if n1 == 0:
        print(n2)
        return n2
    return gcd(n2 % n1, n1)

def gcd12(n1, n2):
    if n1 == n2:
        return n1
    if n1 < n2:
        n1, n2 = n2, n1
            
    return gcd12(n1 - n2, n2)

def gcdMod(n1, n2):
    if n1 == n2:
        return n1
    if n1 < n2:
        n1, n2 = n2, n1
            
    return gcd12(n1 % n2, n2)

def gcdLoop(n1, n2):
    while n1 != n2:
        if n1 < n2:
            n1, n2 = n2, n1
        mod = n1 % n2
        n2 = n1
        n1 = mod
        print(n1,n2)
    print(n1)


if __name__ == '__main__':
    main()