def main(num):
    lst1 = []
    lst2 = []
    i = 1
    j = 0
    if num < 1:
        return "Invalid Input!!", "Not Valid"
    print("Prime Numbers : ")
    while j < num:
        flag = prime(i, 0, 1)
        if flag:
            print(i, end=" ")
        i += 1
        j += 1

    i = 1
    j = 0
    print("\nNon prime Numbers : ")
    while j < num:
        flag = prime(i, 0, 1)
        if not flag:
            print(i, end=" ")
        i += 1
        j += 1
    # return lst1,lst2

# def prime(num):
#     if num < 1:
#         return
#     i = 1
#     count = 0
#     while i * i <= num:
#         if num%i == 0:
#             count += 1
#             if num//i == i:
#                 break
#             count += 1
#         i += 1
#     return count == 2

def prime(num, result, i):
    if num == 1:
        return False
    if i * i > num or result > 2:
        return result == 2
    return prime(num, result + 2 if num % i == 0 else result, i+1)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    main(n)
    # print(f"Prime numbers are: {plst}")
    # print(f"Non Prime numbers are: {nplst}")


