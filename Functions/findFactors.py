def main(num): # unreliable and takes too much time
    lst = []
    for i in range(1, num+1):
        x = num%i
        if x == 0:
            lst.append(i)
    return lst

def fact2(num):
    i = 1
    count = 0
    while i*i <= num:
        if num%i == 0:
            print(i, end=' ')
            count += 1
            if i == num//i:
                break
            count += 1
            print(num//i, end=' ')
        i += 1
    return count

if __name__ == '__main__':
    n = int(input("Enter a Number: "))
    num1 = main(n)
    fact2(n)
    