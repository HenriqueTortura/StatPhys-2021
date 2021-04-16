import numpy as np

#%%
def Create_Binary_Sequences(all_sequences, sequence, n, i, verbose = False):
    
    if i == n:
        if verbose: print(sequence)
        return np.concatenate((all_sequences, sequence))
    
    for j in range(2):
        sequence[:,i] = j
        all_sequences = Create_Binary_Sequences(all_sequences, sequence, n, i+1)
    
    return all_sequences

#%%

n = 3
sequence = np.zeros((1,n), dtype=int)
all_sequences = np.zeros((1,n), dtype=int)

all_sequences = Create_Binary_Sequences(all_sequences, sequence, n, 0)
all_sequences =  np.delete(all_sequences, (0), axis=0)

#%%

print('Alfabeto de binário.')
print('Palavras com '+str(n)+' dígitos.')
print('Analítico: 2^n = ', 2**n)
      
print('Computacional:', np.size(all_sequences, axis=0))