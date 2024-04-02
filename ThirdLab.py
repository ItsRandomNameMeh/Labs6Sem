import math
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

num1()
num2()
num3()
num4()
num5()
num6()




