class Car:
    def __init__(self, carModel, rentalPrice):
        self.carModel = carModel
        self.rentalPrice = rentalPrice
        self.isAvailable = False
        print("The car model is:",self.carModel)
        print("The car rental Price is: ",self.rentalPrice)

    def rentCar(self):
        if self.isAvailable:
            self.carModel = input("Enter the car model: ")
            self.rentalPrice = input("Enter the car Price: ")
            print("The Car has been rented")
            self.isAvailable = False
        else:
            print("Sorry the car is not available!")

    def returnCar(self):
        print("The Car has been returned!")
        self.isAvailable = True


cModel = input("Enter the car model: ")
cPrice = input("Enter the car price: ")
c1 = Car(cModel, cPrice)
while True:
    op = input("Rent - 1\nReturn - 2\nExit - 3\nEnter the option: ")
    if (op == "1"):
        c1.rentCar()
    elif (op == "2"):
        c1.returnCar()
    elif (op == "3"):
        break