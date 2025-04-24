def main(N,M):
    if N > M:
        raise ValueError("Invalid Input!!")
    lst = []
    while N <= M:
        if isPrime(N):
            lst.append(N)
        N += 1
    return lst

def isPrime(num):
    if num <= 1:
        return 
    i = 2
    while i * i <= num:
        if num%i == 0:
            return
        i += 1
    return True


if __name__ == '__main__':
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    try:
        result = main(x,y)
        print(result)
    except ValueError:
        print("Invalid Input!!")