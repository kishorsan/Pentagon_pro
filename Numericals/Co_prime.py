def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second numbe: "))
    if n1>n2:
        n1, n2 = n2, n1
    coPrime = Co_prime(n1,n2,n1)
    if coPrime == 1:
        print("The numbers are co-prime")
    else:
        print("The numbers are not co-prime")

def Co_prime(x, y, i):
    if x%i == 0 and y%i == 0:
        return i
    return Co_prime(x,y,i-1)


if __name__ == '__main__':
    main()
    