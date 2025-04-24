def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second numbe: "))
    if n1>n2:
        n1, n2 = n2, n1
    hcf = Hcf(n1,n2,n1)
    gcd = Gcd(n1,n2,n1)
    print(hcf)
    print(gcd)

def Hcf(x, y, i):
    if x%i == 0 and y%i == 0:
        return i
    return Hcf(x,y,i-1)

def Gcd(x,y,i):
    if x%i == 0 and y%i == 0:
        return i
    return Gcd(x,y,i-1)


if __name__ == '__main__':
    main()