# Полностью автоматическое создание трендов с matplotlib
import matplotlib.pyplot as plt # импортируем построитель графиков из библиотеки matplotlib
import numpy as np # импортируем библиотеку numpy для работы с массивами numpy
from sklearn.metrics import r2_score # функция для расчёта критерия r^2

# Массивы входных данных
# x = [15.03, 14.03,13.03,12.03,10.03,9.03,8.03, 7.03, 6.03,5.03,3.03,2.03,1.03,28.02,27.02,
#     26.02,24.02,23.02,22.02,21.02,20.02,19.02,17.02,16.02,15.02 ]
x = [1678881600,1678795200,1678708800,1678622400,1678449600, 1678363200, 1678276800, 1678276800, 1678104000, # c использованием Timestamp
1678017600, 1677844800, 1677758400, 1677672000, 1677585600, 1677499200, 1677412800, 1677240000,
1677153600, 1677067200, 1676980800, 1676894400, 1676808000, 1676635200, 1676548800, 1676462400]
y = [11.0122,10.9612,10.9558,11.0191, 11.0189, 10.8899, 10.9358, 10.9190, 10.8861, 10.9489,  10.9495, 10.8914,
     10.9403, 10.8129, 10.7419, 10.9444, 10.9442, 10.8568, 10.8817, 10.9184, 10.8678, 10.8175, 10.8173,
     10.9107, 10.8817]

# Массивы numpy по входным данным
numpy_x = np.array(x)
numpy_y = np.array(y)

# Линии тренда
# линейный (автоматическое создание)
set_line_by_data = np.polyfit(numpy_x, numpy_y, 1) # полином первой степени
linear_trend = np.poly1d(set_line_by_data) # снижение размерности до одномерного массива
print("{0}x + {1}".format(*set_line_by_data)) # формула

# полиномиальный
set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 6) # работа с полиномом 6 степени
polinom_trend = np.poly1d(set_polinom_by_data) # Рассчитать значение полинома в точках x
print("${0}x^6 + {1}x^5 + {2}x^4 + {3}x^3 + {4}x^2 + {5}x + {6}$".format(*set_polinom_by_data)) # формула

# логарифмический
set_log_by_data = np.polyfit(np.log(numpy_x), numpy_y, 1) # работа с полиномом 1 степени + логарифмирование x
log_trend = [set_log_by_data[0]*np.log(x) + set_log_by_data[1] for x in numpy_x] # создание одномерного массива для логарифмического тренда
print("${0}ln(x) + {1}$".format(*set_log_by_data))  # формула

# экспоненциальный
set_exp_by_data = np.polyfit(numpy_x, np.log(numpy_y), 1) # работа с полиномом 1 степени + логарифмирование
exp_trend = [np.exp(set_exp_by_data[1]) * np.exp(set_exp_by_data[0] * x) for x in numpy_x] # создание одномерного массива для экспоненциального тренда
print("${1}e^{0}x$".format(*set_exp_by_data))  # формула

# Расчёт R^2
linear_r2 = r2_score(numpy_y, linear_trend(numpy_x))
polinom_r2 = r2_score(numpy_y, polinom_trend(numpy_x))
log_r2 = r2_score(numpy_y, log_trend)
exp_r2 = r2_score(numpy_y, exp_trend)


# Отображение графиков
plt.figure(figsize=(13, 13)) # размер графика


# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 1)

# !!! Текущая ячейка - 1 (левый верхний график)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, linear_trend(numpy_x), linestyle='dashed', color="orange", label = 'linear trend') # линейный тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc='upper right', fontsize=12)
plt.title("Линейный \n$R^2=$" + str(linear_r2) + "\n{0}x + {1}".format(*set_line_by_data))

# !!! Текущая ячейка - 2
plt.subplot(2, 2, 2)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
x = np.linspace(numpy_x.min(), numpy_x.max()) # набор данных для x для большей гладкости графика (50 точек)
plt.plot(x, polinom_trend(x), linestyle='dashed', color="orange", label = 'polinomial trend') # полиномиальный тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Полиномиальный \n$R^2=$" + str(polinom_r2) + "\n${2}x^4 + {3}x^3$ + \n${4}x^2 + {5}x$ + \n${6}$".format(*set_polinom_by_data))

# !!! Текущая ячейка - 3
plt.subplot(2, 2, 3)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, log_trend, linestyle='dashed', color="orange", label = 'log trend') # логарифмический тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'upper right', fontsize=12)
plt.title("Логарифмический \n$R^2=$" + str(log_r2) + "\n${0}ln(x) + {1}$".format(*set_log_by_data))

# !!! Текущая ячейка - 4
plt.subplot(2, 2, 4)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, exp_trend, linestyle='dashed', color="orange", label = 'exp trend')
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Экспоненциальный \n$R^2=$" + str(exp_r2) + "\n{1}e^({0}x)".format(*set_exp_by_data))

fig = plt.gcf() # Взять текущую фигуру
fig.set_size_inches(10, 10) # Задать размеры графика

# Покажем окно с нарисованным графиком
plt.show()