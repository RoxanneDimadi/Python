# Apartment class
class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
            .format(self.rent, self.metersFromUCSB, self.condition)

    def __lt__(self, rhs):
        #true if Apartment 1 is better than Apartment2, Apartment1 < Apartment2
        #rent first, metersfromUCSB second, lastly condition
        if self.rent < rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == 'excellent' and rhs.condition != 'excellent':
                    return True
                elif self.condition == 'average' and rhs.condition == 'bad':
                    return True
                elif self.condition == 'bad' and rhs.condition != 'bad':
                    return False
                return False
        return False

    def __gt__(self, rhs):
        # True if Apartment2 is better than Apartment1, Apartment1 > Apartment2
        # rent first, meters from UCSB second, lastly condition
        if self.rent > rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == 'bad' and rhs.condition != 'bad':
                    return True
                elif self.condition == 'average' and rhs.condition == 'excellent':
                    return True
                elif self.condition == 'excellent' and rhs.condition != 'excellent':
                    return False
                return False
        return False

    def __eq__(self, rhs):
        # True if Apartment1 is equal to Apartment2 for all attributes
        # rent, meters from UCSB, and condition must be the same
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == rhs.condition:
                    return True
                return False
            return False
        return False
