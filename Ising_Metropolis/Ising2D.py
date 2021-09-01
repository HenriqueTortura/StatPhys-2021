import numpy as np
import scipy as sp
import time
import matplotlib.pyplot as plt

from Metropolis import metropolis_for_2d_ising as m2di
print(m2di.__doc__)
# print(Metropolis.metropolis_for_2d_ising.__doc__)

#%%

H = 0
k_B = 1
J = 1

L = 100
T = 2.5
t_END = 10**8

#%%
Energy, Magnetization = m2di.metropolis(J, H, k_B, T, L, t_END)

#%%
e = Energy[::10**4]/L**2
m = Magnetization[::10**4]/L**2