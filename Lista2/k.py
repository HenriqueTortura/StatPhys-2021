import numpy as np

#%%
def Create_Sequences(all_sequences, sequence, m, n, i, verbose = False):
    
    if i == n:
        if verbose: print(sequence)
        return np.concatenate((all_sequences, sequence))
    
    for j in range(m):
        sequence[:,i] = j
        all_sequences = Create_Sequences(all_sequences, sequence, m, n, i+1)
    
    return all_sequences

#%%

m = 4
n = 3
sequence = np.zeros((1,n), dtype=int)
all_sequences = np.zeros((1,n), dtype=int)

all_sequences = Create_Sequences(all_sequences, sequence, m, n, 0)
all_sequences =  np.delete(all_sequences, (0), axis=0)

#%%

print('Alfabeto de '+str(m)+' dígitos.')
print('Palavras com '+str(n)+' dígitos.')
print('Analítico: m^n = ', m**n)
      
print('Computacional:', np.size(all_sequences, axis=0))