

class FiniteElement():
    """docstring for Finiteelement"""

    def __init__(self, element: int, prime: int): #initiate the finite field
        if type(element) == int:
            if element >= prime or element < 0: #check if element btwn 0 and prime-1
                error = 'Element {} not in the range of the finite field of 0 to {}'\
                .format(element, prime-1)
                raise ValueError(error)
        self.element= element
        self.prime = prime


    def __eq__(self, other): #equating function
        if other is None:
            return False
        return self.element == other.element and self.prime == other.prime

    def __ne__(self, other): #not equal
        return not (self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            exception = 'Cannot add two elements not in the same order'
            raise TypeError(exception)
        if self == None:
            return other
        if type(self.element) == int:
            element = (self.element + other.element) % self.prime
        elif type(self.element) == FiniteElement:
            element = (self.element.element + other.element.element)  % self.prime
        return self.__class__(element, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            exception = 'Cannot subtract  two elements not in the same field'
            raise TypeError(exception)
        if type(self.element) == int:
            element = (self.element - other.element) % self.prime
        elif type(self.element) == FiniteElement:
            element = (self.element.element - other.element.element) % self.prime
        return self.__class__(element, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            exception = 'Cannot multiply elements of different fields'
            raise TypeError(exception)
        element = (self.element * other.element) % self.prime
        return self.__class__(element, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        element = pow(self.element, n, self.prime)
        return self.__class__(element % self.prime, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            exception = 'Cannot divide elements of different fields'
            raise TypeError(exception)
        element = (self.element *pow(other.element, self.prime-2, self.prime)) % self.prime
        return self.__class__(element, self.prime)
    def __repr__(self):#representation function
        return 'FieldElement_{}({})'.format(self.prime, self.element)

P = (2**256) - (2**32) -977
class S256Field(FiniteElement):#creating a field of secp256ki
    def __init__(self, element, prime=None):
        super().__init__(element=element, prime=P)

    def sqrt(self):
        """
        Here we are trying to get a square root in a finite field
        using Fermat's little theorem, P is such that P % 4 == 3,
        hence (P+1)%4 = 0, hence using fermat's little theorem
        w^2 = v when know v becomes w^2^(p+1)/4 = v^(p+1)/4
        """
        return self**((P + 1) // 4)

    def __repr__(self):
        return '{:x}'.format(self.element).zfill(64) #256bit number