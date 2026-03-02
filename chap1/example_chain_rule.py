from sympy import *

x, y = symbols('x y')
# derivative for the first function
# need to underscore _y to prevent variable clash
_y = x**2 + 1
dy_dx = diff(_y)

# calculate the second function
z = y**3 - 2
dz_dy = diff(z)

# chain rule
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

print(dz_dx_chain)
print(dz_dx_no_chain)
