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
    # TODO: add the flatsurf version of this polygon and compare the j-invariant

    twelve_gon = [to_coords(Integer(-1),Integer(0),Integer(0),Integer(0)), 
                  to_coords(Integer(13)/Integer(171),Integer(-42)/Integer(85),Integer(42)/Integer(84),Integer(-12)/Integer(170)), 
                  to_coords(Integer(-1)/Integer(2),Integer(0),Integer(0),Integer(1)/Integer(2)), 
                  to_coords(Integer(13)/Integer(85),Integer(0),Integer(84)/Integer(85),Integer(0)), 
                  to_coords(Integer(1)/Integer(2),Integer(0),Integer(0),Integer(1)/Integer(2)), 
                  to_coords(Integer(14)/Integer(170),Integer(-42)/Integer(85),Integer(42)/Integer(85),Integer(13)/Integer(170))]
    vertices = twelve_gon[:]
    for coord in twelve_gon:
        vertices.append(coord.scale(Integer(-1)))
    p = Symbolic12Gon(vertices)
    return p.jyy(), p.translate(to_coords(1,1,1,1)).jyy()

print(test_j_invt())
