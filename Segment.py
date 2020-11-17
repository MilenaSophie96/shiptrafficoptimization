class Segment:
    type = "no_type"
    length = -100
    #pre = None
    suc = None
    #position = 0

    def __init__(self, t, l, s):
        self.type = t
        self.length = l
        #self.pre = p
        self.suc = s
        #self.position = pos