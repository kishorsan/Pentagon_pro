import time
print("****************************************")
print("*  Welcome to the Grand Travel Agency  *")
print("****************************************")
type = int(input("Select your destination type:\nInternational - 1\nDomestic - 2\n"))
if type == 1:
    ticket = int(input("Select the type of ticket\nFirst class - 1\nEconomy - 2\n"))
    if ticket == 1:
        fair = 45000
        print("You will get a 15% discount")
        print(f"The actual fair is {fair}")
        time.sleep(1.3)
        print(f"Your discounted price will be {fair * ((100-15)/100)}")
    elif ticket == 2:
        fair = 20000
        print("You will get a 10% discount")
        print(f"The actual fair is {fair}")
        time.sleep(1.3)
        print(f"Your discounted price will be {fair * ((100-10)/100)}")
    else:
        print("No such class is availbale")

elif type == 2:
    ticket = int(input("Select the type of ticket\nFirst class - 1\nEconomy - 2\n"))
    if ticket == 1:
        fair = 12000
        print("You will get a 5% discount")
        print(f"The actual fair is {fair}")
        time.sleep(1.3)
        print(f"Your discounted price will be {fair * (100-5)/100}")
    elif ticket == 2:
        print("You will get No discount")
    else:
        print("No such class is availbale")
else:
    print("Invalid option!\nVisit Next time to ulock this option!!")
time.sleep(1.5)

print("################################################")
print("#  Thank you for choosing Grand Travel Agency  #")
print("################################################")