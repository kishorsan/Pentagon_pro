def main():
    n = int(input("Enter the number: "))
    flag = EvenOrOdd(n)
    # if result:
    #     print(f"{n} is Even")
    # else:
    #     print(f"{n} is Odd")
    print(f"{n}" , "is Even" if flag else "is Odd")

    # Re-using the same Function to do more 
    # Printing even number from start to end !!
    start = int(input("Enter the start number: "))
    end = int(input("Enter your end number: "))
    for i in range(start, end + 1):
        if EvenOrOdd(i):
            print(i, end=' ')



def EvenOrOdd(num):
    return num%2 == 0


''' The above method is even easier to return True or False
    if num%2 == 0:
        return True
    return False
'''

if __name__ == '__main__':
    main()