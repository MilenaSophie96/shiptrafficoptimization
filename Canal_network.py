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



        net = {}
        net[str(0)] = 0
        seg = self.first
        for i in range(1,len(self.segment_dic)+1):
            net[str(i)] = net[str(i-1)] + self.seg_dic[seg].length
            seg = self.seg_dic[seg].suc
        return net, arc
