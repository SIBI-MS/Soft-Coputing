X = {}
Y = {}
Z = {}
C = {}

# Input fuzzy set X
print('Enter the fuzzy set X:')
for i in range(1, 5):
    X[i] = float(input('Enter the element: '))

# Input fuzzy set Y
print('Enter the fuzzy set Y:')
for i in range(1, 5):
    Y[i] = float(input('Enter the element: '))

print("Fuzzy set X:", X)
print("Fuzzy set Y:", Y)
print("\n")

# Function to calculate union of two fuzzy sets
def fuzzy_union(X, Y):
    return {i: max(X[i], Y[i]) for i in X}

# Function to calculate intersection of two fuzzy sets
def fuzzy_intersection(X, Y):
    return {i: min(X[i], Y[i]) for i in X}

# Function to calculate complement of a fuzzy set
def fuzzy_complement(Z):
    return {i: round(1 - Z[i], 2) for i in Z}

# Verify De Morgan's First Law
if fuzzy_complement(fuzzy_intersection(X, Y)) == fuzzy_union(fuzzy_complement(X), fuzzy_complement(Y)):
    print("De Morgan's First Law is verified")
    print("(X ^ Y)' =", fuzzy_complement(fuzzy_intersection(X, Y)))
    print("(X' U Y') =", fuzzy_union(fuzzy_complement(X), fuzzy_complement(Y)))
else:
    print("De Morgan's First Law is not verified")

# Verify De Morgan's Second Law
if fuzzy_complement(fuzzy_union(X, Y)) == fuzzy_intersection(fuzzy_complement(X), fuzzy_complement(Y)):
    print("\nDe Morgan's Second Law is verified")
    print("(X U Y)' =", fuzzy_complement(fuzzy_union(X, Y)))
    print("(X' ^ Y') =", fuzzy_intersection(fuzzy_complement(X), fuzzy_complement(Y)))
else:
    print("\nDe Morgan's Second Law is not verified")
