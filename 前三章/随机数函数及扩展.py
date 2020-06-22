#随机函数及扩展.py
import random
import time

for i in range(5):
    print("不使用种子生成随机序列前两位：{:.2f}".format(random.random()))
    time.sleep(0.1)

#for i in range(5, 11):
#    random.seed(i)
#    print("种子{}生成的随机序列前两位为：{:.2f}".format(i, random.random()))

for i in range(5):
    print("10到100的随机数：{}".format(random.randint(10, 100)))

for i in range(5):
    print("10到100，步长为5随机数：{}".format(random.randrange(10, 100, 5)))

for i in range(2, 11, 2):
    print("生成比特长为{}的随机数：{}".format(i, random.getrandbits(i)))

for i in range(1, 5):
    print("生成从{}到{}的随机小数：{:.2f}".format(2 * i, 3 * (i + 1), random.uniform(i*2, (i+1)*3)))

print("choice函数：{}".format(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(s)
print(s)
