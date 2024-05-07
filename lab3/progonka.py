n = int(input("Введите размер матрицы: "))
d = float(input("Введите параметр: "))
A = [0] * (n + 1)
B = [0] * (n + 1)
C = [0] * (n + 1)
F = [0] * (n + 1)
C[1] = 1
B[1] = -d
F[1] = 0

for i in range(2, n):
    A[i] = 1
    C[i] = -2
    B[i] = 1
    F[i] = 10 * ((i-1) / (n-1))**2

A[n] = 1
C[n] = -1
F[n] = 10

print("A:")
for i in range(2, n + 1):
    print(A[i], end=" ")
print()

print("C:")
for i in range(1, n + 1):
    print(A[i], end=" ")
print()

print("B:")
for i in range(1, n):
    print(A[i], end=" ")
print()

print("F:")
for i in range(1, n + 1):
    print(A[i], end=" ")
print()

x = [0] * (n + 1)
alpha = [0] * (n + 1)
beta = [0] * (n + 1)

alpha[1] = -B[1] / C[1]
beta[1] = F[1] / C[1]
for i in range(2, n):
    tmp = (C[i] + A[i] * alpha[i - 1])
    alpha[i] = -B[i] / tmp
    beta[i] = (F[i] - A[i] * beta[i - 1]) / tmp

x[n] = (F[n] - A[n] * beta[n - 1]) / (C[n] + A[n] * alpha[n - 1])
for i in range(n - 1, 0, -1):
    x[i] = alpha[i] * x[i + 1] + beta[i]

print("Решение:")
for i in range(1, n + 1):
    print(x[i])
