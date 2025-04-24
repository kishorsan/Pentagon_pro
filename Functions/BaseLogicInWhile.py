# According to MAM 

def isevenOdd(num):
    return num%2 == 0

n = int(input("Enter a number: "))
count = 0
i = 1
while count < n:
    if isevenOdd(i):
        print(i)
        count += 1
    i += 1