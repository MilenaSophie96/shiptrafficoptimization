from Segment import Segment
from Canal_network import Canal_network

# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def collision_free_routing(canal_nw,request,time):
    # canal_nw: canal network
    # request: routing request
    # time: time windows
    test, test
    path = 0

    return path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    seg_list = {"seg1": Segment("transit",100,"seg2"),
                "seg2": Segment("waiting",200,"seg3"),
                "seg3": Segment("transit",300,None)}
    first_seg = "seg1"
    can = Canal_network(seg_list, first_seg)
    print(can.N)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
