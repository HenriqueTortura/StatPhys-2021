import numpy as np

#%%
def Create_Binary_Sequences(alphabet, all_sequences, sequence, n, i, verbose=False):
    
    local_alphabet = alphabet
    
    if i == n:
        if verbose: print(sequence)
        return np.concatenate((all_sequences, sequence))
    
    if sequence[:,i-1] == 1:
        local_alphabet = np.delete(alphabet, np.where(alphabet == [1]), axis=0)
        
    for j in local_alphabet:
        sequence[:,i] = j
        all_sequences = Create_Binary_Sequences(alphabet, all_sequences, sequence, n, i+1)
    
    return all_sequences

#%%

n = 3
alphabet = np.arange(2)

sequence = np.zeros((1,n), dtype=int)
all_sequences = np.zeros((1,n), dtype=int)

all_sequences = Create_Binary_Sequences(alphabet, all_sequences, sequence, n, 0)
all_sequences =  np.delete(all_sequences, (0), axis=0)

#%%
Analitical = (1 + 2*np.sqrt(5)/5)*((1+np.sqrt(5))/2)**(n-1) + (1 - 2*np.sqrt(5)/5)*((1 - np.sqrt(5))/2)**(n-1)

print('Alfabeto de binário.')
print('Palavras com '+str(n)+' dígitos sem 1\'s consecutivos.')
print('Analítico:', Analitical)
      
print('Computacional:', np.size(all_sequences, axis=0))