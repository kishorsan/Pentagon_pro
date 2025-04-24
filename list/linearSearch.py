lst = list(map(int, input("Enter a list: ").split()))
target = int(input("Enter the target to be found: "))
flag = False
index = -1

for i in range(len(lst)):
    if lst[i] == target:
        flag = True
        index = i
        break

if flag:
    print(f"Target {target} found at index {index}")
else:
    print("Target element not found")

