#testFile
#import pytest

from lab_03 import integerDivision
from lab_03 import collectEvenInts
from lab_03 import countVowels
from lab_03 import reverseString
from lab_03 import removeSubString

def test_integerDivision():
    assert integerDivision(27, 4) == 6
    assert integerDivision(4, 27) == 0
    assert integerDivision(4, 4) == 1
    assert integerDivision(15, 2) == 7


def test_collectEvenInts():
    assert collectEvenInts([1, 2, 3, 4, 5]) == [2, 4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([2, 2, 2, 3, 5, 7, 10, 11, 12]) == [2, 2, 2, 10, 12]
    assert collectEvenInts([3, 5, 7]) == []

def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("tHIs Is a StrIIiing") == 7
    assert countVowels("bcdf") == 0
    assert countVowels("") == 0

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("Hello") == "olleH"
    assert reverseString("") == ""
    assert reverseString("123aBc") == "cBa321"
    assert reverseString("a") == "a"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("hihellohihello", "hi") == "hellohello"
    assert removeSubString("1010", "1") == "00"
    assert removeSubString("thistookmesolong", "me") == "thistooksolong"



