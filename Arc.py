class Arc:
    tail = -100
    head = -100
    length = -100
    forb_time = []

    def __init__(self, t, h, l, f_t):
        self.tail = t
        self.head = h
        self.length = l
        self.forb_time = f_t
