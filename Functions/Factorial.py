def main():
    num = int(input("Enter a number: "))
    try:
        if num > 0:
            val = fact(num, 1)
        return val
    except:
        return "Invalid Input!!"

def fact(num, result):
    if num == 1:
        return result
    return fact(num-1, result * num)


if __name__ == '__main__':
    result = main()
    print(result)