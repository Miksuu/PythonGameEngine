# Let's extend the Vector2 class by adding as many operations as possible within the token limit.
# We'll include addition, subtraction, multiplication, division, magnitude, normalization, and dot product.

import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # Subtraction
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    # Scalar Multiplication
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    # Scalar Division
    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    # Magnitude (Length)
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Normalization
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0, 0)
        return self / mag

    # Dot Product
    def dot(self, other):
        return self.x * other.x + self.y * other.y

# Create instances to test these operations
v1 = Vector2(3, 4)
v2 = Vector2(1, 2)

# Test Addition
add_result = v1 + v2

# Test Subtraction
sub_result = v1 - v2

# Test Scalar Multiplication
mul_result = v1 * 2

# Test Scalar Division
div_result = v1 / 2

# Test Magnitude
mag_result = v1.magnitude()

# Test Normalization
norm_result = v1.normalize()

# Test Dot Product
dot_result = v1.dot(v2)

# Compile test results
test_results = {
    'Addition': add_result.__dict__,
    'Subtraction': sub_result.__dict__,
    'Scalar Multiplication': mul_result.__dict__,
    'Scalar Division': div_result.__dict__,
    'Magnitude': mag_result,
    'Normalization': norm_result.__dict__,
    'Dot Product': dot_result
}

test_results
