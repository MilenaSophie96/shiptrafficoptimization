# number of ships S
nShips = 4

# list of ships S
S = list(range(nShips))

# number of canal segments E
nSegments = 5

# hash map of canal C
C = {"1":{"isSiding":False},
        "2":{"isSiding":False},
        "3":{"isSiding":False},
        "4":{"isSiding":False},
        "5":{"isSiding":False}}

# list of segments E
E = list(range(nSegments))

# list of siding T
T = [0,4]

# hash map of R
R = {1:{"s":1, "t":4, "r":8},
        2:{"s":1, "t":4, "r":9},
        3:{"s":1, "t":4, "r":10},
        4:{"s":1, "t":4, "r":12}}

import sto_model
sto_model.solve(S, E, T, R)

