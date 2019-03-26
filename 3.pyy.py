#!/user/bin/env python
# _*_ coding: utf-8 _*_
import random
a = ["+", "-"]
sum = 0
for i in range(0,10):
    b = random.randint(0,100)
    c = random.randint(0,b)
    s = random.randint(0,1)
    sum = eval("%d%d%d"%(b,a[s],c))
    print(b,a[s],c,'=')