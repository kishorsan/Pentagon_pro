print("**************************")
print("******Welcome to VRL******")
print("**************************")

print("Enter you prime locatio from India")
print("Select the options given below")
location = int(input("1. Local\n2. Regional\n3. National\n4. International\n"))
if location == 1:
    print("Your package will be delivered in a day!")
elif location == 2:
    print("Your package will be delivered in two days!")
elif location == 3:
    print("Your package will be deliverd in five days!")
elif location == 4:
    print("Your package will be delivered in a weeks time!")
else:
    print("We cannot send the package to your loaction!")

print("If there is any problem with the package contact our customer care\n at 123-456-7890")

print("*******************************************")
print("********Thank You for choosing us**********")
