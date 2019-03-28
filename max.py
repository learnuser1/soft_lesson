#The author is zengyufeng
# The program is to figure the max sum in a list
# 'a' represent a list
def Max_Sum(a):
    max = a[0]
    sum = 0
    # to find a suitable max
    for i in range(0, len(a) - 1):
        sum += a[i + 1]
        # reset the value of sum to 0
        if sum < 0:
            sum = 0
        elif sum > max:
            max = sum
    return max
# to invoking the function and printf the max value
if __name__ == "__main__":
    c = Max_Sum([-1,-4, 2, 3, 0])
    print(c)