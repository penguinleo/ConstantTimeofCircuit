from ParallelResister import parallel_resistance
from ConstantTime import constant_time
from VoltageCapacity import voltage_capacity
from math import exp
x = [1000,1000,1000,1000]
re = parallel_resistance(x)
c = 5
t = constant_time(re,c)
x = exp(1)
print(x)
uc = voltage_capacity(51000,5000,0.000001,5,0.001,0,0)
