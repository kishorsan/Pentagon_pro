list1 = [1,2,3,4,5]

l1 = iter(list1)

print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))

def get_out(num):
    for i in range(1,num):
        yield i*2

out = get_out(10)
print(next(out))
print(next(out))
print(next(out))
print(next(out))