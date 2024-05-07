from math import *
def sign(a):
    if a == 0.0:
        return 0
    if a < 0.0:
        return -1
    return 1

n = int(input("Введите размер матрицы: "))
m = n + 1  # Расширенная матрица
A = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        A[i][j] = 1.0 / (i + j - 1)
print("Точное решение системы: ")
X = [0] * m
for i in range(1, n + 1):
    X[i] = 10 * i
    print(X[i], end=" ")
print()
for i in range(1, n + 1):
    summa = 0
    for j in range(1, m):
        summa += A[i][j] * X[j]
    A[i][m] = summa

S = [[0 for j in range(m)] for i in range(m)]
D = [[0 for j in range(m)] for i in range(m)]

S[1][1] = sqrt(abs(A[1][1]))
D[1][1] = sign(A[1][1])
for j in range(2, n + 1):
    S[1][j] = A[1][j] / (S[1][1] * D[1][1])

for i in range(2, n + 1):
    summa = 0
    for l in range(1, i):
        summa += S[l][i] * S[l][i] * D[l][l]
    S[i][i] = sqrt(abs(A[i][i] - summa))
    D[i][i] = sign(A[i][i] - summa)

    for j in range(i + 1, n + 1):
        summa = 0
        for k in range(1, i):
            summa += S[k][i] * S[k][j] * D[k][k]
        S[i][j] = (A[i][j] - summa) / (S[i][i] * D[i][i])

y = [0] * m
y[1] = A[1][m] / (S[1][1] * D[1][1])
for i in range(2, n + 1):
    summa = 0
    for k in range(1, i):
        summa += S[k][i] * y[k] * D[k][k]
    y[i] = (A[i][m] - summa) / (S[i][i] * D[i][i])

x = [0] * m
x[n] = y[n] / S[n][n]
for i in range(n-1, 0, -1):
    summa = 0
    for k in range(i + 1, n + 1):
        summa += S[i][k] * x[k]
    x[i] = (y[i] - summa) / S[i][i]

print("Расчитанное решение системы: ")
for i in range(1, n + 1):
    print(x[i])

summa = 0
for i in range(1, n + 1):
    summa += (abs(x[i] - X[i]) * (abs(x[i] - X[i])))
norma = sqrt(summa)
print("Евклидова норма разностей рассчитанного и точного решений:", norma)
