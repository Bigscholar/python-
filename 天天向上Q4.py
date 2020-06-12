#天天向上Q4.py
A=pow(1.01,365)
dayfactor=0.01
def dayup(dayfactor):
    B=1.0
    for i in range(365):
        if((i+1)%7 in [0,6]):
            B*=0.99
        else:
            B*=1+dayfactor
    return B
while(dayup(dayfactor)<A):
    dayfactor+=0.0001
print("B君需要每天努力{:.3f}".format(dayfactor))
