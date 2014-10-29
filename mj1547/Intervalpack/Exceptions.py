'''


@author: jiminzi
'''
# there are two expection I raised
'''
if the pattern do not follow the interval instruction
'''
class InvaildIntervals(Exception):
    '''
    raise exception for invalidIntervals
    '''
    pass

class NoOverLapping(Exception):
    '''
    raise exception for no overlapping 
    '''
    pass