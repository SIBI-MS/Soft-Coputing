Z = {}
X = {}
Y = {}

# Input fuzzy set X
print('Enter the fuzzy set X:')
for i in range(1, 5):
    X[i] = float(input('Enter the element: '))

# Input fuzzy set Y
print('Enter the fuzzy set Y:')
for i in range(1, 5):
    Y[i] = float(input('Enter the element: '))

print(X)
print(Y)

# Union
print("Union:")
for i in range(1, 5):
    Z[i] = round(max(X[i], Y[i]), 2)
print(Z)

# Intersection
print("Intersection:")
for i in range(1, 5):
    Z[i] = round(min(X[i], Y[i]), 2)
print(Z)

# Algebraic Sum
print("Algebraic Sum:")
for i in range(1, 5):
    Z[i] = round(X[i] + Y[i] - (X[i] * Y[i]), 2)
print(Z)

# Bounded Sum
print("Bounded Sum:")
for i in range(1, 5):
    Z[i] = round(min(1, X[i] + Y[i]), 2)
print(Z)

# Bounded Difference
print("Bounded Difference:")
for i in range(1, 5):
    Z[i] = round(max(0, X[i] - Y[i]), 2)
print(Z)
