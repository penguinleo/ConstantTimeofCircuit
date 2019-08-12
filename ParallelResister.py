# input x is the resister list
# the unit of the resistance is Ω
def parallel_resistance(x):
    resister_number = len(x)
    r0 = 0;
    for i in range(0,resister_number):
        r0 = r0 + 1/x[i]
        pass
    re = 1 / r0
    # print('the resistance is:',re,'Ω')
    return re
