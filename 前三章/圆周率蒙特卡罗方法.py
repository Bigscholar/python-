#圆周率计算.py
#蒙特卡罗方法：随机撒点
import random
N = 30000000
cir = 0
for i in range(N):
    x = random.random()
    y = random.random()
    if (pow(x, 2) + pow(y, 2)) <= 1:
        cir += 1
print("循环{}次时圆周率近似值：{}".format(N, 4 * (cir / N)))
