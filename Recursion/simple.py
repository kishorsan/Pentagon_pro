def disp1(n):
    print(n)
    return disp2(n+1)

def disp2(n):
    print(n)
    return disp3(n+1)

def disp3(n):
    print(n)
    return disp4(n+1)

def disp4(n):
    print(n)
    return 

disp1(1)

