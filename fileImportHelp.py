import sys

from error_checking.errorHandling import displayError

def my_import(name):
    this = globals()[sys._getframe().f_code.co_name]

    m = None
    try:
        m = __import__(name)
        for n in name.split(".")[1:]:
            m = getattr(m, n)

    except Exception as e:
        displayError(this.__name__, e)
        print "Failed to import the relevant files."
        raise

    return m
