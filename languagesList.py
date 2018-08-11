import sys

from fileImportHelp import my_import
from error_checking.errorHandling import displayError
from error_checking.errorHandling import debugHelper1

availableLanguages = {
    1 : "English",
    2 : "Chinese",
    3 : "Hindi",
    4 : "Tamil"
}

def printOptions():
    for key, value in availableLanguages.iteritems():
        print "%r : %r" % (key, value)
    print


def welcome():
    print "Hello! This program can translate an input integer into different languages.\n"


def getUserChoice():
    this = globals()[sys._getframe().f_code.co_name]

    welcome()
    print "We can translate into the following languages:"
    printOptions()
    language = 'English'

    try:    
        choice = int(raw_input("Choose a language of your choice: (number) "))

        if choice in availableLanguages.keys():
            language = availableLanguages[choice]
        
        else:
            language = 'English'
            print "Choosing English by default."

    except Exception as e:
        displayError(this.__name__, e)

    finally:
        moduleName =  language.lower() + "_numbers_info.translate"

        try:
            translator = my_import(moduleName)

        except Exception as e:
            displayError(this.__name__, e)
            translator = my_import('english_numbers_info.translate')
            print "Choosing English by default. Sorry for the inconvenience."

        print
        return translator
