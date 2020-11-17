class Canal_network:
    seg_dic = {}
    first = None
    A = {}
    N = {}

    def __init__(self, dic, f):
        self.seg_dic = dic
        self.first = f
        self.N = self.construct_nodes()
        self.A = self.construct_arcs()

    def construct_nodes(self):
        n = len(self.seg_dic)
        net = {}
        net[str(0)] = 0
        seg = self.first
        for i in range(1,n+1):
            net[str(i)] = net[str(i-1)] + self.seg_dic[seg].length
            seg = self.seg_dic[seg].suc
        return net

    def construct_arcs(self):
        arc = {}
        for i in range(len(self.N)):
            #arc[(self.N[str(i)], self.N[str(i+1)] = #length, time window
            #arc[(self.N[str(i+1)], self.N[str(i)] = #length
        return arc