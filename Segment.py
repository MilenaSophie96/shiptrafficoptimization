class Segment:
    type = "no_type" #transit or waiting 
    length = -100
    suc = None

    def __init__(self, t, l, s):
        self.type = t
        self.length = l
        self.suc = s
