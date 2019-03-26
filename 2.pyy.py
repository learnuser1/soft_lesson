#!/user/bin/env python
# _*_ coding: utf-8 _*_
#!/user/bin/env python
# _*_ coding: utf-8 _*_
import random
a = ["+", "-"]
sum = 0
for i in range(0,10):
    b = random.randint(0,100)
    c = random.randint(0,b)
    s = random.choice(["+", "-"])
    if s == '+':
        if b >= 50:
            c = random.randint(0, 100-b)
        sum = b + c
    else:
        sum = b - c
    print(b,s,c,'=', sum)