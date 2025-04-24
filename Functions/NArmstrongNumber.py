def main():
    aNum = int(input("Enter a number: "))
    count = 1
    i = 0
    while count <= aNum:
        if isArmstrong(i):
            print(f"{i:<10}:")
            count += 1
        i += 1

def len(num,count):
    if num <= 0:
        return count
    return len(num//10,count+1)

def isArmstrong(num):
    if num < 0:
        return
    original = num
    pow = len(num,0)
    result = 0
    while num:
        result += (num%10)**pow
        num//= 10
    return result == original


if __name__ == '__main__':
    main()