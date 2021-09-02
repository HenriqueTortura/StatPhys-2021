import numpy as np
import scipy as sp
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

from Metropolis import metropolis_for_2d_ising as m2di
print(m2di.__doc__)
# print(Metropolis.metropolis_for_2d_ising.__doc__)


#%% Plots
def Plot_Tarefa_1(Title, T, x):
    
    if Title == 'Energia':
        label = '$E/N$'
        lim = [-2,-0.7]
    elif Title == 'Magnetização':
        label = '$M/N$'
        lim = [-0.3,1]
        
    plt.figure(figsize=(4,3))
    plt.title(Title+', T='+str(T), fontsize=10)
    plt.plot(x, linewidth = 1)
    plt.ylabel(label, fontsize=10)
    plt.xlabel('Passos de Monte Carlo', fontsize=10)
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.ylim(lim[0],lim[1])
    plt.grid()
    plt.savefig('img/'+Title+'--T='+str.replace(str(T), '.', '_')+'.png', dpi=200, bbox_inches='tight')

def Plot_Tarefa_2(Title, t, y):
    
    if Title == 'Energia':
        label = r'$\left\langleE/N\right\rangle$'
        lim = [-2,-0.7]
    elif Title == 'Magnetização':
        label = r'$\left\langleM/N\right\rangle$'
        lim = [-0.3,1]
        
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']    
    
    fig = plt.figure(figsize=(16,9))
    ax = fig.add_axes([0, 0, 1, 1])
    plt.errorbar(t, y[:,0], yerr=y[:,1], ecolor=colors[1], linewidth=3)
    plt.ylabel(label, fontsize=28)
    plt.xlabel('T', fontsize=28)
    plt.xticks(ticks=np.linspace(2,3,11), fontsize = 26)
    plt.yticks(fontsize = 26)
    plt.ylim(lim[0],lim[1])
    plt.grid()
    plt.grid(axis='both', which='major', linestyle='--', color='#878787', linewidth=1.5)
    plt.grid(axis='both', which='minor', color='#adadad')
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    plt.savefig('img/'+Title+'transition.png', dpi=200, bbox_inches='tight')


#%% Parâmetros
H = 0
k_B = 1
J = 1

L = 100
t_END = 10**8


#%% Tarefa 1

for T in [2.1, 2.3, 2.5, 2.7, 2.9]: # Temperaturas a serem simuladas
    print('T = '+str(T))
    
    # Chama a subrotina para obter a Energia e Magnetização em cada passo
    Energy, Magnetization = m2di.metropolis(J, H, k_B, T, L, t_END)
    
    # Gera gráficos de energia e magnetização normalizados
    # pelo número de spins, L**2, e somente a cada passo de Monte Carlo
    Plot_Tarefa_1('Energia', T, Energy[::10**4]/(L**2))
    Plot_Tarefa_1('Magnetização', T, Magnetization[::10**4]/(L**2))

    
#%% Tarefa 2

n_points = 101 # Quantidade de pontos de temperatura entre 2 e 3
e = np.zeros((n_points, 2)) # Vetor para energia por temperatura
m = np.zeros((n_points, 2)) # Vetor para magnetização por temperatura
temperatures = np.linspace(2, 3, n_points) # Vetor de temperaturas

t_TRANS = 3*10**7 # Escolha do período transiente

# Laço pelas temperaturas
for i in range(n_points):
    print('T = '+str(temperatures[i]))
    
    # Chama a subrotina para obter a Energia e Magnetização em cada passo
    Energy, Magnetization = m2di.metropolis(J, H, k_B, temperatures[i], L, t_END)
    
    # Seleção e normalização das energias
    Energy_selected = Energy[3*10**7:]
    Energy_selected = Energy_selected[::int((t_END-t_TRANS)/(10**6))]/(L**2)
    e[i,:] = [Energy_selected.mean(), Energy_selected.std()]
    
    # Seleção e normalização das magnetizações
    Mag_selected = Magnetization[3*10**7:]
    Mag_selected = Mag_selected[::int((t_END-t_TRANS)/(10**6))]/(L**2)
    m[i,:] = [Mag_selected.mean(), Mag_selected.std()]
    
    
Plot_Tarefa_2('Energia', temperatures, e)
Plot_Tarefa_2('Magnetização', temperatures, m)
