# Write a program to reverse a number using recursion.

def main():
    num = int(input("Enter a number: "))
    N = len(num, 0)
    mun = reverseNum(num, N, 0)
    print(mun)

def reverseNum(num, N, rev):
    if num <= 0:
        return rev
    step = num%10 * 10**(N-1)
    return reverseNum(num//10, N-1, rev + step)

def len(num, count):
    if num <= 0:
        return count
    return len(num//10, count + 1)
    pass

if __name__ == '__main__':
    main()