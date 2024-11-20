#lab03
def integerDivision(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    
    return 1 + integerDivision(n - k, k)
#return n * factorial(n-1)

# assert integerDivision(27,4) == 6

def collectEvenInts(listOfInt):
    if len(listOfInt) == 0:
        return []
    if listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    else:
        return collectEvenInts(listOfInt[1:])
    
def countVowels(someString):
    if len(someString) == 0:
        return 0
    if someString[0] == 'A' or someString[0] == 'E' or someString[0] == 'I' or someString[0] == 'O' or someString[0] == 'U' or \
        someString[0] == 'a' or someString[0] == 'e' or someString[0] == 'i' or someString[0] == 'o' or someString[0] == 'u':
        return 1 + countVowels(someString[1:])
    else:
        return countVowels(someString[1:])


def reverseString(s):
    if len(s) == 0 or len(s) == 1:
        return s
    return s[-1] + reverseString(s[:-1])


def removeSubString(s, sub):
    if sub not in s:
        return s
    if s[:len(sub)] == sub:
        return removeSubString(s[len(sub):], sub)
    return s[0] + removeSubString(s[1:], sub)



