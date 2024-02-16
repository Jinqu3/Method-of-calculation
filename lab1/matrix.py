Matrix = []

f = open(r'E:\MetVich\lab1\lower.txt', 'r')
n = int(f.readline())
for i in range(n):
    line = f.readline()
    Matrix.append(list(map(int, line.split())))

b = list(map(int,f.read().split()))
f.close()

x = [b[0]/Matrix[0][0]]

for i in range(1,n):
    summ = 0
    for j in range(0,i):
        summ +=Matrix[i][j]*x[j]
    x.append((b[i]-summ)/Matrix[i][i])

print(x)
