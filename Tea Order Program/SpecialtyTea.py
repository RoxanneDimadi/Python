from Tea import *

class SpecialtyTea(Tea):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.getSize() == "S":
            self.setPrice(12.00)
        elif self.getSize() == "M":
            self.setPrice(16.00)
        elif self.getSize() == "L":
            self.setPrice(20.00)

    def getTeaDetails(self):
        return "SPECIALTY TEA\nSize: {}\nName: {}\nPrice: ${:0.2f}\n"\
    .format(self.size, self.name, self.getPrice())

