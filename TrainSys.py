class Train:

    def __init__(self):
        self.seats=78
        self.fare=190

    def bookTick(self):
        self.seats -=1

    def getStat(self):
        print(self.seats)

    def getFare(self):
        print(self.fare)

tr=Train()
tr.getFare()
tr.getStat()
tr.bookTick()
tr.bookTick()
tr.bookTick()
tr.getStat()