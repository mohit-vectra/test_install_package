import numpy as np
import sympy as sp
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    def np_infor(self):
        #print("Numpy version : ",np.__version__)
        result = np.add(10, 20)
        print(result)
        return result

    def symbolic_add(self, expr1, expr2):
        # Use sympy to add two symbolic expressions
        x, y = sp.symbols('x y')
        result = sp.simplify(expr1 + expr2)
        print("Symbolic add result: ", result)
        return result
