import math
import simpy
import numpy as np
import random

NO_OF_BUSINESS = int(input("Введите количество компаний, участвующих в "
                       "моделировании: "))
NO_OF_MANAGERS = 10  # manager counts
service_wait_time = []  #list to hold the time until a manager is available and will be to server the customer
invite_wait_time = []    #list to hold the time until the queue pass



def num1():
    print("\n\nTask1")
    lyam, T = read_input_from_file("Num1.txt")
    myu = 1/T
    a = "Вероятность обслуживания " + str(round(myu/(lyam+T),3))
    b = "Вероятность отказа " + str(round(1-myu/(lyam+T),3))
    c = "Их отношение "+str(round(myu/(lyam+T)/(1-myu/(lyam+T)),3))
    print(a,"\n",b,"\n",c)

def num2():
    print("\n\nTask2")
    lyam, T = read_input_from_file("Num2.txt")
    myu = 1/T
    p_intesiv =  lyam/myu
    L_queue = 3
    Q = round(1 - (1 - myu / (lyam + T)),3)
    ABC = round(Q*lyam,3)
    p0 = (1-p_intesiv)/(1-p_intesiv**(L_queue+1))
    a = "Вероятность обслуживания " + str(round(1-p_intesiv**(L_queue+1)*p0, 3))
    b = "Вероятность отказа " + str(round(p_intesiv**(L_queue+1)*p0, 3))
    c = "Их отношение " + str(round(myu / (lyam + T) / (1 - myu / (lyam + T)), 3))
    print( a, "\n", b, "\n", c,"\n", ABC,"\n", Q)

def num3():
    print("\n\nTask3")
    lyam, T = read_input_from_file("Num3.txt")
    myu = 1/T
    p_intesiv = lyam / myu
    L_queue = p_intesiv**2/(1-p_intesiv)
    T_queue = L_queue/lyam
    L_smo = p_intesiv/(1-p_intesiv)
    T_smo = L_smo/lyam
    a = round(myu/(T+lyam), 3)
    b = (round(1-myu/(T+lyam), 3))
    c = a/b
    print("Вероятность обслуживания: "+str(a)+"\n Вероятность отказа: "+str(b)+"\n Их отношение: "+str(round(c,3)))

def num4():
    print("\n\nTask4")
    lyam, T = read_input_from_file("Num4.txt")
    myu = 1/T
    a = myu/(lyam+myu)
    b = 1-a
    APS = lyam*myu/(lyam+myu)
    print("Вероятность обслуживания: "+str(round(a,3))+"\n Вероятность отказа: "+str(round(b,3))+"\n Их отношение: "+str(round(a/b,3))+
          "\n Пропускна способсность: "+str(APS))

def num5():
    print("\n\nTask5")
    lyam, T = read_input_from_file("Num5.txt")
    myu = 1 / T
    n = 3 #Кол-во точек облсуживания
    po = lyam/myu
    pon = po/n
    p_0 = 0
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
        print("Вероятность образования очереди: "+str(round(p_och,3))+
              "\n Средняя длина очереди: "+str(round(L_och,3))+
              "\n Среднее время ожидания в очереди: "+str(round(T_och,3))+
              "\n Среднее число заявок в СМО: "+str(round(L_smo,3))+
              "\n Среднее время нахождения заявок в СМО: "+str(round(T_smo,3)))
    else:
        print("Постепенно очередь станет бесконечной, т.к po n = " + str(pon))

def num6():
    print("\n\nTask6")
    n = 2 #Кол-во точек облсуживания
    m = 5 #Макисмальная длина очереди
    lyam, T = read_input_from_file("Num6.txt")
    myu = 1 / T
    po = lyam / myu
    pon = po / n
    p_0 = 0
    if pon != 1:
        for k in range(4):
            p_0 += po**k/math.factorial(k)
        p_0 += po**(n+1)/(math.factorial(n)*(n-po)) * (1-(po/n)**m)
        p_0 = 1/p_0
        b = p_0 * po**(n+m)/(n**m*math.factorial(n)) #chanse of cancle
        L_och = (po**(n+1)/(n*math.factorial(n))) * (1-(po/n)**m*(m+1-m*po/n))/((1-po/n)**2)
        T_och = L_och/lyam
        T_smo = T_och+(1-b)/myu
        k_mid = lyam/myu*(1-b) #Среднее число занятых каналов
    else:
        for k in range(4):
            p_0 += po ** k / math.factorial(k)
        p_0 += m* po ** (n + 1) / (math.factorial(n) * n)
        p_0 = 1 / p_0
        L_och = (po**(n+1)/(n*math.factorial(n)))*m*(m+1)/2*p_0

    print("Вероятность обслуживания: " + str(round(1-b, 3)) +
          "\n Вероятность отказа: " + str(round(b, 3)) +
          "\n Средняя длина очереди: " + str(round(L_och, 3)) +
          "\n Среднее время ожидания очереди: " + str(round(T_och, 3))+
          "\n Среднее время нахождения заявки в СМО: " + str(round(T_smo,3)),
          "\n Среднее число занятых каналов: " + str(round(k_mid,3)))


def read_input_from_file(filename):
    with open(filename, 'r') as file:
            lines = file.readlines()
            first_param = float(lines[0].strip())
            second_param = float(lines[1].strip())
    return first_param, second_param






def PartTwo():
    m = 1 #company counts to 1 manager
    lyam = 0.9
    T = 45
    xmin = 0.6
    xmax = 1.5
    best = 3.9
    myu = 1/T
    p_intensiv = lyam/myu
    env = simpy.Environment()
    manager = simpy.Resource(env, NO_OF_MANAGERS)
    L_queue = p_intensiv ** 2 / (1 - p_intensiv)
    T_queue = L_queue / lyam
    generate_company(env, manager, xmin,xmax,best)
    time_interv(xmin, xmax, best)
    print("\n\nС %s менеджерами и %s компаниями..." % (NO_OF_MANAGERS, NO_OF_BUSINESS))
    print("Среднее время ожидания: %.1f минут." % (np.mean(service_wait_time)))
    print("Среднее время обслуживания: %.1f минут." % (np.mean(invite_wait_time)))


def time_interv(xmin, xmax, best):
    time_to_service = random.triangular(xmin, xmax, best)
    print(time_to_service)


def convert_to_hours(minutes):
    minutes %= 60
    return int(minutes)
def generate_company(env, manager, xmin, xmax, best):
    for i in range(NO_OF_BUSINESS):
        yield env.timeout(random.randint(xmin,xmax))
        env.process(company(env, i, company(env,i,xmin, xmax,best)))

def company(env, name, manager, xmin, xmax, best):
    minutes = convert_to_hours(env.now)
    print("Компания %s прибылаќ в %.1f" % (name, minutes))
    with manager.request() as req:
        start_time = env.now
        yield req
        invite_wait_time.append(env.now - start_time)
        time_to_service = random.triangular(xmin, xmax, best)
        yield env.timeout(time_to_service)
        print("Компания %s обслужена за %.1f минут" % (name, env.now - start_time))
        service_wait_time.append(env.now - start_time)

PartTwo()





lyam = 0.5  # интенсивность потока заявок
μ = 1/1.2  # интенсивность обслуживания


def source(env, lyam, server):
    """Генератор заявок"""
    i = 0
    while True:
        yield env.timeout(np.random.exponential(1/lyam))
        i += 1
        print(f'Заявка {i} поступила в {convert_to_hours(env.now)}')
        env.process(customer(env, f'Автомобиль {i}', server))

def customer(env, name, server):
    """Заявка"""
    arrive = env.now
    if server.count == 0:  # если сервер свободен, начинаем обслуживание
        with server.request() as req:
            service_time = np.random.exponential(1/μ)
            print(f'{name} начал обслуживание в {convert_to_hours(arrive)}, время обслуживания {round(service_time,3)}')
            yield req
            yield env.timeout(service_time)
            print(f'{name} закончил обслуживание в {convert_to_hours(env.now)}')
def convert_to_hours(minutes):
    hours = minutes // 60
    minutes %= 60
    return int(hours), int(minutes)
# Инициализация SimPy
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)  # одноканальная СМО
env.process(source(env, lyam, server))
env.run(until=100)  # моделирование на протяжении 100 часов



#num1()
num2()
#num3()
#num4()
#num5()
#num6()




