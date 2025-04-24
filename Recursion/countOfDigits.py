def count(n, i):
    if n <= 0:
        return i
    i += 1
    return count(n//10, i)

n = int(input("Enter a number: "))
len = count(n, 0)
print(len)