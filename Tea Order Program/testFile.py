import pytest

# CustomTea
from CustomTea import *


def test_getTeaDetails():
    cp1 = CustomTea("S", "Oolong")
    assert cp1.getTeaDetails() == \
"CUSTOM TEA\n\
Size: S\n\
Base: Oolong\n\
Flavors:\n\
Price: $10.00\n"

cp1 = CustomTea("L", "Green")
cp1.addFlavor("peach")
cp1.addFlavor("jasmine")

assert cp1.getTeaDetails() == \
"CUSTOM TEA\n\
Size: L\n\
Base: Green\n\
Flavors:\n\
\t+ peach\n\
\t+ jasmine\n\
Price: $21.50\n"

#Specialty Tea Class
from SpecialtyTea import *
def test_getSpecialtyTeaDetails():
    sp1 = SpecialtyTea("S", "Earl Grey")

    assert sp1.getTeaDetails() == \
"SPECIALTY TEA\n\
Size: S\n\
Name: Earl Grey\n\
Price: $12.00\n"

#Tea Order Class

from TeaOrder import *
def test_getOrderDescription():
	ct1 = CustomTea("S", "Black")
	ct1.addFlavor("rose")
	ct1.addFlavor("cardamom")
	st1 = SpecialtyTea("M", "Matcha")
	order = TeaOrder(400)  # shipping distance: 400 miles
	order.addTea(ct1)
	order.addTea(st1)
	assert order.getOrderDescription() == \
"******\n\
Shipping Distance: 400 miles\n\
CUSTOM TEA\n\
Size: S\n\
Base: Black\n\
Flavors:\n\
\t+ rose\n\
\t+ cardamom\n\
Price: $10.50\n\
\n\
----\n\
SPECIALTY TEA\n\
Size: M\n\
Name: Matcha\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.50\n\
******\n"

# test orderqueue
from OrderQueue import OrderQueue
def test_OrderQueue():
	queue = OrderQueue()
	tea_order1 = TeaOrder(100)
	tea_order2 = TeaOrder(300)
	tea_order3 = TeaOrder(200)
	queue.addOrder(tea_order1)
	queue.addOrder(tea_order2)
	queue.addOrder(tea_order3)

	assert queue.processNextOrder() == tea_order2.getOrderDescription()
	assert queue.processNextOrder() == tea_order3.getOrderDescription()
	assert queue.processNextOrder() == tea_order1.getOrderDescription()

