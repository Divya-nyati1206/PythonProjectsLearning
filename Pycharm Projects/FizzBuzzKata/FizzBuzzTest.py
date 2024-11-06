import pytest

def FizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return (value%mod == 0)

def checkFizzBuzz( value, expectedReturn):
    retValue = FizzBuzz(value)
    assert retValue == expectedReturn


def test_with1PassedIn():
    checkFizzBuzz(1, "1")

def test_with2PassedIn():
    checkFizzBuzz(2, "2")

def test_with3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_with5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_with6PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_with10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_with15PassesdIn():
    checkFizzBuzz(15, "FizzBuzz")