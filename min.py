R = []
S = []

r1 = int(input("Enter the row of the first matrix: "))
c1 = int(input("Enter the column of the first matrix: "))
r2 = int(input("Enter the row of the second matrix: "))
c2 = int(input("Enter the column of the second matrix: "))

print("Relation R")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(float(input("Enter the value: ")))
    R.append(row)

print("Relation S")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(float(input("Enter the value: ")))
    S.append(row)

result = []

for i in range(r1):
    result.append([])
    for j in range(c2):
        result2 = []
        for k in range(r2):
            result2.append(min(R[i][k], S[k][j]))
        result[i].append(max(result2))
    print("\n")

for row in result:
    print(*row)



