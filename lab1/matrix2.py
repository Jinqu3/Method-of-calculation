Matrix = []

f = open(r"E:\MetVich\lab1\upper.txt", 'r')
n = int(f.readline())
for i in range(n):
    line = f.readline()
    Matrix.append(list(map(int, line.split())))

b = list(map(int,f.read().split()))

f.close()

x = n*[0]
x[n-1] = b[n-1]/Matrix[n-1][n-1]

for i in range(n-2,-1,-1):
    summ = 0
    for j in range(i+1,n):
        summ +=Matrix[i][j]*x[j]
    x[i] = (b[i]-summ)/Matrix[i][i]

print(x)
