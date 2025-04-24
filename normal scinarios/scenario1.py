a = 1
while a:
    userState = int(input("Is she : Online - '1' \t or Offline - '2' \n "))

    if userState == 1:
        tickStat = int(input("Tick status is \nGrey - 1\nBlue - 2\n"))
        if tickStat == 1:
            print("Your being ignored")
        elif tickStat == 2:
            print("seen your message")
        else:
            print("Enter either '1' or '2' ")
    elif userState == 2:
        print("Message sent")
    else:
        print("Calling is better than texting")
        a = 0
