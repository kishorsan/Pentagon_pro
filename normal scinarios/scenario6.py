import time

print("Welcome to the Pentagon Theme Park")
print("**********************************")
age = int(input("Enter the age of the visitor: "))
if 120 < age or age < 0:
    print("Nice joke") 
else:
    party = int(input("1. In a Group\n2. Not in a group\n"))
    if age < 12:
        if party == 1:
            print("You got a free entry !!")
        else:
            fair = 10
            print("The ticket will be 10$")
    elif 12 <= age < 63:
        if party == 1:
            fair = 20
            print("You will get a 20% discount !!")
            time.sleep(1.3)
            print(f"Your disounted price is {fair*(100-20)/100}$")
        else:
            print("The ticket will be 20$")
    else:
        print("You are not allowed to enter due to accident conserns")

