from math import sqrt

class Vector:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.args))})"

    def __add__(self, second_vec):
        if len(self.args) != len(second_vec.args):
            return "Vector components do not equal"
        return Vector(*(a + b for a,b in zip(self.args, second_vec.args)))

    def __sub__(self, second_vec):
        if len(self.args) != len(second_vec.args):
            return "Vector components do not equal"
        return Vector(*(a - b for a,b in zip(self.args, second_vec.args)))

    def __mul__(self, other):
        if type(other) == Vector:
            if len(self.args) != len(other.args):
                return "Vector components do not equal"
            return sum([*(a * b for a,b in zip(self.args, other.args))])
        else:
            return Vector(*(a * other for a in self.args))
        

    def magnitude(self):
        return sqrt(sum(a**2 for a in self.args))

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
             return 'Magnitude must not be zero'
        return Vector(*(round(a/magnitude, 3) for a in self.args))

    
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = v1 * 3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)