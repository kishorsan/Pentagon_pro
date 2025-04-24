def main():
    aNum = int(input("Enter a number: "))
    print(sumFirstNnum(aNum))


def sumFirstNnum(num):
    if num <= 1:
        return num
    return sumFirstNnum(num-1) + num 

if __name__ == '__main__':
    main()