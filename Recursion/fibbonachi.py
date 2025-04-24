# WAP to print a fibbonachi series fill the defined position

def main():
    # num = int(input("Enter a numbe : "))
    pos = int(input("Enter which fibb u want ? - "))
    out = fibb(pos, 0, 1)
    print(f"{pos}th fibbonachi is {out} ")
    fibbo(0, 1, pos)
    # print(f"{pos} positions fibbonachi is {result}")
    pass


def fibb(pos, fi, se):  #Nth fibbonachi 
    
    if pos <= 1:
        return fi
    se, fi = fi + se, se
    return fibb(pos - 1, fi, se)
  
def fibbola(i, pos, fi, se):  #Nth fibbonachi with extra variable
    if pos <= 1:
        return fi
    se, fi = fi + se, se
    return fibb(i + 1, pos, fi, se)


def fibbo(i,j,pos): # all fibbonachi till Nth position 
    if pos <= 0:
        return
    print(i, end=' ')
    return fibbo(j, i + j, pos-1)
    pass


if __name__ == '__main__':
    main()