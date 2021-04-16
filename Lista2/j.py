import numpy as np

#%% Função que gera as sequências binárias
def Create_Binary_Sequences(all_sequences, sequence, n, i, verbose = False):
    #Parâmetros
    #   sequence: sequência em construção;
    #   n: tamanho de cada sequência gerada;
    #   i: posição da sequência na qual um dígito do alfabeto é atribuído
    #   verbose: permite imprimir no terminal cada sequência (não recomendado para altos valores de n).
    #Retorna
    #   all_sequences: dicionário de todas as sequências geradas.
    
    if i == n: #Avalia se chegamos no último dígito da sequência
        if verbose: print(sequence)
        return np.concatenate((all_sequences, sequence)) #Concatena a sequência criada na lista de todas as sequências
    
    for j in range(2): #Varre os possíveis dígitos para a posição i (no caso, 0 e 1)
        sequence[:,i] = j #Atribui digíto na posição i
        all_sequences = Create_Binary_Sequences(all_sequences, sequence, n, i+1) #Atualiza para a próxima posição na sequência (i+1)
    
    return all_sequences

#%% Geração das sequências
n = int(input('Quantidade de dígitos por sequência: '))

sequence = np.zeros((1,n), dtype=int)
all_sequences = np.zeros((1,n), dtype=int) #Inicializa uma sequência toda nula (depois excluída)

all_sequences = Create_Binary_Sequences(all_sequences, sequence, n, 0)
all_sequences =  np.delete(all_sequences, (0), axis=0) #Elimina a sequência toda nula (duplicada pela inicialização)

#%% Resultados
print('\n')
print('Alfabeto de binário.')
print('Palavras com n = '+str(n)+' dígitos.')
print('Analítico: 2^n = ', 2**n)
      
print('Computacional:', np.size(all_sequences, axis=0))