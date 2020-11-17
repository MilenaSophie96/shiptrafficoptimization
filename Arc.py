class Arc:
    type = None #Can be of transit, alpha, gamma or betha
    tail = -100
    head = -100
    length = -100
    forb_time = []

    def __init__(self,ty, t, h, l, f_t):
        self.type = ty
        self.tail = t
        self.head = h
        self.length = l
        self.forb_time = f_t
