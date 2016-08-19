'''
    module: Errors handler
'''

# Errors:
# validations errors start from 1: 1xy
# parse errors start from 2: 2xy
# ...
errors = {'Ok':0,
          'PathNotFound':101, 'NotFile':102, 'NotDir':103, 'NotPath':104,
          'ParseErr':201, # parse errors 2xy
         }

#
class ErrorHandler(Exception):
    pass