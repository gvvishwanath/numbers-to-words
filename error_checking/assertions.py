from types import *
import sys

def functionAssert(variable, caller):
    this = globals()[sys._getframe().f_code.co_name]

    assert isinstance(caller, FunctionType), \
    "In %s(): %r is not a function" % (this.__name__, caller)

    assert isinstance(variable, FunctionType), \
    "In %s(): %r is not a function" % (caller.__name__, variable)


def integerAssert(variable, userFn):
    this = globals()[sys._getframe().f_code.co_name]
    functionAssert(userFn, this)

    assert type(variable) is IntType, \
    "In %s(): %r is not an integer" % (userFn.__name__, variable)


def stringAssert(variable, userFn):
    this = globals()[sys._getframe().f_code.co_name]
    functionAssert(userFn, this)

    assert type(variable) is StringType, \
    "In %s(): %r is not a (valid) string" % (userFn.__name__, variable)
