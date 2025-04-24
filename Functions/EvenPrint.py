
def main():
    start = int(input("Enter your start number: "))
    end = int(input("Enter the end number: "))
    if start > end:
        print("Invalid Input")
    else:
        for i in range(start, end + 1):
            if pEven(i):
                print(i,end=' ')


def pEven(num):
    return num%2 == 0


'''
def printEven(num):
    for i in range(num+1):
        print(i if i%2 == 0 else ' ',end='')
'''




if __name__ == '__main__':
    main()
