class Polyline:
    ship = None
    chain = []

    def __init__(self, ship, position_time = None):
        self.ship = ship
        if position_time != None:
            self.chain.append(position_time)
        
    def add_element(self, position_time):
        # time_position should be (position, time) tuple
        self.chain.append(position_time)