def findDigits(n):
    # Write your code here
    print(n)
    count = 0
    d = 0
    temp = n
    while temp > 0:
        d = temp%10
        if d != 0 and n%d == 0:
            count += 1
        temp = temp // 10
    return count

if __name__ == '__main__':
    IP_PATH = 'list\online\ip.txt'
    fptr = open(IP_PATH, 'r')
    data = fptr.readline()
    for i in range(1,int(data)+1):
        data = fptr.readline()
        # print("%s" % data)
        result = findDigits(int(data))
        print(result)