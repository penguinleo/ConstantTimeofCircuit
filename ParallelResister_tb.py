from ParallelResister import parallel_resistance
from ConstantTime import constant_time
from VoltageCapacity import voltage_capacity
from math import exp
import matplotlib.pyplot as plt
x = [1000,1000,1000,1000]
re = parallel_resistance(x)
c = 5
t = constant_time(re,c)
x = exp(1)
print(x)
uc = voltage_capacity(51000,5000,0.000001,5,0.001,0,0)

end_time = 0.05
step_time = 0.000001
number = int(end_time / step_time)
list_t = []
list_v = []
for n in range(0,number):
    t = 0 + n * step_time
    v = voltage_capacity(51000,5000,0.000001,5,t,0,0)
    list_v.append(v)
    list_t.append(t)
    pass
print("data length is:",number)
plt.figure("RC circuit")
plt.plot(list_t,list_v)
plt.show()