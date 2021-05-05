import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def Exponential(x, l):
    return l*np.exp(-l*x)

def Standard(x, mu, sigma):
    return np.exp(-((x-mu)**2)/(2*sigma**2)) / (np.sqrt(2*np.pi)*sigma)


# N = int(input('Quantidade de números uniformemente distribuídos: '))
N = 1000000

delta = float(input('Largura de cada céula a ser populada: '))

# M_x = float(input('Ponto de corte da distribuição exponencial: '))
M_x = 6

# M_z = float(input('Ponto de corte da distribuição padrão: '))
M_z = 3
    
# Gera duas sequências de N números uniformemente distribuídos entre 0 e 1
u1 = np.random.rand(N)
u2 = np.random.rand(N)

# Gera a sequência transformada para a distribuição exponencial
x = -np.log(u1)
# Gera a sequência transformada para a distribuição padrão por Box-Muller
z = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)

# Corta a sequência além do ponto de corte da distribuição exponencial (M_x)
x = np.delete(x, np.where(x>M_x))
# e do ponto de corte da distribuição padrão (M_z)
z = np.delete(z, np.where(np.abs(z)>M_z))

# Calcula o número de células/colunas no histograma de acordo com o delta dado
xbins = int((np.max(x)-np.min(x)) / delta)
zbins = int((np.max(z)-np.min(z)) / delta)

#%% Plotting Z
fig = plt.figure(figsize=(16,9))
ax = fig.add_axes([0, 0, 1, 1])

# Obtem o histograma para a distribuição padrão
z_data = plt.hist(z, bins=zbins, density=True, align='mid',
                  label='Histograma')

# Correção para tomar o ponto x do meio de cada célula
z_x = np.delete(z_data[1], -1) + delta/2 

# Obtem os parâmetros da média e desvio padrão do fit
z_estimation, pcov  = curve_fit(Standard, z_x, z_data[0])

label1 = 'Fit: '+r'$\frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$'
label2 = r'$\mu =$'+'{:.2e}'.format(z_estimation[0])
label3 = r'$\sigma =$'+'{:.2e}'.format(z_estimation[1])

z_x = np.linspace(-M_z, M_z, num = 10000)
plt.plot(z_x, Standard(z_x, z_estimation[0], z_estimation[1]), linewidth = 3,
         label=label1, color='#ff7f0e')

plt.text(0.8325,0.95, label2+'\n'+label3, size = 24, verticalalignment='top',
         horizontalalignment='left', transform = ax.transAxes,
         bbox={'facecolor': 'white', 'alpha': 0.7, 'pad': 0.5,
               'boxstyle': 'round', 'ec': '#ff7f0e', 'lw': 2})

# plt.title('Distribuição Padrão com '+r'$N={:.0e}$'.format(N)+' e '+r'$\delta={:.0e}$'.format(delta),
          # fontsize=26)
plt.vlines([-M_z,M_z], 0, 0.2, linewidth=3, color='red', linestyles='dashed')
plt.text(M_z,0.2, 'M', size = 22, verticalalignment='bottom', color='red',
         horizontalalignment='center')
plt.text(-M_z,0.2, '-M', size = 22, verticalalignment='bottom', color='red',
         horizontalalignment='center')

plt.legend(loc='upper left', fontsize=24)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.xlabel(r'$x$', fontsize=18)
plt.grid()
plt.savefig('img/Distribuicao_Normal_delta'+'{:.0e}'.format(delta)+'.png', dpi=200, bbox_inches='tight')

#%% Plotting X
fig = plt.figure(figsize=(16,9))
ax = fig.add_axes([0, 0, 1, 1])
x_data = plt.hist(x, bins=xbins, density=True, align='mid',
                  label='Histograma')

x_x = np.delete(x_data[1], -1) + delta/2
x_estimation, pcov  = curve_fit(Exponential, x_x, x_data[0])

label1 = 'Fit: '+r'$\lambda e^{-\lambda x}$'
label2 = r'$\lambda =$'+'{:.3e}'.format(x_estimation[0])

x_x = np.linspace(0, M_x, num=10000)
plt.plot(x_x, Exponential(x_x, x_estimation[0]), linewidth = 3,
         label=label1, color='#ff7f0e')

plt.text(0.5,0.75, label2, size = 24, verticalalignment='top',
         horizontalalignment='center', transform = ax.transAxes,
         bbox={'facecolor': 'white', 'alpha': 0.7, 'pad': 0.5,
               'boxstyle': 'round', 'ec': '#ff7f0e', 'lw': 2})

# plt.title('Distribuição Exponencial com '+r'$N={:.0e}$'.format(N)+' e '+r'$\delta={:.0e}$'.format(delta),
          # fontsize=26)
plt.vlines(M_x, 0, 0.2, linewidth=3, color='red', linestyles='dashed')
plt.text(M_x,0.2, 'M', size = 22, verticalalignment='bottom', color='red',
         horizontalalignment='center')

plt.legend(loc='upper center', fontsize=24)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.xlabel(r'$x$', fontsize=18)
plt.grid()
plt.savefig('img/Distribuicao_Exponencial'+'{:.0e}'.format(delta)+'.png', dpi=200, bbox_inches='tight')