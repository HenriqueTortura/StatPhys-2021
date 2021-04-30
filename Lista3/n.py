import numpy as np

#%% Função que gera as sequências binárias com distribuição binomial
def Create_Sequences(n, p, m):
    #Parâmetros
    #   n: tamanho de cada sequência gerada;
    #   p: probabilidade de determinado dígito ser 1;
    #   m: quantidade de seuquências.
    
    all_sequences = (np.random.rand(m,n) <= p).astype(int)

    compare = np.delete(all_sequences + np.roll(all_sequences, 1, axis=1), (0), axis=1)
    selected_sequences = all_sequences[np.unique(np.where(compare==2)[0]),:]
    
    return all_sequences, selected_sequences

#%% Rodando

m = int(input('Quantas sequências quer criar? '))
n = int(input('Quantos dígitos por sequência? '))
p = float(input('Qual a probabilidade de aparecer 1? '))

all_sequences, selected_sequences = Create_Sequences(n, p, m)

delta = np.sqrt(1 + 2*p - 3*p**2)

analitico = (1 + p - 2*p**2 + delta)/(2*delta) * ((1 - p + delta)/2)**(n-1)
analitico = analitico + (2*p**2 - p - 1 + delta)/(2*delta) * ((1 - p - delta)/2)**(n-1)

computacional = 1 - np.size(selected_sequences, 0) / np.size(all_sequences, 0)

print('\n{:<30s} {:<30s}'.format(*['Analítico (item f)', 'Computacional']))
print('\n{:<30s} {:<30s}'.format(*[str(analitico), str(computacional)]))
    