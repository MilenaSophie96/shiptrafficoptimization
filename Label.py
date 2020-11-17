class Label:
    start_position = -100
    arc_head = -100
    epat = -100
    lpat = -100
    pred = -100
    length = -100

    def __init__(self, s, a, e, lp, p, l):
        self.start_position = s
        self.arc_head = a
        self.epat = e
        self.lpat = lp
        self.pred = p
        self.length = l
