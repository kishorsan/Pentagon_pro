import time
while True:
    print("***************************")
    card = int(input("Insert Card - 1\nExit - 2\n"))
    if card == 1:  
        balance, amount =  map(int,input("Enter the current balance and withdrawal amount after a space: ").split())
        print(balance<=amount)
        print(amount)
        if balance >= amount:
            balance -= amount
            time.sleep(1.5)
            print(f"You have withdrawn {amount} \n***************************\nYour current balance is {balance}")
        else:
            print("Insufficient Funds")
    elif card == 2:
        break
    else:
        print("Enter a valid Input")