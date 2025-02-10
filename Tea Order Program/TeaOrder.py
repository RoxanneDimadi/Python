from SpecialtyTea import *
from CustomTea import *
from Tea import *

class TeaOrder:
    def __init__(self, distance):
        #SpecialtyTea.__init__(self, size, name)
        #CustomTea.__init__(self,size,base)
        self.teas = []
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def addTea(self, tea):
        self.teas.append(tea)

    def getOrderDescription(self):
        s = "******\n" \
            "Shipping Distance: {} miles\n".format(self.distance)
        total_price = 0.0

        for tea in self.teas:
            s += tea.getTeaDetails() + "\n"
            s += "----" + "\n"
            total_price += tea.getPrice()
        #s += tea.getTeaDetails(self) + "\n"
        s += "TOTAL ORDER PRICE: ${:0.2f}\n".format(total_price)
        s += "******\n"

        return s


