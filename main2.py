from cvxopt.modeling import variable, op
import time

start = time.time()
x = variable(3, 'x')
z=-(10*x[0] +14*x[1] + 12*x[2]) #Функция цели
mass1 = (2*x[0] + 4*x[1] + 5*x[2]  <= 120) #"1"
mass2 = (x[0] + 8*x[1] + 6*x[2]  <= 280 ) # "2"
mass3 = (7*x[0] + 4*x[1] + 5*x[2]  <= 240) #"3"
mass4 = (4*x[0] + 6*x[1] + 7*x[2]  <= 360)#"4"
x_non_negative = (x >= 0) #"5"
problem =op(z,[mass1,mass2,mass3,mass4, x_non_negative])
problem.solve(solver='glpk')
problem.status

print ("Прибыль:")
print(abs(problem.objective.value()[0]))
print ("Результат:")
print(x.value)
stop = time.time()
print ("Время :")
print(stop - start)