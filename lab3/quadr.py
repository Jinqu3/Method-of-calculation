from math import *

def sign(a):
    if a > 0.0:
        return 1
    if a < 0.0:
        return -1
    return 0

with open("B:\Универ\МетодыВыч\Method-of-calculation\lab3\matrix.txt", "r") as fin:
    n = int(fin.readline())

    A = [[0 for j in range(n+1 + 1)] for i in range(n+1)]

    for i in range(1, n+1):
        row = fin.readline().split()
        for j in range(1, n+2):
            A[i][j] = float(row[j - 1])

S = [[0 for j in range(n+1)] for i in range(n+1)]
D = [[0 for j in range(n+1)] for i in range(n+1)]

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

y = [0] *(n+1)
y[1] = A[1][n+1] / (S[1][1] * D[1][1])
for i in range(2, n + 1):
    summa = 0
    for k in range(1, i):
        summa += S[k][i] * y[k] * D[k][k]
    y[i] = (A[i][n+1] - summa) / (S[i][i] * D[i][i])

x = [0] *(n+1)
x[n] = y[n] / S[n][n]
for i in range(n-1, 0, -1):
    summa = 0
    for k in range(i + 1, n + 1):
        summa += S[i][k] * x[k]
    x[i] = (y[i] - summa) / S[i][i]

for i in range(1, n + 1):
    print(x[i])
