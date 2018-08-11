import sys

from simpleTranslations import *
from biggerNumbers import *
from grammaticalDetails import *

from error_checking.assertions import integerAssert
#from errorHandling import debugHelper1

def message():
    print "(The Roman numerals indicate the corresponding Chinese tones of pronunciation of the words.)\n"


def secondDigit(num):
    this = globals()[sys._getframe().f_code.co_name]
    integerAssert(num, this)

    if num < 0:
        num = -num

    while num >= 100:
        num = num/10
    return (num % 10)


def translateNumber(num):
    this = globals()[sys._getframe().f_code.co_name]
    integerAssert(num, this)

    translation = ""

    if num < 0:
        translation = minusSignWord + " " + translateNumber(-num)

    elif num in basicNumbers.keys():
        translation = basicNumbers[num]

    elif num >= 11 and num < 20:
        t10 = basicNumbers[10]
        t1 = translateNumber(num%10)
        translation = t10 + " " + t1

    elif num < 100:
        t10 = translateNumber(num/10) + " "+ basicNumbers[10]
        t1 = translateNumber(num%10)

        translation = t10 + " " + t1
        if t1 == basicNumbers[0]:
            translation = t10

    elif num < 1000:
        t100 = translateNumber(num/100) + " " + biggerNumbers[100]
        if (num/100) == 2:
            t100 = synonyms[2] + " " + biggerNumbers[100]

        rest = translateNumber(num%100)

        translation = t100 + " " + rest
	if rest == basicNumbers[0]:
            translation = t100

        elif secondDigit(num) == 0:
            translation = t100 + zeroConjunction + rest

    elif num < Wan:
        t1000 = translateNumber(num/1000) + " " + biggerNumbers[1000]
        rest = translateNumber(num%1000)

        translation = t1000 + " " + rest 
        if rest == basicNumbers[0]:
            translation = t1000

        elif secondDigit(num) == 0:
            translation = t1000 + zeroConjunction + rest 

    elif num < Yi4:
        tWan = translateNumber(num/Wan) + " " + biggerNumbers[Wan]
        rest = translateNumber(num % Wan)

        translation = tWan + " " + rest
        if rest == basicNumbers[0]:
            translation = tWan

        elif secondDigit(num) == 0:
            translation = tWan + zeroConjunction + rest

    else:
        tYi4 = translateNumber(num/Yi4) + " " + biggerNumbers[Yi4]
        rest = translateNumber(num % Yi4)

        translation = tYi4 + " " + rest
        if rest == basicNumbers[0]:
            translation = tYi4

        elif secondDigit(num) == 0:
            translation = tYi4 + zeroConjunction + rest

    return translation        
