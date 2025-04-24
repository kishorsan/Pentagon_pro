def main():
    aNum = int(input("Enter a number : "))
    print(mulNum(aNum))

def mulNum(num):
    if num <= 9:
        return num
    return num%10 * mulNum(num//10)

if __name__ == '__main__':
    main()