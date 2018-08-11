import sys

from simpleTranslations import *
from biggerNumbers import *
from grammaticalDetails import *

from error_checking.assertions import integerAssert
#from errorHandling import debugHelper1

def message():
    print

def translateSmallNumber(num):
    this = globals()[sys._getframe().f_code.co_name]
    maxLimit = Lakh
    translation = ""

    integerAssert(num, this)

    if num < 0:
        if num > -maxLimit:
            translation = minusSignWord + " " + translateSmallNumber(-num)

    elif num in basicNumbers.keys():
       translation = basicNumbers[num]

    elif num < 100:
        t10 = tens[num/10]
        t1 = basicNumbers[num%10]
        
        translation = t10 + " " + t1
        if t1 == basicNumbers[0]:
            translation = t10 

    elif num < 1000:
        t100 = basicNumbers[num/100] + " " + biggerNumbers[100]
        rest = translateSmallNumber(num%100)

        translation = t100 + andConjunction + rest
        if rest == basicNumbers[0]:
            translation = t100

    elif num < Lakh:
        t1000 = translateSmallNumber(num/1000) + " " + biggerNumbers[1000]
        rest = translateSmallNumber(num%1000)

	translation = t1000 + " " + rest
        if rest == basicNumbers[0]:
            translation = t1000

        elif (num%1000) < 100:
            translation = t1000 + andConjunction + rest

    return translation


def translateNumIndian(num):
    this = globals()[sys._getframe().f_code.co_name]
    translation = ""

    integerAssert(num, this)

    if num > -Lakh and num < Lakh:
        return translateSmallNumber(num)

    elif num < 0:
        translation = minusSignWord + " " + translateNumIndian(-num)

    elif num < Crore:
        tLakh = translateSmallNumber(num/Lakh) + " " + biggerNumbers[Lakh]
        rest = translateSmallNumber(num % Lakh)

        translation = tLakh + " " + rest
        if rest == basicNumbers[0]:
            translation = tLakh
            if (num/Lakh) > 1:
                translation += pluralMarker

        elif (num % Lakh) < 100:
            translation = tLakh + andConjunction + rest

    else:
        tCrore = translateNumIndian(num/Crore) + " " + biggerNumbers[Crore]
        rest = translateNumIndian(num % Crore)

        translation = tCrore + " " + rest
        if rest == basicNumbers[0]:
            translation = tCrore
            if (num/Crore) > 1:
                translation += pluralMarker

        elif (num % Crore) < 100:
            translation = tCrore + andConjunction + rest

    return translation


def translateNumInternational(num):
    this = globals()[sys._getframe().f_code.co_name]
    translation = ""

    integerAssert(num, this)
    
    if num > -Lakh and num < Lakh:
        return translateSmallNumber(num)

    elif num < 0:
        translation = minusSignWord + " " + translateNumInternational(-num)

    elif num < Million:
        t1000 = translateSmallNumber(num/1000) + " " + biggerNumbers[1000]
        rest = translateSmallNumber(num%1000)

        translation = t1000 + " " + rest
        if rest == basicNumbers[0]:
            translation = t1000

        elif (num%1000) < 100:
            translation = t1000 + andConjunction + rest

    elif num < Billion:
        tMillion = translateSmallNumber(num/Million) + " " + biggerNumbers[Million]
        rest = translateNumInternational(num % Million)

        translation = tMillion + " " + rest
        if rest == basicNumbers[0]:
            translation = tMillion

        elif (num % Million) < 100:
            translation = tMillion + andConjunction + rest

    else:
        tBillion = translateNumInternational(num/Billion) + " " + biggerNumbers[Billion]
        rest = translateNumInternational(num % Billion)

        translation = tBillion + " " + rest
        if rest == basicNumbers[0]:
            translation = tBillion

        elif (num % Billion) < 100:
            translation = tBillion + andConjunction + rest

    return translation


def translateNumber(num):
    this = globals()[sys._getframe().f_code.co_name]
    integerAssert(num, this)

    if num > -Lakh and num < Lakh:
        return translateSmallNumber(num)
    
    else:
        system = raw_input("In which system do you want the number? Indian (H) or international (I)? ").lower()
        if system == 'h':
            return translateNumIndian(num)

        elif system == 'i':
            return translateNumInternational(num)

        else:
            print "Invalid input for number system.\n"
            return "error"
