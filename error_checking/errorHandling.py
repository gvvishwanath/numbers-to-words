import sys

from assertions import integerAssert, stringAssert

def displayError(functionString, exception):
    this = globals()[sys._getframe().f_code.co_name]

    try:
        stringAssert(functionString, this)

        print "Error in " + functionString + "(): ", exception
        print

    except Exception as e:
        displayError(this.__name__, e)


def debugHelper1(functionString, lineNo):
    this = globals()[sys._getframe().f_code.co_name]

    try:
        stringAssert(functionString, this)
        integerAssert(lineNo, this)

        print "Reached line number %d in %s(). " % (lineNo, functionString)

    except Exception as e:
        displayError(this.__name__, e)
