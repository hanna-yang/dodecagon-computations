from sage.all import *
class SymbolicNumQAdjoinSqrtD:
    """
    represents an arbitary number in the field Q[sqrt(D)],
    where all values can be represented with variables

    is mostly just a wrapper class for the symbolic algebra system
    already existing in sage
    """

    def __init__(self, rational, irrational):
        """
        creates a new number in Q(sqrt(D))
        """
        self.rational = rational
        self.irrational = irrational
        self.root = var("D")

    def __repr__(self):
        rep = "(" + self.rational.__repr__() + ")"
        if self.irrational == 0:
            return rep
        return rep + " + (" +\
                     self.irrational.__repr__() + ") sqrt(" +\
                     self.root.__repr__() + ")"

    def __str__(self):
        s = "(" + self.rational.__repr__() + ")"
        if self.irrational == 0:
            return s
        return s + " + (" +\
                     self.irrational.__repr__() + ") sqrt(" +\
                     self.root.__repr__() + ")"

    def __call__(self, val):
        """
        returns a new symbolic number in q adjoin sqrt(D), 
        where all the values D in the rational and irrational
        parts have been set to val

        NOTE: as of now, does not replace the sqrt string with
        the corresponding D value (nor will continue to replace D
        with val in further computations)
        """
        try:
            rs = self.rational(D=3)
        except AttributeError:
            rs = self.rational
        try:
            irs = self.irrational(D=3)
        except AttributeError:
            irs = self.irrational
        return SymbolicNumQAdjoinSqrtD(rs, irs)

    def rational(self):
        return self.rational

    def irrational(self):
        return self.irrational

    def __add__(self, other):
        """
        adds two numbers together, returning another number in the same field
        """
        return SymbolicNumQAdjoinSqrtD(self.rational + other.rational,\
                                       self.irrational + other.irrational)

    def __sub__(self, other):
        """
        returns another number in the field, representing self - other
        """
        return SymbolicNumQAdjoinSqrtD(self.rational - other.rational,\
                                       self.irrational - other.irrational)

    def __mul__(self, other):
        """
        multiplies two numbers together, simplifying and returning another
        number in the same field
        """
        return SymbolicNumQAdjoinSqrtD(self.rational * other.rational +\
                                       self.irrational * other.irrational * self.root,\
                                       self.rational * other.irrational +\
                                       self.irrational * other.rational)

    def conj(self):
        """
        returns the number in this field which has the same rational part,
        and negated irrational part
        """
        return SymbolicNumQAdjoinSqrtD(self.rational, -1*self.irrational)

    def __truediv__(self, other):
        """
        returns a number representing self / other, by rationalizing the denominator
        """
        unscaled = self * other.conj()
        # print(unscaled)
        denom = (other * other.conj()).rational
        return SymbolicNumQAdjoinSqrtD((unscaled.rational)/denom,\
                                       (unscaled.irrational)/denom)

    def full_simplify(self):
        """
        fully simplifies both the rational and irrational parts of this number,
        according to sage
        """
        try:
            rs = self.rational.full_simplify()
        except AttributeError:
            rs = self.rational
        try:
            irs = self.irrational.full_simplify()
        except AttributeError:
            irs = self.irrational
        return SymbolicNumQAdjoinSqrtD(rs, irs)

    # def __call__(self, val):
        # """
        # replaces all instances of 
        # """
        # try:
            # rs = self.rational(D=3)
        # except AttributeError:
            # rs = self.rational
        # try:
            # irs = self.irrational(D=3)
        # except AttributeError:
            # irs = self.irrational
        # return SymbolicNumQAdjoinSqrtD(rs, irs)
    
    def is_rational(self):
        return self.irrational == 0

    def scale(self, i):
        """
        multiplies this number by a number in q
        TODO: this is essentially the same as multiplying
        """
        rs = self.rational
        irs = self.irrational
        return SymbolicNumQAdjoinSqrtD(i*rs, i*irs)

    def wedge_over_q(self, other):
        """
        returns the coefficient of the term (1,0) wedge (0,1) in Q
        (all other terms, for this case, are 0).
        """
        return self.rational*other.irrational - self.irrational*other.rational

class SymbolicCoordinates:
    """
    represents coordinates in 
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + self.x.__repr__() + " , " + self.y.__repr__() + ")"

    def __str__(self):
        return "(" + str(self.x) + " , " + str(self.y) + ")"

    def __sub__(self, other):
        """
        returns another coordinate in the field, representing self - other
        """
        return SymbolicCoordinates(self.x - other.x,\
                                       self.y - other.y)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def magnitude(self):
        """
        returns magnitude of this coordinate as a vector from the origin
        """
        squared = self.x*self.x + self.y*self.y
        expn = squared.rational + squared.irrational * sqrt(var("D"))
        return sqrt(expn)

    def qx_to_shear_by(self, other):
        """
        return the value of q for which to shear by in order to make the
        line from self to other horizontal
        """
        return (self.y - other.y)/(self.x - other.x)

    def qy_to_shear_by(self, other):
        """
        return the value of q for which to shear by in order to make the
        line from self to other horizontal
        """
        return (self.x - other.x)/(self.y - other.y)

    def tensor(self, other):
        """
        """
        a1_ = self.x.rational
        a2_ = other.x.rational
        b1_ = self.x.irrational
        b2_ = other.x.irrational
        c1_ = self.y.rational
        c2_ = other.y.rational
        d1_ = self.y.irrational
        d2_ = other.y.irrational
        return (a1_ * c2_ - a2_ * c1_,\
                a1_ * d2_ - a2_ * d1_,\
                b1_ * c2_ - b2_ * c1_,\
                b1_ * d2_ - b2_ * d1_)

    def full_simplify(self):
        return SymbolicCoordinates(self.x.full_simplify(), self.y.full_simplify())

    def apply_matrix(self, matrix):
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return SymbolicCoordinates(a*self.x + b*self.y, c*self.x + d*self.y)

    def jyy_projection(self, other):
        """
        return coefficient for Jyy, which is the wedge of e1 and e2, where
        e1 represents 1 and e2 represents sqrt(D)
        """
        return self.y.rational * other.y.irrational - self.y.irrational * other.y.rational

    def stretch_y(self, s):
        """
        input types:
            s: SymbolicNumQAdjoinSqrtD
        multiplies the y-coordinates of this point by s
        return: scaled version of this 12-gon
        """
        return SymbolicCoordinates(self.x, self.y * s)

    def translate(self, p):
        return SymbolicCoordinates(self.x - p.x, self.y - p.y)

    def shear_x_zero(self, q):
        """
        Return the coordinates of the sheared version of this point using the matrix
         1  0
        -q  1
        as a tuple, with first value q_rational and second value q_sqrt_d
        """
        q_rational = q.rational
        q_sqrt_d = q.irrational
        a = self.x.rational
        b = self.x.irrational
        c = self.y.rational
        d = self.y.irrational
        y_coord = SymbolicNumQAdjoinSqrtD(c -a*q_rational - q_sqrt_d*b*D, d - a*q_sqrt_d - q_rational*b)
        x_coord = SymbolicNumQAdjoinSqrtD(self.x.rational, self.x.irrational)
        return SymbolicCoordinates(x_coord, y_coord)

    def shear_y_zero(self, q):
        """
        Return the coords of the sheared version of this point using the matrix
        1  -q
        0   1
        as a tuple, with first value q_rational and second value q_sqrt_d
        """
        x_coord = self.x - self.y*q
        y_coord = SymbolicNumQAdjoinSqrtD(self.y.rational, self.y.irrational)
        return SymbolicCoordinates(x_coord, y_coord)

    def scale(self, n):
        return SymbolicCoordinates(self.x.scale(-1), self.y.scale(-1))

def to_coords(a,b,c,d):
    x_coord = SymbolicNumQAdjoinSqrtD(a,b)
    y_coord = SymbolicNumQAdjoinSqrtD(c,d)
    return SymbolicCoordinates(x_coord, y_coord)

class Symbolic12Gon:

    def __init__(self, vertices=None):
        """
        define a 12-gon centered at the origin
        """
        if vertices is None:
            vertices = []
            for i in range(6):
                v_x = SymbolicNumQAdjoinSqrtD(var("a" + str(i)),\
                                              var("b" + str(i)))
                v_y = SymbolicNumQAdjoinSqrtD(var("c" + str(i)),\
                                              var("d" + str(i)))
                vertices.append(SymbolicCoordinates(v_x, v_y))
            for i in range(6):
                v_x = SymbolicNumQAdjoinSqrtD(-1 * var("a" + str(i)),\
                                              -1 * var("b" + str(i)))
                v_y = SymbolicNumQAdjoinSqrtD(-1 * var("c" + str(i)),\
                                              -1 * var("d" + str(i)))
                vertices.append(SymbolicCoordinates(v_x, v_y))
            self.vertices = tuple(vertices)
        else:
            self.vertices = tuple(v for v in vertices)

    def __str__(self):
        """
        returns a string of the vertices, seperated by linebreaks
        """
        s = "Polygon with vertices:\n"
        for vertex in self.vertices:
            s += str(vertex) + "\n"
        return s[:-1]

    def shear_x_zero(self, q):
        """
        input types:
            q: SymbolicNumQAdjoinSqrtD
        shear an entire polygon using the matrix
         1  0
        -q  1
        return: the sheared version of this 12-gon
        """
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex.shear_x_zero(q))
        return Symbolic12Gon(vertices)

    def shear_y_zero(self, q):
        """
        input types:
            q: SymbolicNumQAdjoinSqrtD
        shear an entire polygon using the matrix
         1  0
        -q  1
        return: the sheared version of this 12-gon
        """
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex.shear_y_zero(q))
        return Symbolic12Gon(vertices)

    def translate(self, p):
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex.translate(p))
        return Symbolic12Gon(vertices)

    def stretch_y(self, s):
        """
        input types:
            s: SymbolicNumQAdjoinSqrtD
        multiplies the y-coordinates of all the points
        in this 12-gon by s
        return: scaled version of this 12-gon
        """
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex.stretch_y(s))
        return Symbolic12Gon(vertices)

    def get_cylinder(self, n):
        """
        requires: returns a tuple of vectors (width, height) of
        the cylinder which is through edge vn to v_{n+1}
        """
        width = self.vertices[n] - self.vertices[(n + 1) % 12]
        height = self.vertices[n] - self.vertices[(n + 7) % 12]
        return (width, height)

    def jyy(self):
        jyy = 0
        for i in range(12):
            vi = self.vertices[i]
            vj = self.vertices[(i + 1) % 12]
#             print(vi.jyy_projection(vj))
            jyy += vi.jyy_projection(vj)
        return jyy

    def jxy(self):
        """
        computes jxy projection for this 12-gon
        """
        jxy = [0,0,0,0]
        for i in range(12):
            t = self.vertices[i].tensor(self.vertices[(i + 1) % 12])
            for j in range(4):
                jxy[j] += t[j]
        return tuple(jxy)

