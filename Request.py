class Request:
    start = -200
    target = -200
    velocity = -200
    release_time = -200
    parking_distance = -200

    def __init__(self, s, t, v, r, h):
        self.start = s
        self.target = t
        self.velocity = v
        self.release_time = r
        self.parking_distance = h
