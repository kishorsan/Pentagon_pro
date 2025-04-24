def main():
    Num = int(input("Enter a number: "))
    N = len(Num, 0)
    out =  0
    if armstrong(Num, out, N) == Num:
        print("Is armstrong")
    else:
        print("Is not armstrong")


def armstrong(num, out, N):
    if num <= 0:
        return out
    base = num%10
    return armstrong(num//10, out + base**N, N)


def len(num, N):
    if num <= 0:
        return N
    return len(num//10, N + 1)

if __name__ == '__main__':
    main()