from lab06 import *
from Apartment import Apartment
#apartment class
def test_getRent():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getRent() == 1204

def test_getMetersFromUCSB():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getMetersFromUCSB() == 200

def test_getCondition():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getCondition() == "bad"

def test_getApartmentDetails():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"

def test__lt__():
# rent first, metersfromUCSB second, lastly condition
    a0 = Apartment(1204, 200, "bad")
    a1 = Apartment(1300, 200, "bad")
    assert a0 < a1
    a2 = Apartment(1300, 400, "bad")
    assert a1 < a2
    a3 = Apartment(1300, 400, "excellent")
    assert a3 < a2
    a4 = Apartment(1300, 400, "average")
    assert a3 < a2
    assert a3 < a4
    assert a4 < a2
    assert (a2 < a3) == False
    assert (a4 < a3) == False
    assert (a2 < a4) == False

def test__gt__():
    a0 = Apartment(1204, 200, "bad")
    a1 = Apartment(1300, 200, "bad")
    a2 = Apartment(1300, 400, "bad")
    a3 = Apartment(1300, 400, "excellent")
    a4 = Apartment(1300, 400, "average")
    assert a2 > a1
    assert a1 > a0
    assert a2 > a3
    assert a2 > a3
    assert a2 > a4

def test__eq__():
    a5 = Apartment(1204, 200, "bad")
    a6 = Apartment(1204, 200, "bad")
    assert a5 == a6


#lab06

def test_ensureSortedAscending():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getBestApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"

def test_getWorstApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

def test_getAffordableApartments():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getAffordableApartments(apartmentList, 950) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n\
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"


