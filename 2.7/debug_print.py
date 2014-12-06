from __future__ import print_function

#-----------------------------------------------------------
#For compatible with python3.x
#use: from __future__ import print_function

DEBUG = 1
def debug(*debug_string):
    '''used to print style debugging.
'''
    if DEBUG:       
        for each in debug_string:
            print(each, end="")
        print(end="\n")
#-----------------------------------------------------------


if __name__ == '__main__':
	debug('dizuo')
	var = 5
	debug('var = ', var)