def len(num):
    count = 0
    if not num:
        return 1
    while num>0:
        num = num//10
        count += 1
    return count

def len1(num,count):
    if not num:
        return count
    return len1(num//10,count+1)

def pos(num):
    return num * (-1)

def main(len):
    num = int(input("Enter a number: "))
    if num < 0:
        num = pos(num)
    length = (lambda num, count=0: 1 if num == 0 == count else count if num == 0 else length(num // 10, count + 1))
    print(len(num))
    print("Length of the number:", length(num))
    print(len1(num,0))

main(len)

