import sys

from languagesList import getUserChoice
from error_checking.errorHandling import displayError
from error_checking.assertions import integerAssert, stringAssert

translator = getUserChoice()

def displayTranslation(num, string):
    this = globals()[sys._getframe().f_code.co_name]

    try:
        integerAssert(num, this)
        stringAssert(string, this)

        print "In words, %d is %s." % (num, string)

    except Exception as e:
        displayError(this.__name__, e)


def displayFailure(num):
    this = globals()[sys._getframe().f_code.co_name]

    try:
        integerAssert(num, this)

        print "Sorry! We haven't added the logic to translate %d yet!\n" % num
    
    except Exception as e:
        displayError(this.__name__, e)


def translateInput():
    this = globals()[sys._getframe().f_code.co_name]

    try:
	num = int(raw_input("Enter an integer : "))
        translation = translator.translateNumber(num)

        if translation != "" and translation != "error":
            displayTranslation(num, translation)
            translator.message()  

        elif translation == "":
            displayFailure(num)

    except Exception as e:
        displayError(this.__name__, e)


def mainProg():
    this = globals()[sys._getframe().f_code.co_name]

    try:
    	flag = 'y'
    	while(flag == 'y'):
            translateInput()
            flag = raw_input("Do you want to continue? (y/n) ").lower()
            print

    except Exception as e:
        displayError(this.__name__, e)


mainProg()
