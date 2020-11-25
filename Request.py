class Request:
    ship = None
    start = -200
    target = -200
    velocity = -200
    release_time = -200
    parking_distance = -200

    def __init__(self, name, s, t, v, r, h):
        self.ship = name
        self.start = s
        self.target = t
        self.velocity = v
        self.release_time = r
        self.parking_distance = h
