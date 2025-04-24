def main():
    num = int(input("Enter the number: "))
    if isArmstrong(num, 0, original = num, N = len(num,0)):
        print("Is an Armstrong number!")
    else:
        print("Nope")

def len(num, count):
    if not num:
        return count
    return len(num//10,count+1)

def isArmstrong(aNum, result, original, N):
    if not aNum:
        return result == original
    a = aNum%10
    return isArmstrong(aNum//10, result + a**N, original, N)

if __name__ == '__main__':
    main()

# <><><><>