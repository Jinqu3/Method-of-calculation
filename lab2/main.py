import copy
def GaussMethod(A:list,b:list,n:int)->list:
    for k in range(0, n):
        for i in range(k+1, n):
            coefficient = A[i][k] / A[k][k]
            for j in range(k, n):
                if k == j:
                    A[i][j] = 0
                    continue
                A[i][j] -= A[k][j] * coefficient
            b[i] -= b[k] * coefficient

    x = n * [0]
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += A[i][j] * x[j]
        x[i] = (b[i] - summ) / A[i][i]

    return x

def UpgradedGaussMethod(A:list,b:list,n:int)->list:
    order = [i for i in range(n)]

    for k in range(0, n):
        column = k
        row = k
        max_el = A[k][k]

        #нахождение максимального элемента в матрице
        for i in range(k,n):
            for j in range(k,n):
                if A[i][j] > max_el:
                    row = i
                    column = j
                    max_el = A[i][j]

        if k != row and k != column:
            # замена строк
            A[k],A[row] = A[row],A[k]
            b[k],b[row] = b[row],b[k]
            # замена столбцов
            for i in range(n):
                A[i][column],A[i][k] = A[i][k],A[i][column]
            order[k], order[column] = order[column], order[k]

        for i in range(k + 1, n):
            coefficient = A[i][k] / A[k][k]
            for j in range(k, n):
                if k == j:
                    A[i][j] = 0
                    continue
                A[i][j] -= A[k][j] * coefficient
            b[i] -= b[k] * coefficient

    x = n * [0]
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += A[i][j] * x[j]
        x[i] = (b[i] - summ) / A[i][i]

    return [x[i] for i in order]


def Determinant(A:list,b:list,n:int):
    for k in range(0, n):
        for i in range(k+1, n):
            coefficient = A[i][k] / A[k][k]
            for j in range(k, n):
                if k == j:
                    A[i][j] = 0
                    continue
                A[i][j] -= A[k][j] * coefficient
            b[i] -= b[k] * coefficient

    det = 1
    for i in range(n):
        det *= A[i][i]

    return det

def ReverseMatrix(A:list,n:int):    

    for i in range(n):
        A[i]+= [0]*n
        A[i][i+n] = 1
    
    for k in range(0, n):
        for i in range(k+1, n):
            coefficient = A[i][k] / A[k][k]
            for j in range(k, 2*n):
                if k == j:
                    A[i][j] = 0
                    continue
                A[i][j] -= A[k][j] * coefficient
            
    Reverse = [n * [0] for _ in range(n)]

    #k - столбец таблицы справа
    for k in range(0,n):
        x = n * [0]
        x[n - 1] = A[n - 1][k+n] / A[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            summ = 0
            for j in range(i + 1, n):
                summ += A[i][j] * x[j]
            x[i] = (A[i][k+n] - summ) / A[i][i]

        for i in range(n):
            Reverse[i][k] = x[i]

    return Reverse
    

if __name__ == '__main__':
    A = []

    f = open('lab2/matrix2.txt', 'r')
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        A.append(list(map(int, line.split())))

    b = list(map(int, f.read().split()))
    f.close()

    #rez = GaussMethod(copy.deepcopy(A),copy.deepcopy(b),n)
    #rez_upgrade = UpgradedGaussMethod(copy.deepcopy(A),copy.deepcopy(b),n)
    #det = Determinant(copy.deepcopy(A),copy.deepcopy(b),n)
    rev = ReverseMatrix(copy.deepcopy(A),n)
    for i in range(n):
        print(rev[i])