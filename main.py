from sage.all import *
from j_invariant_computations import *
from symbolic_wrappers import *
from dodecagon_maker import *
from misc import *

"""
Let the vertices, in clockwise order of the dodecagon, starting from
(1, 0) be v0, v1, v2, ... v11
"""

def compute_60_deg_gb():
    """
    prints out the groebner basis generated by the following expressions
    (set equal to zero)
    - the projection of the j-invariant, Jvv, along the directions of
    vectors connecting:
        -
    - the irrational component of the numerator of
    -
    one can verify that the only solutions are
    b1=c1=0
    and
    a1=0, b1=1/2, c1=1/2, d1=0
    either by hand, or asking sage to solve the series of equations which are printed.

    TODO: maybe fix the issues with all the variables so that solve will work
    by passing variables into the constructor
    """
    equations_to_zero = []
    p = make_60_deg_sym_gon()

    # compute the equations corresponding to zero-ing of j-invariant
    print("computing equations arising from j-invt")
    exp_assumption = []
    for i in range(2,4):
        exp_assumption += expressions_to_zero(i, polygon=p)[:2]
    nums = [e.numerator()(D=Integer(3)) for e in exp_assumption if e is not None]
    equations_to_zero += nums

    R = QQ['a1, b1, c1, d1']; (a1, b1, c1, d1,) = R._first_ngens(4)
    I = R.ideal(equations_to_zero)
    gb = I.groebner_basis()
    print("groebner basis of jvv computations for")
    print("a pi/3 rotationally symmetric 12-gon (see lemma [TODO]")
    print(gb)

    # compute the equations corresponding the zero-ing of the irrational part of the
    # ratio of the moduli of two cylinders which always appear on the 12-gon
    # TODO: clean up this computation; check to make sure naming conventions are followed
    print("computing equations arising from rational moduli")
    p = make_60_deg_sym_gon()

    # wi_scaled are the projection of 
    w2_scaled = (dist_along_transversal(p[2])-\
        dist_along_transversal(p[1]))
    w1_scaled = (dist_along_transversal(p[4]) -\
        dist_along_transversal(p[3]))
    w_comp = w2_scaled/w1_scaled
    
    m = (p[3].y - p[10].y)/(p[3].x - p[10].x)
    parallel2 = eqn_for_line_point_slope(p[2], m)
    side = eqn_for_line_2pts(p[11], p[0])
    pt2 = intersection(*parallel2, *side)
    parallel1 = eqn_for_line_point_slope(p[1], m)
    pt1 = intersection(*parallel1, *side)

    h2 = (p[2].x - pt2.x) + (p[1].x - pt1.x)
    h1 = (p[4].x - p[9].x)
    h_comp = h1/h2

    irr_mod1 = (w_comp*h_comp).irrational(D=Integer(3)).numerator()
    equations_to_zero.append(irr_mod1)

    # print("equations to zero:", equations_to_zero)
    # compute groebner basis of all the generated equations
    R = QQ['a1, b1, c1, d1']; (a1, b1, c1, d1,) = R._first_ngens(4)
    I = R.ideal(equations_to_zero)
    gb = I.groebner_basis()

    print("computing groebner basis generated by the expressions derived")
    print("from the 60 degree symmetric 12-gon:")
    return gb

def cyclic_moduli():
    """
    Computes the pairwise moduli of the cylinders along the direction from
    v3 to v10, and sets the irrational part to 0. If the groebner basis
    computed by adding these equations doesn't change, then all cyclic
    12-gons will already have this property

    we use the following conventions:
    - the central cylinder is numbered 1
    - the other cylinders, numbered going to the right, are 2 and 3
    - hi and wi are the height and width, respectively of the cyliders

    Note that in our derivation of these formulas, we already force two cylinders
    to have commensurable moduli. We then only need to check the moduli of
    the remaining cylinder against any other moduli

    TODO: clean up the make 60 sym gon repetitions; get rid of additional print statements
    """
    equations_to_zero = list(compute_60_deg_gb())

    p = make_60_deg_sym_gon()

    w2_scaled = (dist_along_transversal(p[3])-\
        dist_along_transversal(p[2]))
    w1_scaled = (dist_along_transversal(p[4]) -\
        dist_along_transversal(p[3]))
    w_comp = w2_scaled/w1_scaled

    h2 = p[3].x - p[10].x + p[2].x - p[11].x
    h1 = (p[4].x - p[9].x)
    h_comp = h1/h2

    irr_mod1 = (w_comp*h_comp).irrational(D=Integer(3)).numerator()
    equations_to_zero.append(irr_mod1)

    R = QQ['a1, b1, c1, d1']; (a1, b1, c1, d1,) = R._first_ngens(4)
    I = R.ideal(equations_to_zero)
    gb = I.groebner_basis()

    return gb
    

def compute_generic_gb():
    """
    prints groebner basis for a generic 12-gon with equations derived from
    - Jvv connections along diagonals
    - Jxy symmetric constraints

    here, we make the additional normalization that there is one vertex at (1,0).
    this is afforded to us because actions on a surface by GL2R do not affect its
    veechness
    """
    equations_to_zero = []
    p = make_more_assumption_gon()

    # compute the equations corresponding to zero-ing of j-invariant
    print("computing equations arising from j-invt")
    exp_assumption = []
    for i in range(1,6):
        exp_assumption += expressions_to_zero(i, polygon=p)
    nums = [e.numerator()(D=Integer(3)) for e in exp_assumption if e is not None]
    equations_to_zero += nums

    exp, sym = compute_all_jxy(polygon=p)
    for i in range(6):
        equations_to_zero.append((sym[i][0].numerator()*sym[i][1].denominator() - sym[i][1].numerator()*sym[i][0].denominator())(Integer(3)))

    R = QQ['a1, b1, c1, d1, a2, b2, c2, d2, a4, b4, c4, d4, a5, b5, c5, d5']
    (a1, b1, c1, d1, a2, b2, c2, d2, a4, b4, c4, d4, a5, b5, c5, d5) = R._first_ngens(17)
    I = R.ideal(equations_to_zero)
    gb = I.groebner_basis()
    print(gb)

# ------------ output ------------
print(compute_60_deg_gb())
# print(cyclic_moduli())
# compute_generic_gb()
