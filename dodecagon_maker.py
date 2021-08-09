from sage.all import *
from symbolic_wrappers import * 

# TODO: replace all occurrences of numbers with Integer versions of the number

def make_regular():
    """
    return a regular 12-gon
    """
    regular_twelve_gon = [to_coords(-1,0,0,0), to_coords(0,-1/2,1/2,0), to_coords(-1/2,0,0,1/2), to_coords(0,0,1,0), to_coords(1/2,0,0,1/2), to_coords(0,1/2,1/2,0)]
    for coord in [(-1,0,0,0), (0,-1/2,1/2,0), (-1/2,0,0,1/2), (0,0,1,0), (1/2,0,0,1/2), (0,1/2,1/2,0)]:
        regular_twelve_gon.append(to_coords(-1*coord[0], -1*coord[1], -1*coord[2], -1*coord[3]))
    return Symbolic12Gon(regular_twelve_gon)

def make_any_gon():
    twelve_gon = []
    for i in range(6):
        twelve_gon.append(to_coords(var("a" + str(i)), var("b" + str(i)), var("c" + str(i)), var("d" + str(i))))
    for i in range(6):
        twelve_gon.append(to_coords(-1*var("a" + str(i)), -1*var("b" + str(i)), -1*var("c" + str(i)), -1*var("d" + str(i))))
    return Symbolic12Gon(twelve_gon)

def make_assumption_gon():
    twelve_gon = [to_coords(1,0,0,0)]
    for i in range(5):
        twelve_gon.append(to_coords(var("a" + str(i)), var("b" + str(i)), var("c" + str(i)), var("d" + str(i))))
    twelve_gon.append(to_coords(-1,0,0,0))
    for i in range(5):
        twelve_gon.append(to_coords(-1*var("a" + str(i)), -1*var("b" + str(i)), -1*var("c" + str(i)), -1*var("d" + str(i))))
    return Symbolic12Gon(twelve_gon)

def make_ideal_gon():
    var("a6 b6 c6 d6")
    twelve_gon = [to_coords(0,0,0,0),
                  to_coords(a1,b1,c1,d1),
                  to_coords(1,0,0,0),
                  to_coords(a3,b3,c3,d3),
                  to_coords(a4,b4,c4,d4),
                  to_coords(a5,b5,c5,d5),
                  to_coords(a6,b6,c6,d6),
                  to_coords(a6-a1,b6-b1,c6-c1,d6-d1),
                  to_coords(a6-1,b6-0,c6-0,d6-0),
                  to_coords(a6-a3,b6-b3,c6-c3,d6-d3),
                  to_coords(a6-a4,b6-b4,c6-c4,d6-d4),
                  to_coords(a6-a5,b6-b5,c6-c5,d6-d5),
                 ]
    return Symbolic12Gon(twelve_gon)

def make_90_deg_sym_gon():
    """
    return a 12-gon which has 90 degree rotational symmetry
    """
    var("a1 b1 c1 d1")
    var("a2 b2 c2 d2")
    verts = [to_coords(1,0,0,0),
                  to_coords(a1,b1,c1,d1),
                  to_coords(a2,b2,c2,d2),
                ]
    row1 = to_coords(0, 0, -1, 0)
    row2 = to_coords(1, 0, 0, 0)
    e = verts[:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    e = verts[3:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    e = verts[6:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    return Symbolic12Gon(verts)

def make_60_deg_sym_gon():
    """
    return a 12-gon which has 60 degree rotational symmetry
    TODO: clean up this code with some kind of matrix application
    """
    var("a1 b1 c1 d1")
    row1 = to_coords(Integer(1)/Integer(2),0,0,Integer(-1)/Integer(2))
    row2 = to_coords(0,Integer(1)/Integer(2),Integer(1)/Integer(2),0)
    verts = [to_coords(Integer(1),Integer(0),0,0),
             to_coords(a1,b1,c1,d1)]
    e = verts[:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    e = verts[2:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    e = verts[4:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    e = verts[6:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    e = verts[8:]
    for v in e:
        verts.append(SymbolicCoordinates(row1.dot(v),row2.dot(v)))
    return Symbolic12Gon(verts)

def make_more_assumption_gon():
    twelve_gon = [to_coords(1,0,0,0)]
    for i in range(1,3):
        twelve_gon.append(to_coords(var("a" + str(i)), var("b" + str(i)), var("c" + str(i)), var("d" + str(i))))
    twelve_gon.append(to_coords(0,0,1,0))
    for i in range(4,6):
        twelve_gon.append(to_coords(var("a" + str(i)), var("b" + str(i)), var("c" + str(i)), var("d" + str(i))))
    twelve_gon.append(to_coords(-1,0,0,0))
    for i in range(1,3):
        twelve_gon.append(to_coords(-1*var("a" + str(i)), -1*var("b" + str(i)), -1*var("c" + str(i)), -1*var("d" + str(i))))
    twelve_gon.append(to_coords(0,0,-1,0))
    for i in range(4,6):
        twelve_gon.append(to_coords(-1*var("a" + str(i)), -1*var("b" + str(i)), -1*var("c" + str(i)), -1*var("d" + str(i))))
    return Symbolic12Gon(twelve_gon)
