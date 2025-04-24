def main():
    n1 = int(input("Enter a number : "))
    n2 = int(input("Enter another numbe : "))
    if n1 > n2:
        n1 , n2 = n2, n1
    out= fact(n1, n2, 1, 1)
    print(out)

def fact(n1, n2, j, gcd):
    if j > n1:
        return gcd
    if n1%j == 0 and n2%j == 0:
        gcd = j
    return fact(n1, n2, j + 1, gcd)


if __name__ == '__main__':
    main()