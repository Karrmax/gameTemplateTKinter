class Vector:
    
    def __init__(self,x, y) -> None:
        self.x = x
        self.y = y
        
    @staticmethod
    def prods(vector1,vector2):
        return vector1.x*vector2.x + vector1.y*vector2.y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, vect):
        return Vector(self.x + vect.x, self.y + vect.y)
    
    def __min__(self, vect):
        return Vector(self.x - vect.x, self.y - vect.y)
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        
    def __rmul__(self, other):
        return self * other
    
    def __neg__(self):
        return -1 * self
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)
    
    def __copy__(self):
        return Vector(self.x, self.y)

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        copy_obj = Vector(self.x, self.y)
        memo[id(self)] = copy_obj
        return copy_obj

    def prods(self, vector):
        return self.x * vector.x + self.y * vector.y

    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def to_tuple(self):
        return (self.x, self.y)

    @staticmethod
    def from_tuple(t):
        return Vector(t[0], t[1])
    
NULLVECTOR = Vector(0, 0)
    