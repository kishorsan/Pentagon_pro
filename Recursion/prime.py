def main():
    num = int(input("Enter a number: "))
    flag = prime(num, 1, 0)
    if flag:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
    pass

def prime(num, i, base):
    if i > num:
        return base == 2
        # print(i)
        # base += 1 
    return prime(num, i + 1,base + 1 if num % i == 0 else base )

if __name__ == '__main__':
    main()