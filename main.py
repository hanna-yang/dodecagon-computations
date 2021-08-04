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
    """
    equations_to_zero = []
    p = make_60_deg_sym_gon()

    # compute the equations corresponding to zero-ing of j-invariant
    exp_assumption = []
    for i in range(2,4):
        exp_assumption += expressions_to_zero(i, polygon=p)[:2]
    nums = [e.numerator()(D=Integer(3)) for e in exp_assumption if e is not None]
    equations_to_zero += nums

    # # compute the equations corresponding the zero-ing of the ratio of the two intervals of the IET
    # # the surface always breaks into three cylinders -- this code seems to not add any new constraints
    # irrational_iet = ((dist_along_transversal(p.vertices[3]) - dist_along_transversal(p.vertices[2]))/(dist_along_transversal(p.vertices[1]) - dist_along_transversal(p.vertices[0]))).irrational(D=3).numerator() 
    # equations_to_zero.append(irrational_iet)

    # compute the equations corresponding the zero-ing of the irrational part of the
    # ratio of the moduli of two cylinders
    w_comp = (dist_along_transversal(make_60_deg_sym_gon().vertices[2])-\
        dist_along_transversal(make_60_deg_sym_gon().vertices[1]))/(\
        dist_along_transversal(make_60_deg_sym_gon().vertices[4]) -\
        dist_along_transversal(make_60_deg_sym_gon().vertices[3]))

    p = make_60_deg_sym_gon().vertices
    m = (p[3].y - p[10].y)/(p[3].x - p[10].x)
    parallel = eqn_for_line_point_slope(p[2], m)
    side = eqn_for_line_2pts(p[11], p[0])
    pt2 = intersection(*parallel, *side)
    m = (p[3].y - p[10].y)/(p[3].x - p[10].x)
    parallel = eqn_for_line_point_slope(p[1], m)
    side = eqn_for_line_2pts(p[11], p[0])
    pt1 = intersection(*parallel, *side)

    h2 = (p[2].x - pt2.x) + (p[1].x - pt1.x)
    h_comp = (make_60_deg_sym_gon().vertices[4].x - make_60_deg_sym_gon().vertices[9].x)/h2

    irr_mod1 = (w_comp*h_comp).irrational(D=Integer(3)).numerator()
    equations_to_zero.append(irr_mod1)

    # w_comp = (dist_along_transversal(make_60_deg_sym_gon().vertices[2])-\
        # dist_along_transversal(make_60_deg_sym_gon().vertices[1]))/(\
        # dist_along_transversal(make_60_deg_sym_gon().vertices[3]) -\
        # dist_along_transversal(make_60_deg_sym_gon().vertices[2]))
    # h_comp = (make_60_deg_sym_gon().vertices[2].x - make_60_deg_sym_gon().vertices[11].x + make_60_deg_sym_gon().vertices[3].x - make_60_deg_sym_gon().vertices[10].x)/(make_60_deg_sym_gon().vertices[1].x - make_60_deg_sym_gon().vertices[0].x + make_60_deg_sym_gon().vertices[2].x - make_60_deg_sym_gon().vertices[11].x)
    # irr_mod1 = (w_comp*h_comp).irrational(D=Integer(3)).numerator()
    # equations_to_zero.append(irr_mod1)

    # w_comp = (dist_along_transversal(make_60_deg_sym_gon().vertices[4])-\
        # dist_along_transversal(make_60_deg_sym_gon().vertices[3]))/(\
        # dist_along_transversal(make_60_deg_sym_gon().vertices[3]) -\
        # dist_along_transversal(make_60_deg_sym_gon().vertices[2]))
    # # w3/w2
    # h_comp = (make_60_deg_sym_gon().vertices[2].x - make_60_deg_sym_gon().vertices[11].x + make_60_deg_sym_gon().vertices[3].x - make_60_deg_sym_gon().vertices[10].x)/(make_60_deg_sym_gon().vertices[3].x - make_60_deg_sym_gon().vertices[10].x)
    # #h2/h3
    # irr_mod2 = (w_comp*h_comp).irrational(D=Integer(3)).numerator()
    # equations_to_zero.append(irr_mod2)

    # print("equations to zero:", equations_to_zero)
    # compute groebner basis of all the generated equations
    R = QQ['a1, b1, c1, d1']; (a1, b1, c1, d1,) = R._first_ngens(4)
    I = R.ideal(equations_to_zero)
    gb = I.groebner_basis()

    print("computing groebner basis generated by the expressions derived")
    print("from the 60 degree symmetric 12-gon:")
    return gb

# ------------ output ------------
print(compute_60_deg_gb())