def main():
    aNum = int(input("Enter a number : "))
    print(sumNum(aNum))

def sumNum(num):
    if num <= 0:
        return num
    return num%10 + sumNum(num//10)

if __name__ == "__main__":
    main()
