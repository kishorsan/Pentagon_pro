def isPrime(num):
    if num <= 1:
        return
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return
    return True

aNum = int(input("Enter a number: ")) 
if isPrime(aNum):
    print("The number is a prime")
else:
    print("Nope")




# [2,3,4,5,6,7,8,9,11]