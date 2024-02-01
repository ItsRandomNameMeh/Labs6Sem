from scipy.optimize import linprog
import time
start = time.time()
c = [-10, -14, -12] #Функция цели
A_ub = [[2, 4, 5],
        [1, 8, 6],
        [7, 4, 5],
        [4, 6, 7]]  #'1, 2, 3 левая часть'
b_ub = [120, 280, 240, 360] #'1, 2, 3, 4 правая часть'
print (linprog(c, A_ub, b_ub))
stop = time.time()
print ("Время :")
print(stop - start)