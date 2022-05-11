# 1행의 합계를 계산



s = [[1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]]

rows = len(s)
cols = len(s[0])

i = 1
total = 0
for j in range(cols) :
    total = total +s[i][j]
print(total)

print()

# 3열의 합계를 계산

j = 3
total = 0
for i in range(rows) :
    total = total + s[i][j]
print(total)
