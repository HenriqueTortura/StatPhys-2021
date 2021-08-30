import numpy as np
import scipy as sp
import time
import matplotlib.pyplot as plt

#%%
def Hamiltonian(J, H, spins):
    # kerr = 
    return -J* - H*np.sum(spins)

H = 0
k_B = 1
J = 1

L = 100
T = 2.5
t_END = 10**6

spins = np.ones((L,L), dtype=int)
Energy = np.zeros(t_END+1)
Energy[0] = 0

Magnetization = np.zeros(t_END+1)
Magnetization[0] = np.sum(spins)

e = Energy[0]

#%%
beginning = time.time()
# t_END = 1
for i in range(t_END):
    candidate = np.random.randint(0,L), np.random.randint(0,L)
    
    neighbors = np.array((np.roll(spins,1,0)[candidate], np.roll(spins,-1,1)[candidate],
                           np.roll(spins,-1,0)[candidate], np.roll(spins,1,1)[candidate]))
    
    Energy[i+1] = Energy[i]
    Delta_H = 2 * spins[candidate] * (J*np.sum(neighbors) + H)
    
    Magnetization[i+1] = Magnetization[i]
    
    # print(np.exp(-Delta_H/T))
    print(i/t_END)
    if (Delta_H < 0) or (np.random.random() <= np.exp(-Delta_H/(k_B*T))):
        # print('Transicionou')
        spins[candidate] = -1*spins[candidate]
           
        Energy[i+1] = Energy[i] + Delta_H
        Magnetization[i+1] = Magnetization[i] + 2*spins[candidate]

end = time.time()

print('Tempo do laço: '+str(end-beginning))

#%%

