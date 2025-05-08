def print_rangoli(n):
    sor = scr = n 
    for i in range(1, n*2):
        soc = n
        for j in range(1, n*2):
            if j >= sor and j < n+1:
                soc -= 1
                print(chr(97+soc), end='')
            elif j <= scr and j > sor:
                soc += 1
                print(chr(97+soc), end='')
            else:
                print('-', end='')
            print('-' if j < n*2-1 else '',end='')
        if i < n:
            sor -= 1
            scr += 1
        else:
            sor += 1
            scr -= 1
        print()
        # if i < n:
        #     scr += 1
        # else:
        #     scr -= 1
        

print_rangoli(5)