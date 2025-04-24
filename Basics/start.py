country = input("Which country are you from? (ind - india): ")
if country == "ind":
    age = int(input("Enter your age: "))
    if  0 < age < 18:
        print("You are not elegible to vote")
    elif age > 100:
        print("You are not elegible to vote")
    elif age >= 18:
        print("You are elegible to vote!")
    else:
        print("Are you mad!")
else:
    print("Foriner!")
