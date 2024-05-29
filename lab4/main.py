import numpy as np
from math import sqrt

def norm(a):
    # sum = 0
    # for i in a:
    #     sum += i*i
    # print(sum(a[i]*a[i] for i in range(len(a))))
    return sqrt(sum(a[i]*a[i] for i in range(len(a))))

def seidel_solver(A, b, n, epsilon, itmax):
    x = [0]*n
    it = 0
    while it < itmax:
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] =  (b[i] - s1 - s2) / A[i][i]
        
        dx = norm(np.array(x_new) - np.array(x))

        if dx < epsilon:
            break
        
        x = x_new
        it += 1
    
    return x, it, dx

def relaxation_solver(A, b, n, omega, epsilon, itmax):
    x = [0]*n
    it = 0
    while it < itmax:
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1 - omega) * x[i] + omega * ( (b[i] - s1 - s2)/ A[i][i] )
        
        dx = norm(np.array(x_new) - np.array(x))

        if dx < epsilon:
            break
        
        x = x_new
        it += 1
    
    return x, it, dx


def optimal_omega(A, b, omega_start=0.1, omega_end=2.0, omega_step=0.1):
    best_omega = omega_start
    dx_min_over_all_omegas = float('inf')
    for omega in np.arange(omega_start, omega_end, omega_step):
        x = [0]*n
        it = 0
        dx_min_for_current_omega = 1
        while it < 5:
            x_new = x.copy()
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (1 - omega) * x[i] + omega * ( (b[i] - s1 - s2)/ A[i][i] )
        
            dx = norm(np.array(x_new) - np.array(x))

            if dx < dx_min_for_current_omega:
                dx_min_for_current_omega = dx
        
            x = x_new
            it += 1

        if dx_min_for_current_omega < dx_min_over_all_omegas:
            dx_min_over_all_omegas = dx_min_for_current_omega
            best_omega = omega

    return best_omega

# Входные данные
n = 3

# A_relax = [[ 2,-1, 0 ],
#            [-1, 2,-1 ],
#            [ 0,-1, 2 ]]
# b_relax = [0.3333333333,1,-0.3333333333]


# A_seidel = [[ 2,-1, 0 ],
#            [-1, 2,-1 ],
#            [ 0,-1, 2 ]]
# b_seidel = [0.3333333333,1,-0.3333333333]

A_relax = [[2.56,0.67,-1.78],[0.67,-2.67,1.35],[-1.78,1.35,-6.55]]
b_relax = [1.14,0.66,1.72]

# A_relax = [[1,0,0],[0,1,0],[0,0,1]]
# b_relax= [1,2,3]

# A_seidel = [[1,0,0],[0,1,0],[0,0,1]]
# b_seidel = [1,2,3]

# A_relax = [[-1,0,0],[0,-1,0],[0,0,-1]]
# b_relax = [-1,-2,-3]
# A_seidel = [[-1,0,0],[0,-1,0],[0,0,-1]]
# b_seidel = [-1,-2,-3]

# A_relax = [[3,1,1],[1,3,1],[1,1,3]]
# b_relax= [8,10,12]
# A_seidel = [[3,1,1],[1,3,1],[1,1,3]]
# b_seidel = [8,10,12]

# print(f"Матрица для метода Зейделя:\n {A_seidel}")
# print(f"Вектор b для метода Зейделя:\n {b_seidel}")
print(f"Матрица для метода релаксации:\n {A_relax}")
print(f"Вектор b для метода релаксации:\n {b_relax}\n")
epsilon = float(input("Введите параметр ε для окончания итераций: "))
itmax = int(input("Введите максимальное число итераций (itmax): "))

# Решение методом Зейделя
# print("\nМетод Зейделя:")
# x_seidel, it_seidel, dx_seidel = seidel_solver(A_seidel, b_seidel, n, epsilon, itmax)
# print("Решение (вектор x):")
# print(x_seidel)
# print("Количество итераций (it):", it_seidel)
# print("Норма разности двух последних итераций для x:", dx_seidel)

# # Проверка условия окончания итераций
# if it_seidel == itmax:
#     print("\nВнимание: метод Зейделя достиг максимального числа итераций без удовлетворения критерия сходимости.")
#     if dx_seidel >= epsilon:
#         print("Условие окончания итераций с ε не выполнено.")
#     else:
#         print("Хотя итерации не завершились, норма разности последних итераций меньше ε.")

# Поиск оптимального omega для метода релаксации
omega = optimal_omega(A_relax, b_relax)
print("\nОптимальное значение параметра релаксации (omega):", omega)

# Решение методом релаксации с оптимальным omega
print("\nМетод релаксации:")
x_relax, it_relax, dx_relax = relaxation_solver(A_relax, b_relax, n, omega, epsilon, itmax)
print("Решение (вектор x):")
print(x_relax)
print("Количество итераций (it):", it_relax)
print("Норма разности двух последних итераций для x:", dx_relax)

if it_relax == itmax:
    print("\nВнимание: метод релаксации достиг максимального числа итераций без удовлетворения критерия сходимости.")
    if dx_relax >= epsilon:
        print("Условие окончания итераций с ε не выполнено.")
    else:
        print("Хотя итерации не завершились, норма разности последних итераций меньше ε.")