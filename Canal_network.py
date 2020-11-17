from Segment import Segment
from Request import Request
from Node import Node
from Arc import Arc
from Label import Label

class Canal_network:
    segment_dic = {}
    first_segment = None
    arcs = {} #Dictionnary with arc objects
    nodes = {} #Dictionnary with node objects

    def __init__(self, dic, f):
        self.segment_dic = dic
        self.first_segment = f
        self.nodes, self.arcs = self.construct_graph()

    def construct_graph(self):
        n = {}
        a = {}
        n[str(0)] = Node(0)
        seg = self.first_segment
        for i in range(1,len(self.segment_dic)+1):
            #Generate node at end of siding
            n[str(i)] = Node(n[str(i-1)].position + self.segment_dic[seg].length)
            #Generate arc, if segment is a transit segment
            if self.segment_dic[seg].type == 'transit':
                a[(str(i-1), str(i))] = Arc("transit", n[str(i-1)], n[str(i)], self.segment_dic[seg].length, [])
                a[(str(i), str(i-1))] = Arc("transit", n[str(i)], n[str(i-1)], self.segment_dic[seg].length,[])
            seg = self.segment_dic[seg].suc
        return n,a
