import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def probability_density(i, alpha, I_0):
    
    rho = np.zeros(np.size(i))
    x = i[np.where(i > -I_0)]/I_0 + 1
    
    rho[np.where(i > -I_0)] = np.exp( -(1/(2*alpha**2))*np.log(x)**2 ) / ( I_0*np.sqrt(2*np.pi)*alpha*x )

    return rho


#%%
a = -5.0
b= 5.0
d = 0.001
num = (b-a)/d

i = np.linspace(a, b, num = int(num))

I_0 = [2,3,4]
alpha = [0.25, 0.5, 0.75]

rho = np.zeros((3, np.size(i)))
mode = np.zeros(3)
median = np.zeros(3)

for j in range(3):
    rho[j] = probability_density(i, alpha[j], I_0[2])
    mode[j] = I_0[2]*(np.exp(-alpha[j]**2) - 1)
    median[j] = I_0[2]*(np.exp(alpha[j]/2) - 1)
    print(median[j])
    print()
    
rho2 = np.zeros((3, np.size(i)))
mode2 = np.zeros(3)
median2 = np.zeros(3)

for j in range(3):
    rho2[j] = probability_density(i, alpha[2], I_0[j])
    mode2[j] = I_0[j]*(np.exp(-alpha[2]**2) - 1)
    median2[j] = I_0[j]*(np.exp(alpha[2]/2) - 1)
    
#%% Plotting
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(16,9))

for j in range(3):
    plt.plot(i, rho[j], label=r'$\alpha = {:<0.2f}$'.format(alpha[j]), linewidth=2)
    
    plt.vlines(mode[j], 0, np.max(rho[j]), color=colors[j], linewidth=2, linestyles='dashed')
    plt.text(mode[j], rho[j,np.where(rho[j]==np.max(rho[j]))]+0.02, r'$i_M={:<0.3f}$'.format(mode[j]),
             size = 16, verticalalignment='top', horizontalalignment='left', color=colors[j],
             bbox={'facecolor': 'white', 'alpha': 0.7, 'pad': 0.5, 'boxstyle': 'round'})
    
    plt.vlines(median[j], 0, rho[j,np.where(np.abs(i-median[j])<d)[0][0]],
               color=colors[j], linewidth=2, linestyles='dotted')
    plt.text(median[j], rho[j,np.where(np.abs(i-median[j])<d)[0][0]]+0.02,
             r'$<I>={:<0.3f}$'.format(median[j]), size = 16, verticalalignment='top',
             horizontalalignment='left', color=colors[j],
             bbox={'facecolor': 'white', 'alpha': 0.7, 'pad': 0.5, 'boxstyle': 'round'})
    
plt.title('Densidade de probabilidade da corrente, '+ r'$I(0) = 4$', fontsize=22)
plt.legend(loc='best', fontsize=18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.xlim(i[0], i[-1])
plt.ylim(0,0.45)
plt.xlabel(r'i', fontsize=18)
plt.ylabel(r'$\rho_I(i)$', fontsize=18)
plt.grid()

# plt.show()
plt.savefig('img/Densidade_I0cte.png', dpi=200, bbox_inches='tight')

#%% Plotting2
plt.figure(figsize=(16,9))

for j in range(3):
    plt.plot(i, rho2[j], label=r'$I(0) = {:<0.0f}$'.format(I_0[j]), linewidth=2)
    
    plt.vlines(mode2[j], 0, np.max(rho2[j]), color=colors[j], linewidth=2, linestyles='dashed')
    plt.text(mode2[j], rho2[j,np.where(rho2[j]==np.max(rho2[j]))]+0.02, r'$i_M={:<0.3f}$'.format(mode2[j]),
             size = 16, verticalalignment='top', horizontalalignment='left', color=colors[j],
             bbox={'facecolor': 'white', 'alpha': 0.7, 'pad': 0.5, 'boxstyle': 'round'})
    
    plt.vlines(median2[j], 0, rho2[j,np.where(np.abs(i-median2[j])<d)[0][0]],
               color=colors[j], linewidth=2, linestyles='dotted')
    plt.text(median2[j], rho2[j,np.where(np.abs(i-median2[j])<d)[0][0]]+0.02,
             r'$<I>={:<0.3f}$'.format(median2[j]), size = 16, verticalalignment='top',
             horizontalalignment='left', color=colors[j],
             bbox={'facecolor': 'white', 'alpha': 0.7, 'pad': 0.5, 'boxstyle': 'round'})
    
plt.title('Densidade de probabilidade da corrente, '+ r'$\alpha = 0.75$', fontsize=22)
plt.legend(loc='best', fontsize=18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.xlim(i[0], i[-1])
plt.ylim(0,0.45)
plt.xlabel(r'i', fontsize=18)
plt.ylabel(r'$\rho_I(i)$', fontsize=18)
plt.grid()

# plt.show()
plt.savefig('img/Densidade_alphacte.png', dpi=200, bbox_inches='tight')