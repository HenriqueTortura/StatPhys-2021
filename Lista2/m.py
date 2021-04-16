import numpy as np

#%%
def Create_Sequences(alphabet, all_sequences, sequence, m, n, i, verbose = False):
    
    local_alphabet = alphabet
    
    if i == n:
        if verbose: print(sequence)
        return np.concatenate((all_sequences, sequence))
    
    if sequence[:,i-1] == 1:
        local_alphabet = np.delete(alphabet, np.where(alphabet == [1]), axis=0)
        
    for j in local_alphabet:
        sequence[:,i] = j
        all_sequences = Create_Sequences(alphabet, all_sequences, sequence, m, n, i+1)
    
    return all_sequences

#%%
m = 9
alphabet = np.arange(m)

n = 5

sequence = np.zeros((1,n), dtype=int)
all_sequences = np.zeros((1,n), dtype=int)

all_sequences = Create_Sequences(alphabet, all_sequences, sequence, m, n, 0)
all_sequences =  np.delete(all_sequences, (0), axis=0)

#%%
alpha = np.sqrt((m-1)*(m+3))

a = (m**2 + (alpha+1)*m - 2) / (alpha**2 + (m-1)*alpha)
b = (-m**2 + (alpha-1)*m + 2) / (-alpha**2 + (m-1)*alpha)

Analitical = a*((m-1+alpha)/2)**n + b*((m-1-alpha)/2)**n

print('Alfabeto de '+str(m)+' dígitos.')
print('Palavras com '+str(n)+' dígitos.')
print('Analítico:', Analitical)
      
print('Computacional:', np.size(all_sequences, axis=0))
