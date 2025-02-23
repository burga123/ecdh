from FiniteElements import FiniteElement

class Point():#defining a point on a curve using secp256k1 y^2 = x^3 + a.x^2 + b
    zero = 0
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if (self.y)**2 != (self.x)**3 + a*x + b:
            raise ValueError('Point {},{} is not on curve'.format(x, y))
        
    def __eq__(self, other):
        if other is None:
            return False
        return self.a == other.a and self.b == other.b and self.x == other.x and self.y == other.y


    def __ne__(self, other):
        return not (self == other)
        """return self.a != other.a and self.b != other.b and self.x != other.x and self.y != other.y"""


    def __add__(self, other):
        three = FiniteElement(element=3, prime=self.x.prime)
        zero = FiniteElement(element=0, prime=self.x.prime)
        if self.x == other.x and self.y == other.y and self.y == zero:
            return self.__class__(None, None, self.a, self.b)
        if self.a != other.a or self.b != other.b:
            exception = 'Points {} {} are not on the same curve'.format(self, other)
            raise TypeError(exception)

        if other.x is None:
            x = self.x
            y = self.y
        elif self.x is None:
            x = other.x
            y = other.y

        if self.x == other.x and self.y != other.y:
            x = None
            y = None

        if self.x != other.x:
            slope = (other.y - self.y) / (other.x - self.x)
            x = pow(slope, 2) -self.x - other.x
            y = (slope*(self.x - x)) - self.y


        if self.x == other.x and self.y == other.y:
            slope = (three*pow(self.x, 2) + self.a) / (self.y+self.y)
            x = pow(slope, 2) - (self.x+self.x)
            y = (slope*(self.x - x)) - self.y
        


        return self.__class__(x, y, self.a, self.b)
    def __rmul__(self, coefficient):    #using binary expansion
        coef = coefficient-1
        current = self
        """result0 = self.__class__(None, None, self.a, self.b)"""#start at point at infinity
        result1 = self.__class__(self.x, self.y, self.a, self.b)#due to a hiccup(slope for self ==other) up there i cannot start at 0
        while coef:
            if coef & 1: #checking the right-most bit, if 1 add 1
                result1 +=current #adding point to itself
            current += current #adding point to self again
            coef >>=1 #shifting the coeffiecient bit to the right
        return result1