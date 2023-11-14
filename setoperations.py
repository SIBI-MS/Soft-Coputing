X = {'a': 0.7, 'b': 0.3, 'c': 0.2}
Y = {'a': 0.5, 'b': 0.2, 'c': 0.4}
Z = {}

# Union
print("Union:")
for i in X and Y:
    Z[i] = max(X[i], Y[i])
print(Z)

# Intersection
print("Intersection:")
for i in X and Y:
    Z[i] = min(X[i], Y[i])
print(Z)

# Algebraic Sum
print("Algebraic Sum:")
for i in X.keys():
    Z[i] = X[i] + Y[i] - (X[i] * Y[i])
print(Z)

# Bounded Sum
print("Bounded Sum:")
for i in X and Y:
    Z[i] = round(min(1, X[i] + Y[i]), 2)
print(Z)

# Bounded Difference
print("Bounded Difference:")
for i in X and Y:
    Z[i] = round(max(0, X[i] - Y[i]), 2)
print(Z)
