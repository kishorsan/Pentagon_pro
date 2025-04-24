def main():
    n1 = int(input("Enter a number : "))
    n2 = int(input("Enter another number : "))
    if n1 > n2:
        n1, n2 = n2, n1
    try:
        print(lcm(n1,n2,n2))
    except RecursionError:
        print("Recursion limit exceeded, Using While loop!!")
        i = n2
        while True:
            if i%n1 == 0 and i %n2 == 0:
                print(i)
                break
            i += 1
        
        print("Another way to find LCM")
        j = 2
        res = 1
        while True:
            if j > n1:
                res *= n1 * n2
                break
            if n1%j == 0 and n2 %j == 0:
                res *= j
                n1 /= j
                n2 /= j
            else:
                j += 1
        print(int(res))


def lcm(x,y,i):
    if i%x == 0 and i%y == 0:
        return i
    return lcm(x,y,i+1)


if __name__ == '__main__':
    main()


