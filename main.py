from Segment import Segment
from Canal_network import Canal_network
from Request import Request
from Node import Node
from Arc import Arc
from Label import Label
#
def collision_free_routing(canal_nw,request,time):
    # canal_nw: canal network
    # request: routing request
    # time: time windows
    path = 0

    return path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    seg_list = {"seg1": Segment("transit",100,"seg2"),
                "seg2": Segment("waiting",200,"seg3"),
                "seg3": Segment("transit",300,None)}
    first_seg = "seg1"
    can = Canal_network(seg_list, first_seg)
    print(can.nodes, can.arcs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
