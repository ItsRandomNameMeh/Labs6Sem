from pulp import LpVariable, LpProblem, LpMaximize, value
import time

start = time.time()
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
problem = LpProblem('0', LpMaximize)
problem += 10*x1 + 14*x2+12*x3, "Функция цели"
problem += 2*x1+4*x2+5*x3 <= 120, "1"
problem += x1+8*x2+6*x3 <= 280, "2"
problem += 7*x1+4*x2+5*x3 <= 240, "3"
problem += 4*x1+6*x2+7*x3 <= 360, "4"
problem.solve()
print("Результат :")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print("Прибыль:")
print(value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)