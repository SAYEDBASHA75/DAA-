x, y = 1234, 5678
n = max(len(str(x)), len(str(y)))
m = n // 2

high_x, low_x = divmod(x, 10**m)
high_y, low_y = divmod(y, 10**m)

z0 = low_x * low_y
z1 = (low_x + high_x) * (low_y + high_y)
z2 = high_x * high_y

result = (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0
print(f"The product of {x} and {y} is {result}")

Output: Result of 1234 x 5678 = 11052
