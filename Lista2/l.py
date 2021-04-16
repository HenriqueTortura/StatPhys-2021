import numpy as np

#%% Função que gera as sequências binárias
def Create_Binary_Sequences(alphabet, all_sequences, sequence, n, i, verbose=False):
    #Parâmetros
    #   alphabet: alfabeto dos possíveis dígitos;
    #   sequence: sequência em construção;
    #   n: tamanho de cada sequência gerada;
    #   i: posição da sequência na qual um dígito do alfabeto é atribuído;
    #   verbose: permite imprimir no terminal cada sequência (não recomendado para altos valores de n).
    #Retorna
    #   all_sequences: dicionário de todas as sequências geradas.
    
    local_alphabet = alphabet
    
    if i == n: #Avalia se chegamos no último dígito da sequência
        if verbose: print(sequence)
        return np.concatenate((all_sequences, sequence)) #Concatena a sequência criada na lista de todas as sequências
    
    if sequence[:,i-1] == 1: #Se o símbolo anterior for 1, remove esse valor do alfabeto
        local_alphabet = np.delete(alphabet, np.where(alphabet == [1]), axis=0)
        
    for j in local_alphabet: #Varre os possíveis dígitos para a posição i
        sequence[:,i] = j #Atribui digíto na posição i
        all_sequences = Create_Binary_Sequences(alphabet, all_sequences, sequence, n, i+1) #Atualiza para a próxima posição na sequência (i+1)
    
    return all_sequences

#%% Geração das sequências
n = int(input('Quantidade de dígitos por sequência: '))

alphabet = np.arange(2)
sequence = np.zeros((1,n), dtype=int)
all_sequences = np.zeros((1,n), dtype=int) #Inicializa uma sequência toda nula (depois excluída)

all_sequences = Create_Binary_Sequences(alphabet, all_sequences, sequence, n, 0)
all_sequences =  np.delete(all_sequences, (0), axis=0) #Elimina a sequência toda nula (duplicada pela inicialização)

#%% Resultados
Analitical = (1 + 2*np.sqrt(5)/5)*((1+np.sqrt(5))/2)**(n-1) + (1 - 2*np.sqrt(5)/5)*((1 - np.sqrt(5))/2)**(n-1)

print('\n')
print('Alfabeto de binário.')
print('Palavras com n = '+str(n)+' dígitos sem 1\'s consecutivos.')
print('Analítico:', Analitical)
      
print('Computacional:', np.size(all_sequences, axis=0))