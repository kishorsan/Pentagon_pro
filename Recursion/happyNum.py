def main():
    num = int(input("Enter a numbe : "))
    flag = isHappy(num)
    if flag:
        print("Is a happy number!")
    else:
        print("Is not a happy number!")

def isHappy(n):
    if n == 1:
        return True
    elif n == 4:
        return False
    sum = 0
    while n > 0:
        base = n%10
        sum = sum + base**2
        n = n//10
    return isHappy(sum) 


if __name__ == '__main__':
    main()