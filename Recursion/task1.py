# For Output : 4 3 2 1 1 2 3 4
def func(n):
    if n <= 0:
        return
    print(n)
    func(n - 1)
    print(n)

func(4)