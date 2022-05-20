# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def poisson():
    #生成符合泊松分布的车辆队列
    lam = 1  # 参数为1的泊松过程
    n = 150  # 一个周期共通过150台车辆
    # 150 个参数为 lam 的指数分布随机数
    r = np.random.exponential(1 / lam, size=n)
    # 150台车辆的到达时刻
    t = np.hstack([[0], np.cumsum(r)])
    return t

def arrange(buffer, status):
    if status == 0:
        buffer[0] += 1
    if status == 1:
        if(buffer[0] < 4):
            buffer[0] += 1
        else:
            buffer[1] += 1
    if status == 2:
        buffer[1] += 1
    if status == 3 or status == 4:
        buffer[2] += 1
    if status == 5 or status == 6:
        if (buffer[3] < 4):
            buffer[3] += 1
        else:
            buffer[4] += 1
    return buffer


yo = []
ya = []
sumrate = []
for i in range(0, 50):
    sumo = 0
    suma = 0
    t = poisson()
    buffero = [0, 0, 0, 0, 0, 0]
    buffera = [0, 0, 0, 0, 0, 0]
    for j in range(0, 150):
        r = np.random.randint(0, 9)
        print("第{}次测试 第{}s 状态为{}".format(i, j, r))
        #道路堵塞量缓存
        if j < 20:
            if(r < 5):
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)
            for k in range(0, 6):
                if (buffero[k] > 4):
                    sumo += buffero[k] - 4
                if (buffera[k] > 4):
                    suma += buffera[k] - 4

        elif j < 38:
            if(j == 20):
                buffera[3] = 0

            if (r < 3):
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)
            if r == 3 or r == 4:
                buffero = arrange(buffero, r)
            if r == 5 or r == 6:
                buffera = arrange(buffera, r)
            for k in range(0, 6):
                if (buffero[k] > 4):
                    sumo += buffero[k] - 4
                if (buffera[k] > 4):
                    suma += buffera[k] - 4

        elif j < 60:
            if (j == 38):
                buffero[3] = 0

            if (r < 3):
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)
            if r == 5 or r == 6:
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)
            for k in range(0, 6):
                if (buffero[k] > 4):
                    sumo += buffero[k] - 4
                if (buffera[k] > 4):
                    suma += buffera[k] - 4

        elif j < 75:
            if (j == 60):
                buffera[0] = 0
                buffera[1] = 0
                buffera[2] = 0

            if (r < 3):
                buffero = arrange(buffero, r)
            if r == 3 or r == 4:
                buffera = arrange(buffera, r)
            if r == 5 or r == 6:
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)
            for k in range(0, 6):
                if (buffero[k] > 4):
                    sumo += buffero[k] - 4
                if (buffera[k] > 4):
                    suma += buffera[k] - 4

        else:
            if (j == 75):
                buffero[0] = 0
                buffero[1] = 0
                buffero[2] = 0

            if r == 3 or r == 4:
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)
            if r == 5 or r == 6:
                buffero = arrange(buffero, r)
                buffera = arrange(buffera, r)

            for k in range(0, 6):
                if (buffero[k] > 4):
                    sumo += buffero[k] - 4
                if (buffera[k] > 4):
                    suma += buffera[k] - 4

    yo.append(sumo)
    ya.append(suma)
    sumrate.append((suma -sumo) / sumo)


x = list(range(1, 51))
# 作图显示
plt.figure(1)
plt.plot(x, yo, color="blue", linewidth=1.5, linestyle="-", label="Our Schedule")
plt.plot(x, ya, color="red", linewidth=1.5, linestyle="-", label="Average Schedule")
plt.legend(loc='upper left')
plt.xlim(0, 51)
plt.savefig('./result_1.jpg')

plt.figure(2)
plt.plot(x, sumrate, color="blue", linewidth=1.5, linestyle="-", label="Average Rate")
plt.legend(loc='upper left')
plt.xlim(0, 51)
plt.savefig('./result_2.jpg')

plt.show()
