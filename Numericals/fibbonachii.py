def main():
    N = int(input("Enter a value : "))
    i = 0
    j = 1
    while N > 0:
        print(i, end= ' ')
        j = i + j
        i = j - i
        N -= 1        

main()