def main():
    N = int(input("Enter the number of fibb: "))
    if N <= 0:
        return
    elif N == 1:
        print(0)
    elif N == 2:
        print(0,1)
    else:
        fibb(N,0,1)
    pass

def fibb(N,i,j):
    if N <= 0:
        return
    print(i, end=" ")
    return fibb(N-1,j,i+j)

if __name__ == '__main__':
    main()
    