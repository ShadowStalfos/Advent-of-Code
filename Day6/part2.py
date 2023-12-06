from math import ceil, sqrt, floor
A = -1
B = 58996469
C = -478223210191071
D = B**2-4*A*C
a = ceil((-B+sqrt(D))/(2*A))
b = floor((-B-sqrt(D))/(2*A))
print(a)
print(b)
print(b-a)