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
        random_num = -100
        n = {}
        a = {}
        n[str(0)] = Node(0, str(0))
        seg = self.first_segment
        for i in range(1,len(self.segment_dic)+1):
            #Generate node at end of siding
            n[str(i)] = Node(n[str(i-1)].position + self.segment_dic[seg].length, str(i))
            #Generate arc, if segment is a transit segment
            if self.segment_dic[seg].type == 'transit':
                a[(str(i-1), str(i))] = Arc("transit", n[str(i-1)], n[str(i)], self.segment_dic[seg].length, [])
                a[(str(i), str(i-1))] = Arc("transit", n[str(i)], n[str(i-1)], self.segment_dic[seg].length,[])
            elif self.segment_dic[seg].type == 'siding':
                #in one direction
                n[str(i-0.6)] = Node(None, str(i-0.6))
                a[str(i-1), str(i-0.6)] = Arc("alpha", n[str(i-1)], n[str(i-0.6)],random_num, [])
                a[str(i-0.6), str(i-0.6)] = Arc("beta", n[str(i-0.6)], n[str(i-0.6)],random_num, [])
                a[str(i-0.6), str(i)] = Arc("gamma", n[str(i-0.6)], n[str(i)],random_num, [])
                #in the other direction 
                n[str(i-0.4)] = Node(None, str(i-0.4))
                a[str(i), str(i-0.4)] = Arc("alpha", n[str(i)], n[str(i-0.4)],random_num, [])
                a[str(i-0.4), str(i-0.4)] = Arc("beta", n[str(i-0.4)], n[str(i-0.4)],random_num, [])
                a[str(i-0.4), str(i-1)] = Arc("gamma", n[str(i-0.4)], n[str(i-1)],random_num, [])
            seg = self.segment_dic[seg].suc
        return n,a

    def print_nodes(self):
        for n in self.nodes.keys():
            print(n + " at position {}".format(self.nodes[n].position))
    
    def print_arcs(self):
        for a in self.arcs.keys():
            print(str(a)  + " goes from {}".format(self.arcs[a].tail.name) + " to {}".format(self.arcs[a].head.name) + " and is of type " + self.arcs[a].type)
