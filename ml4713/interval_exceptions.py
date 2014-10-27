# -*- coding: utf-8 -*-
"""This file contains three exceptions:
      Invalid_Interval_list_input(): if the user enters invalid input interval list
      Invalid_Interval_input(): if a single interval is not valid
      Cant_be_merged(): if two intervals are not mergeable     
"""

class Invalid_Interval_list_input(Exception):   
    pass
    
    
class Invalid_Interval_input(Exception):
    pass

class Cant_be_merged(Exception):
    pass