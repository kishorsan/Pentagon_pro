# For loops can be used inside while loops if and only if certain conditions are satisfied
# If not the loop will be executed endlessly
'''
j = 0
while True:
    for i in range(5):
        if i == 5:
            break
        print(i)
    j += 1
    if j == 3:
        break

# The dependency of execution depends on where the break statement is
print("Execution finished\n\n")

k = 1
while k:
    k -= 1
    print("Anything works!!!")
    print("Except for 0 and False in while condition")
    break
print()
l = 1
while l==1:
    print("And hard coding also works!!!\n",
          "Untill it dosen't\n")
    l = 2

'''

# WHILE #
#--> While Loop is entry-controlled and once the execution enters the loop, the exit it dependent on the loop logic
i = 0
while i < 10: # Here the control is is the value of i
    i += 2
    print(":(){:|:};:")


#--> While Loop does not follow iterative based approaach but it can be used as one!
i = 0
lst = [1,2,3,4,5,6,9,3,10]
while i < len(lst):
    print(lst[i], end=' ')
    i += 1
print("\n Program executed!!")


#--> While Loop helps with infinetly executing a set of logic untill a condition is met

i = 1
temp = "Kishor"
def main(aStr):
    global i
    return aStr[i:]

while True:
    print(temp)
    temp = main(temp)
    if temp == '':
        break
