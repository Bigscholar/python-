#DayDayUpQ3.py
#周中进步，周末退步
me = 1.0
dayfactor = 0.01
for i in range(365):
        if ( (i+1)%7 in [6,0] ):
            me *= 1-dayfactor
        else:
            me *= 1+dayfactor
print("一年之后，你的水平：{:.2f}".format(me))
