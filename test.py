from sage.all import *
from j_invariant_computations import *
from symbolic_wrappers import *
from dodecagon_maker import *
from misc import *

#TODO: fill in test suite with assertion statements

# test j-invariant correctness:
def test_j_invt():
    """
    compares the j-invariant computed by this code with j-invariants as
    computed by flatsurf
    """
    twelve_gon = [to_coords(-1,0,0,0), 
                  to_coords(13/171,-42/85,42/84,-12/170), 
                  to_coords(-1/2,0,0,1/2), 
                  to_coords(13/85,0,84/85,0), 
                  to_coords(1/2,0,0,1/2), 
                  to_coords(14/170,-42/85,42/85,13/170)]
    vertices = twelve_gon[:]
    for coord in twelve_gon:
        vertices.append(coord.scale(-1))
    p = Symbolic12Gon(vertices)
    return p.jyy(), p.translate(to_coords(1,1,1,1)).jyy()

print(test_j_invt())
