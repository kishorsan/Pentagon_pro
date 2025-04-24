def printNum(n):
    if n > 4:
        return
    print(n, end=" ")
    return printNum(n+1)

printNum(1)

# i = 0
# while True:
#     print("Hi", i)
#     i += 100
