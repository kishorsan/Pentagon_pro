def main():
    a = int(input("Enter a number : "))
    print(f"The factorial of {a} is {fact(a)}.")

def fact(num):
    try:
        if num <= 1:
            return 1
        return num * fact(num - 1)
    except:
        print("There is an error")


if __name__ == '__main__':
    main()
