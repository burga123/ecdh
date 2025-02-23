from Point import Point
from FiniteElements import S256Field

P = (2**256) - (2**32) -977
A = 0 #value of a in secp256ki
B = 7 #value of b in secp256ki
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Point(Point):#defining the point for the field above
    def __init__(self, x, y, a=None, b=None):
        _a = S256Field(A)
        _b = S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y, P), a=_a, b=_b)
        else:
            super().__init__(x=x, y=y, a=_a, b=_b)

    def __rmul__(self, coefficient):#defining recursive multiplication as we know N
        coef = coefficient % N #to make sure that the coefficient always goes back to 0 incase bigger than N
        return super().__rmul__(coef) 
    def __repr__(self):
        return 'S256Point {}, {}'.format(self.x, self.y)
    
G = S256Point(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
