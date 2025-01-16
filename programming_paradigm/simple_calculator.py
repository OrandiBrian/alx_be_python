class SimpleCalculator:
    """A simple calulator class that supports arithmetic operations"""

    def add(self, a, b):
        """Return the addition of a and b"""
        return a + b
    
    def subtract(self, a, b):
        """Return the subtraction of a and b"""
        return a - b
    
    def multiply(self, a, b):
        """Return the multiplication of a and b"""
        return a * b
    
    def divide(self, a, b):
        """Return the division of a and b. Returns None if b is zero"""
        if b == 0:
            return None
        return a / b