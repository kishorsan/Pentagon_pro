def main(num):
    i = 0
    lst = []
    count = 0
    if num < 1:
        return "Invalid Input!!"
    while count < num:
        i += 1
        if isPrime(i):
            lst.append(i)
            count += 1
    return lst

def isPrime(num):
    if num <= 1:
        return
    i = 2
    while i * i <= num:
        if num % i == 0:
            return
        i += 1
    return True 

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    plist = main(n)
    print(plist)
    