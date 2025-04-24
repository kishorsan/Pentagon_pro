def main():
    pos = int(input("Enter the postion : "))
    out = fibb(pos)
    print(out)


def fibb(pos):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibb(pos - 2) + fibb(pos - 1)

if __name__ == '__main__':
    main()