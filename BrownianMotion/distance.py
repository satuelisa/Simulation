from math import fabs, sqrt
 
def euclideana(p1, p2):
    return sqrt(sum([(c1 - c2)**2 for (c1, c2) in zip(p1, p2)]))
 
def manhattan(p1, p2):
    return sum([fabs(c1 - c2) for (c1, c2) in zip(p1, p2)])
 
def ed_orig(p):
    dimension = len(p)
    origen = [0] * dimension
    return euclideana(p, origen)
 
def md_orig(p):
    dimension = len(p)
    origen = [0] * dimension
    return manhattan(p, origen)
