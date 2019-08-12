# the input parameter 
#   r1: the parallel resister of the RC module, the unit is Ω
#   r2: the series resister of the RC module, the unit is Ω
#   c1: the capacity of the RC module, the unit is F
#   u:  the input voltage of the circuit, the unit is V
#   t:  a time point after the voltage is set to u. It must be greater than zero
#   uc0:the initial voltage on the capacity.
#   t0: define the initial voltage time
# Output
#   uc0: the capacity voltage at t
# Description:
#   The zero time point was defined as the system change point. We simplified the system 
#   by define the source voltage change immediately.
from ParallelResister import parallel_resistance
from math import exp
def voltage_capacity(r1,r2,c1,u,t,uc0,t0):
    re = 0;  # the equivalent resister 
    tao = 0; # the constant time of the rc system
    parameter_a = 0; # the parameter 
    r_list = [r1,r2]
    re = parallel_resistance(r_list)
    r1_pl_r2    = r1 + r2
    r1_mp_r2    = r1 * r2
    tao         = re * c1
    temp0 = exp(t0 / tao)
    temp1 = r1*u/(r1+r2)
    parameter_a = temp0 * (uc0 - temp1)
    temp3 = exp(-1 * t /tao)
    uc = parameter_a * temp3 + temp1
    # print("the voltage of capacity at time ",t,"s is",uc,'V')
    return uc

