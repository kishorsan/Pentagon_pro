# WAP to print all the even numbers and odd numbers of a custamized range seperately

def main():
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    print("Even    Odd")
    for i in range(start, end + 1):
        if EvenOdd(i):
            print(i, end='\t')
        else:
            print(i)
    print()
    # for i in range(start, end + 1):
    #     if not EvenOdd(i):
    #         print(i, end=' ')

def EvenOdd(num):
    return num%2 == 0

main()
