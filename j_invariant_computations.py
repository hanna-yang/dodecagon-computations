from sage.all import *
from symbolic_wrappers import *
from dodecagon_maker import * 

def make_q(v0, v2):
    """
    Given two vertices to make a diagonal between, generate the value of q for which
    to shear by
    """
    return (v0.y - v2.y)/(v0.x - v2.x)

def expressions_to_zero(spacing=2, polygon=None):
    """
    input: 
        polygon: polygon to compute jvv expressions to zero
            if no polygon is specified, will compute with the regular 12-gon
        spacing: spacing between successive vertices to form directions in
            (must be an integer > 1)
    ouput: prints a list of expressions such that if polygon is veech,
    all of the expressions will equal 0

    note: takes polygons specified in symbolic or numerical coordinates, 
    or any combination of the two
    """
    expressions = []
    if polygon is None:
        polygon = make_regular()

    # for each diagonal:
    for i in range(6):
        print(i)
        # translate points so that the vertex we are considering is now the origin
        # this will simplify computation of jvv
        translated_polygon = polygon.translate(polygon.vertices[i])

        # in the direction we wish to compute jvv, written as (1, q), we perform
        # a shear such that (1,q) becomes (1,0)
        # we try to compute q, but will fail if we are trying to shear a vertical
        # vector to be horizontal, so we ignore such directions
        try:
            # TODO: replace this with the q[x/y] to shear by method
            q = make_q(translated_polygon.vertices[i], translated_polygon.vertices[i+spacing])
        except ZeroDivisionError:
            expressions.append(None)
            continue

        # shear each of the points in the 12-gon using q
        sheared_polygon = translated_polygon.shear_x_zero(q)

        # compute jyy for this polygon
        jyy = sheared_polygon.jyy()
        expressions.append(jyy)

    return expressions

def compute_all_jxy(polygon = None):
    """
    for each direction for which there exists a cylinder in
    a 12-gon, compute jxy
    """
    expressions = []
    symmetric = []

    # given a 12-gon, we do the following:
    # polygon = Symbolic12Gon()
    # polygon = make_regular()
    if polygon is None:
        polygon = make_any_gon()
    # polygon = make_assumption_gon()

    # print(polygon.vertices)
    for i in range(6):
        print(i)
        # translate such that this point is the origin
#         polygon = polygon.translate(polygon.vertices[i])
#         print(polygon)
        # shear so that the diagonal we are considering is vertical
        try:
            q = polygon.vertices[i].qx_to_shear_by(polygon.vertices[i+1])
#             print("q1:", q.rational(D=3), q.irrational(D=3))
        except ZeroDivisionError:
            print("-------")
            print("division by 0!")
            print("-------")
            continue

        sheared_polygon = polygon.shear_x_zero(q)
#         print(sheared_polygon)
#         print("test:", sheared_polygon.vertices[i] - sheared_polygon.vertices[i+1])
        w, h = sheared_polygon.get_cylinder(i)
        # print("h: ",h.full_simplify())
#         print("shear 1 w: ",w.full_simplify())
        # print(len(sheared_polygon.vertices))
#         print(sheared_polygon.vertices[i])
        # shear again so that the edge that we consider is horizontal
        try:
            q = sheared_polygon.vertices[i].qy_to_shear_by(sheared_polygon.vertices[(i + 7) % 12])
#             print(sheared_polygon.vertices[i], sheared_polygon.vertices[(i + 7) % 12])
#             print("q2:", q.rational(D=3), q.irrational(D=3))
        except ZeroDivisionError:
            print("-------")
            print("division by 0!")
            print("-------")
            continue

        twice_sheared = sheared_polygon.shear_y_zero(q)

        # rescale such that the modulus of the vertical cylinder is rational
        w, h = twice_sheared.get_cylinder(i)
#         print("shear 2 h: ",h.full_simplify())
#         print("shear 2 w: ",w.full_simplify())
        # print(w.y, h.x)
        stretch_factor = w.x/h.y # this should be reciprocated, but we just care it is rational
        # print(stretch_factor)
        stretched_polygon = sheared_polygon.stretch_y(stretch_factor)

        # compute Jxy
        jxy = stretched_polygon.jxy()
        expressions.append(jxy)
        symmetric.append((jxy[1], jxy[2]))

    return expressions, symmetric
