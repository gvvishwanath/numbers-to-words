import sys

from simpleTranslations import *
from biggerNumbers import *
from grammaticalDetails import *

from error_checking.assertions import integerAssert
#from errorHandling import debugHelper1

def message():
    print "(The capital letters, if any, indicate 'hard' sounds. 'ZH' is as in tamiZH.)\n" 


def translateNumber(num):
    this = globals()[sys._getframe().f_code.co_name]
    integerAssert(num, this)

    maxLimit = 1000
    translation = ""

    if num < 0:
        if num > -maxLimit:
            translation = minusSignWord + " " + translateNumber(-num)

    elif num in basicNumbers.keys():
        translation = basicNumbers[num]

    elif num >= 11 and num < 20:
        t10 = elevenToTwentyPrefixes(num%10)
        t1 = basicNumbers[num%10]
        translation = t10 + t1

    elif num < 100:
        t10 = decade[num/10]
        t1 = basicNumbers[num%10]

        translation = makePrefix(num, t10) + " " + t1
        if t1 == basicNumbers[0]:
            translation = t10

    elif num < 800:
        n100 = num/100
        t100 = ""
        rest = translateNumber(num%100)

        if n100 == 1:
            t100 = biggerNumbers[100]
        else:
            t100 = hundredPrefixes[n100] + biggerNumbers[100]

        translation = makePrefix(num, t100) + " "+ rest
        if rest == basicNumbers[0]:
            translation = t100

    elif num < 1000:
        t100 = biggerNumbers[100*(num/100)]
        rest = translateNumber(num%100)
       
        translation = makePrefix(num, t100) + " " + rest
        if rest == basicNumbers[0]:
            translation = t100

    elif num < Lakh:
        n1000 = num/1000
        t1000 = ""
        rest = translateNumber(num%1000)

        if n1000 == 1:
            t1000 = biggerNumbers[1000]
        else:
            t1000 = translateNumber(n1000)[:-1] + biggerNumbers[1000]

        translation = makePrefix(num, t1000) + " "+ rest
        if rest == basicNumbers[0]:
            translation = t1000

    return translation        
