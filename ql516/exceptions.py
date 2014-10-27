# -*- coding: utf-8 -*-

class InValidIntervalList(Exception):
    "raise when the input interval list is invalid"
    def __str__(self):
        return "input interval list is invalid"
    pass



class InValidInterval(Exception):
    "raise when the interval is invalid"
    pass

class NotOverlap(Exception):
    "raise in the mergeIntervals function when the two intervals are not overlapping"
    pass

    