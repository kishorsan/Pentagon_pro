'''
# simple if
n = int(input("Enter a number: "))
if n > 10:
    print(f"{n} is large")
print("Program executed")

# if else alternation 
n = int(input("Enter another n: "))
if n%2 == 0:
    print("Number is even")
else:
    print("Number is odd")
 
# elif introduction - elif lader
n = int(input("Enter another another number: "))
if n%2 == 0:
    print("Even!")
elif n%3 == 0:
    print("A multiple of 3!")
elif n%5 == 0:
    print("Majority of 5 multiples excpet some multiples of 3")
else:
    print("This will never be executed unless u know how to ")


'''

marks = int(input("Enter the marks you got: "))
if marks >= 90:
    print("Superstar Distinction!!")
elif(marks >= 75 and marks < 90):
    print("First rank, eeeh party!!!!")
elif(marks >= 60 and marks < 75):
    print("Your second class good grade !!!")
elif(marks >= 50 and marks < 60):
    print("Boiii you barely passed !!!")
else:
    if( marks < 0 ):
        print("dude your the worse")
    else:
        print("You failed")

if marks <= 100 and marks >= 90:
    print("S Grade")
elif marks < 90 and marks >= 80:
    print("A Grade")
elif marks < 80 and marks >= 70:
    print("B Grade")
elif marks < 70 and marks >= 60:
    print("C Grade")
elif marks < 60 and marks >= 50:
    print("D Grade")
elif (marks < 0) or (marks > 100):
    print("Invalid Input")
else:
    print("You failed!!!")

percentage = int(input("Enter your percentage: "))
if 0 > percentage > 100 :
    print("Invalid Input!")
else:
    if 100 >= percentage >= 85:
        print("Distinction!!")
    elif 85 > percentage >= 65:
        print("First class!")
    elif 65 > percentage >= 55:
        print("Second class!")
    elif 55 > percentage >= 35:
        print("Third class!")
    else:
        print("Better luck next time!")
    print("Work hard >>> Study Hard.....!")