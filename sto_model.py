from gurobipy import *

def solve(S, E, T, R):

    # init model
    model = Model("Ship Traffic Optimization")

    # init variables
    d = {}
    omega = {}
    w = {}
    z = {}
    delta = {}

    C_E = findConflicts(E,S,d)

    for i in S:
        for t in T:
            w[i,t] = model.addVar(vtype=GBR.INTEGER, name="w_%s_%s" %(i,t), lb=0)

        for e in E:
            d[i,e] = model.addVar(vtype=GBR.INTEGER, name="d_%s_%s" %(i,e), lb=0)
            omega[i,e] = model.addVar(vtype=GBR.INTEGER, name="omega_%s_%s" %(i,e), lb=0)



def findConflicts(E,S,d):

    C_E = {}

    for i in S:
        for e in E:
            for j in S:
                if d[i,e] == d[j,e]:
                    C_E[(i,j)] = e

    return C_E



