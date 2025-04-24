# Membershit operator
# in, not in
# ball not in box of balls - False
# ball in ball - error makes no sense


s1 = "0000"
print("0" in s1)
print('1' in s1)
l1 = [10, 20, [10,20]]
print(10 in l1)
print([10] in l1)
print([10,20] in l1)
a = 10
# print(10 in a) # error because ball in ball dosen't make sense
b = "10"
print("10" in b) # for string it works because string is an itterable object
c = '1'
# print(1 in c) # error
# print(10 in 10,20,30,40) # error in print statement