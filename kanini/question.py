def main(num):
    i = 2
    start = 800
    fresult = 0 # count containing the num of elements having 1 in begining
    return convertable(num, start, i, fresult, 0)

def convertable(num, start, i, result, a):
    a = sumNum(start, 0)
    if start + i >= num:
        print(a)
        return result + oneInplace(a)
    print(a, end=' ')
    return convertable(num, start + i, i + 2, result + oneInplace(a), a)

def oneInplace(num):
    if num//10 == 1:
        return 1
    else:
        return 0

def sumNum(num, result):
    if not num:
        return result
    return sumNum(num//10, result + num%10)

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    result = main(num)
    print(result)
