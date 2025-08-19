import random 

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked from {fro} to {to} on train {self.trainNo}")

    def getStatus(self):
        print(f"Status for train {self.trainNo} is: On Time")

    def getFare(self, fro, to):
        print(f"Fare for {fro} to {to} on train {self.trainNo} is {random.randint(100, 5000)}")

A = Train(12345)
A.book("Mumbai", "Delhi")
A.getStatus()
A.getFare("Mumbai", "Delhi")