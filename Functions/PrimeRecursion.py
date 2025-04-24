def main():
    num = int(input("Enter a number: "))
    result = prime(num, 0, 1)
    print(result)

def prime(num, result, i):
    if i > num or result > 2:
        return result == 2
    return prime(num, result + 1 if num % i == 0 else result, i+1)

main()