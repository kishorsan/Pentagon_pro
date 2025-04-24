def middle3(aStr):
    n = len(aStr)
    if n%2 == 0:
        print("Even length, no middle three")
    elif n < 3:
        print("Length of the string should be minimum 3!")
    else:
        start = n//2 - 1
        end = n//2 + 2
        print(aStr[start:end])
    
if __name__ == '__main__':
    stri = input("Enter a string: ")
    middle3(stri)

    