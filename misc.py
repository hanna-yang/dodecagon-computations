from sage.all import *
from j_invariant_computations import *
from symbolic_wrappers import *
from dodecagon_maker import *
# ---------- general utility functions -------------
def dist_along_transversal(coord):
    """
    calculates the x-coordinate of the intersection point of the
    coordinate with the y-axis, when projected in the direction parallel
    to the cylinder in the center

    TODO: generalize this (just have it take a slope)
    """
    p = make_60_deg_sym_gon()
    v3 = p.vertices[3]
    v10 = p.vertices[10]
    m = (v3.y - v10.y)/(v3.x - v10.x)
    return (coord.y.scale(-1))/(m) + coord.x

def eqn_for_line_2pts(p1, p2):
    """
    given two points p1, p2, return the tuple m,b
    such that p1 and p2 lie on the line y = mx + b
    """
    m = (p2.y-p1.y)/(p2.x - p1.x)
    return eqn_for_line_point_slope(p1, m)

def eqn_for_line_point_slope(p1, m):
    """
    given a point p1 and a slope m, return the tuple m,
    b such that p1 lies on y = mx + b
    """
    return m, p1.y - m*p1.x

def intersection(m1, b1, m2, b2):
    """
    given two lines, y = m1 + b1 and y = m2 + b2,
    return the intersection of the two lines
    """
    def intersection_x(m1, b1, m2, b2):
        return (b2 - b1)/(m1 - m2)

    x = intersection_x(m1, b1, m2, b2)
    return SymbolicCoordinates(x, m1 * x + b1) # , m2 * x + b2 for debugging

