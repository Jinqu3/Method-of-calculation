import numpy as np
def GaussMethod(M:list,b:list,n:int)->list:
    for k in range(0, n):
        for i in range(k+1, n):
            coefficient = M[i][k] / M[k][k]
            for j in range(k, n):
                if k == j:
                    M[i][j] = 0
                M[i][j] -= M[k][j] * coefficient
            b[i] -= b[k] * coefficient

    return answer(M,b,n)
def answer(M:list,b:list,n:int)->list:

    x = n * [0]
    x[n - 1] = b[n - 1] / Matrix[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += Matrix[i][j] * x[j]
        x[i] = (b[i] - summ) / Matrix[i][i]

    return x

if __name__ == '__main__':
    Matrix = []

    f = open('matrix2.txt', 'r')
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        Matrix.append(list(map(int, line.split())))

    b = list(map(int, f.read().split()))
    f.close()

    x = GaussMethod(Matrix,b,n)
    print(x)