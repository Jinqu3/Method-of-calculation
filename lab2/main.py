
def GaussMethod(M:list,b:list,n:int)->list:
    for k in range(1,n):
        a = M[k-1][k-1]
        for i in range(k,n):
            coefficient = M[i][k-1]/a
            for j in range(k-1,n):
                M[i][j]-= M[k-1][j]*coefficient
            b[i] -= b[i-1]*coefficient

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

    f = open(r'D:\MetVich\lab2\matrix.txt', 'r')
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        Matrix.append(list(map(int, line.split())))

    b = list(map(int, f.read().split()))
    f.close()

    x = GaussMethod(Matrix,b,n)
    print(x)