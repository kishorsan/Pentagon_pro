def main():
    s = input("Enter a string: ")
    output = digitsSum3(s, i=0, N=len(s)+1, total=0, sum=0)
    print(output)
    
    aStr = input("Enter a string: ") + " "
    output2 = sumOfDigits(aStr)

def digitsSum(s, i, N, total):
    if i >= N:
        return total
    if '0' <= s[i] <= '9':
        total += ord(s[i]) - 48
    return digitsSum(s, i+1, N, total)

def digitsSum2(s, i, N, total):
    if i >= N:
        return total
    if (i+1 < N) and '0' <= s[i] <= '9' and '0' <= s[i+1] <= '9':
        total += (ord(s[i])-48)*10 + ord(s[i+1]) - 48 
        return digitsSum2(s, i+2, N, total)
    elif '0' <= s[i] <= '9':
        total += ord(s[i]) - 48
    return digitsSum2(s, i+1, N, total)

def digitsSum3(s, i, N, total, sum):
    if i >= N:
        return total
    if i+1 < N and '0' <= s[i] <= '9':
        sum = (sum*10) + ord(s[i]) - 48
    else:
        total += sum
        sum = 0
    return digitsSum3(s, i+1, N, total, sum)
    

def sumOfDigits(s):  # here we are adding an extra space to the input 
    sum1 = 0
    total = 0
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            sum1 = (sum1*10) + ord(s[i]) - 48
        elif sum1 != 0:
            total += sum1
            sum1 = 0
    return total

if __name__ == '__main__':
    main()