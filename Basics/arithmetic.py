def plus():
    print(1+3+5+7+9)
    print(+9)
    print(9.8+8.0+7.7+6.8+9.9)
    print(+0)
    print(0.0009+9)
    print(+0.9)
    print(10+9999+0.0987)

def diff():
    print(100-9)
    print(9-9-9-9)
    print(0.99-0.99-0.88-0.005)
    print(-0.98)
    print(-10000)
    print(-987)
    print(0-0-0.9)
    print(8-0)
    print(0-0-0-0-0-0-0-0-0-0-0.0)
    print(9-9-9-9-9-9-0.99)
    print(-0)

def mul():
    print(8*7*6*20)
    print(8.9*0.9*6)
    try:
        print(*8)
    except TypeError:
        print("TypeError")
    
    #String Opertations
    print("abc" * 7) 
    print("Hello " * 8)
    print( " op " * 9)

def power(): #exponentiation
    print(2**3)
    print(3**2)
    print(9**0)
    print(100**7)
    print(8**4)
    print(1.3**3.2)

def floordiv():
    print(9//3)
    print(8//2)
    print(1000//46)
    print(89//4)
    print(77//3)

def div():
    print(9/3)
    print(8/3)
    print(22/7)
    print(9.89/3)
    print(89/4)
    print(783/34)
    print(7/9)

def mod():
    print(8%3)
    print(9%3)
    print(100%9)
    print(89%2)
    print(77%4)
    print(99%23)
    print(8902%124)
    pass

if __name__ == '__main__':
    op = input()
    if op == '+':
        plus()
    if op == '-':
        diff()
    if op == '*':
        mul()
    if op == '**':
        power()
    if op == '//':
        floordiv()
    if op == '/':
        div()
    if op == '%':
        mod()
    pass