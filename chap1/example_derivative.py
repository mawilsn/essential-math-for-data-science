from sympy import *
from sympy.plotting import plot3d

x = symbols('x')
f = x**2

dx_f = diff(f)
print(dx_f)

x, y = symbols('x y')
f = 2*x**3 + 3*y**3
dx_f = diff(f, x)
dx_y = diff(f, y)

print(dx_f)
print(dx_y)

plot3d(f)
