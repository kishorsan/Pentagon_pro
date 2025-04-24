# WAP to print a fibbonachi series fill the defined position

def main():
    # num = int(input("Enter a numbe : "))
    pos = int(input("Enter which fibb u want ? - "))
    out = fibb(0, pos-1, 0, 1)
    print(f"{pos}th fibbonachi is {out} ")
    fibbo(0, 1, pos)
    # print(f"{pos} positions fibbonachi is {result}")
    pass


def fibb(i, pos, fi, se):  #Nth fibbonachi 
    if pos == i:
        return fi
    se = fi + se
    fi = se - fi
    return fibb(i+1, pos, fi, se)



def fibbo(i,j,pos): # all fibbonachi till Nth position 
    if pos <= 0:
        return
    print(i, end=' ')
    return fibbo(j, i + j, pos-1)
    pass


if __name__ == '__main__':
    main()