class InitErr(Exception):
        def __init__(self, message):
                self.message = message
        def __str__(self):
                return self.message

class MergeErr(Exception):
        def __str__(self):
                return "Can not merge."

