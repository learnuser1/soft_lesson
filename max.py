#!/user/bin/env python
# _*_ coding: utf-8 _*_
def max_sum(a):
    max = a[0]
    sum = 0
    for i in range(0, len(a) - 1):
        sum += a[i + 1]
        if sum < 0:
            sum = 0
        elif sum > max:
            max = sum
    return max
if __name__ == "__main__":
    c = max_sum([-1,-4,2,3,0])
    print(c)