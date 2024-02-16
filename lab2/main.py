import numpy as np
def GaussMethod(M:list,b:list,n:int)->list:
    for k in range(0, n):
        for i in range(k+1, n):
            coefficient = M[i][k] / M[k][k]
            for j in range(k, n):
                if k == j:
                    M[i][j] = 0
                    continue
                M[i][j] -= M[k][j] * coefficient
            b[i] -= b[k] * coefficient

    return answer(M,b,n)

def UpgradedGaussMethod(M:list,b:list,n:int)->list:
    order = [i for i in range(n)]

    for k in range(0, n):
        column = k
        row = k
        max_el = M[k][k]

        #нахождение максимального элемента в матрице
        for i in range(k,n):
            for j in range(k,n):
                if M[i][j] > max_el:
                    row = i
                    column = j
                    max_el = M[i][j]

        if k != row and k != column:
            # замена строк
            M[k],M[row] = M[row],M[k]
            b[k],b[row] = b[row],b[k]
            # замена столбцов
            for i in range(n):
                M[i][column],M[i][k] = M[i][k],M[i][column]
            order[k], order[column] = order[column], order[k]

        for i in range(k + 1, n):
            coefficient = M[i][k] / M[k][k]
            for j in range(k, n):
                if k == j:
                    M[i][j] = 0
                    continue
                M[i][j] -= M[k][j] * coefficient
            b[i] -= b[k] * coefficient

    return answer(M, b,order, n)
def answer(M:list,b:list,order:list,n:int)->list:

    x = n * [0]
    x[n - 1] = b[n - 1] / M[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += M[i][j] * x[j]
        x[i] = (b[i] - summ) / M[i][i]

    return [x[i] for i in order]

if __name__ == '__main__':
    Matrix = []

    f = open('matrix2.txt', 'r')
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        Matrix.append(list(map(int, line.split())))

    b = list(map(int, f.read().split()))
    f.close()

    #x = GaussMethod(Matrix.copy(),b.copy(),n)
    y = UpgradedGaussMethod(Matrix.copy(),b.copy(),n)
    print(y)