from math import ceil, sqrt, floor
b = -58996469
c = 478223210191071

b1 = floor((b + sqrt(pow(b, 2) - 4 * c))/2)
b2 = ceil((b - sqrt(pow(b, 2) - 4 * c))/2)

print(b1)
print(b2)
print(b1-b2+1)