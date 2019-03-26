a = [-1,-2,5,3,-4,-5]
max = a[0]
i = 0
for x in range(0,len(a)-1):
    if a[i] < 0:
        i+=1

sum = a[i]
print(sum)
while (i<len(a)-1):
    sum += a[i+1]
    if sum>max:
        max = sum
    i+=1
print(max)


