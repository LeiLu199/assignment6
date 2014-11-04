class nullInterval(Exception):
    def __str__(self):
        return 'Your input is an empty string!'
    pass

class invalidBracket(Exception):
    def __str__(self):
        return 'Your string does not have brackets\parenthesis!'
    pass

class invalidIntervalInput(Exception):
    def __str__(self):
        return 'Your string input is not an interval!'
    pass

class invalidIntervalList(Exception):
    def __str__(self):
        return 'Your input string is not a valid interval list!'
    pass

class noOverlapping(Exception):
    def __str__(self):
        return 'Intervals do not overlap!'
    pass
