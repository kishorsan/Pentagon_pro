def isprime(num):
    if num <= 1:
        return
    i = 2
    while i*i <= num:
        if num%i == 0:
            return 
        i+=1
    return True



if __name__ == '__main__':
    num = int(input("Enter a number: "))
    result = isprime(num)
    print("Is Prime" if result else "Not prime")