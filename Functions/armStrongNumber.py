def main():
    aNum = int(input("Enter a number: "))
    if isArmstrong(aNum):
        print("Is an Armstrong!")
    else:
        print("Is not an Armstrong!")

def len(num):
    count = 0
    if not num:
        return 1
    while num:
        num //= 10
        count += 1
    return count

def isArmstrong(num):
    original = num
    if num < 0:
        num *= (-1)
    pow = len(num)
    result = 0
    while num:
        result += (num%10)**pow
        num//= 10
    return result == original

if __name__ == '__main__':
    main()
