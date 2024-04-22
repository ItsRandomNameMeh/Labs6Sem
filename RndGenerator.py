import numpy.random
import simpy
import math
а=16070093
b=453816693
k=31


#Очередь не ограниченная.
def Ans():
    lyam, T = read_input_from_file("Lab3Secpart.txt")
    n = 10  # менеджеров
    m = 1  # сколько компаний за раз обслуживает один менеджер
    myu = 1/T
    po = lyam / myu
    pon = po / n
    p_0 = 0
    x_min = 0.6
    x_max =  1.5
    BetterAns = 3.9 #предпочтительный результат в конце (для проверки?)
    if pon < 1:
        for k in range(4):
            p_0 += po**k/math.factorial(k)
        p_0 += po**(n+1)/(math.factorial(n)*(n-po))
        p_0 = 1/p_0
        p_och = po**(n+1)/(math.factorial(n)*(n-po)) * p_0
        L_och = n/(n-po)*p_och
        T_och = L_och/lyam
        L_smo = L_och+po
        T_smo = T+T_och


def read_input_from_file(filename):
    with open(filename, 'r') as file:
            lines = file.readlines()
            first_param = float(lines[0].strip())
            second_param = float(lines[1].strip())
    return first_param, second_param

Ans()