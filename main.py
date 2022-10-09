import random
import time

TAMANHO = 20 # tamanho padrão de todos utilizado para os vetores de amostra

# Função para gerar amostra aleatória

def amostraAleatoria(n, max):
    # Resumo: a função retorna um vetor de n posições preenchido com números aleatórios de 1 até max (apenas inteiros positivos)
    # n = o tamanho do vetor
    # Max = o maior número aleatório (inteiro positivo) que pode ser gerado

    vetor = [] # vetor onde será armazenado os números aleatórios
    for i in range(n):
        vetor.append(random.randint(1, max))
    return vetor

# Função para gerar amostra inversamente ordenada
def amostraInversa(n):
    vetor = []
    for i in range(n,0,-1):
        vetor.append(i)
    return vetor

# Função para gerar amostra semi-ordenada
def amostraSemiOrdenada(n):
    vetor = []
    for i in range(n):
        vetor.append(i+1)
        
    aux = vetor[i]
    vetor[i] = vetor[i-1]
    vetor[i-1] = aux
    
    return vetor

# Insertion sort 

def insertionSort(array):
    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1
           
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = chave
      
  
# MergeSort

def mergeSort(array):
    if len(array) > 1:

        #  r é a posição em que o vetor será dividido em dois
        r = len(array)//2
        A = array[:r]
        B = array[r:]

        # Ordena as duas metades
        mergeSort(A)
        mergeSort(B)

        i = 0
        j = 0
        k = 0

        # Até chegar no final do vetor A ou B, compara qual o menor elemento
        # e coloca ele na posição apropriada do vetor principal ("array")
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                array[k] = A[i]
                i += 1
            else:
                array[k] = B[j]
                j += 1
            k += 1

        # Quando todos os elementos de A ou B já estiverem no vetor principal, 
        # pega todos os elementos restantes e coloca no vetor principal
        while i < len(A):
            array[k] = A[i]
            i += 1
            k += 1

        while j < len(B):
            array[k] = B[j]
            j += 1
            k += 1


# Abaixo estão códigos feitos apenas para testar os algoritmos

# ---------------------gerando amostras e testando o Insertion Sort ----------------------------------------------

data = amostraAleatoria(TAMANHO,100)
print('Vetor nao ordenado')
print(data)

print('------------------------------------------------------------------')

data2 = amostraInversa(TAMANHO)
print('Vetor inversamente ordenado')
print(data2)

print('------------------------------------------------------------------')

data3 = amostraSemiOrdenada(TAMANHO)
print('Vetor semi-ordenado')
print(data3)

# Executando o Inserction Sort e calculando o seu tempo de execução
start_time = time.time()
insertionSort(data)
end_time = time.time()
finish_time = end_time - start_time # calcula o tempo de execução do programa
print('Tempo em milesegundos da execucao do inserction sort:')
print(finish_time*1000) # o valor de "finish_time" é dado em segundos, então é multiplicado por 1000 para exibir em milesegundos
#Nota: se o tamanho do vetor for muito pequeno (como n=20), não será possível calcular o tempo de execução

print('Vetor ordenado (amostra aleatoria):')
print(data)

# ---------------------gerando uma nova amostra testar o Merge Sort ----------------------------------------------
print('------------------------------------------------------------------')

data = amostraAleatoria(TAMANHO,100)
print('Vetor nao ordenado')
print(data)

# Executando o Merge Sort e calculando o seu tempo de execução
start_time = time.time()
mergeSort(data)
end_time = time.time()
finish_time = end_time - start_time # calcula o tempo de execução do programa
print('Tempo em milesegundos da execucao do Merge sort:')
print(finish_time*1000) # o valor de "finish_time" é dado em segundos, então é multiplicado por 1000 para exibir em milesegundos
#Nota: se o tamanho do vetor for muito pequeno (como n=20), não será possível calcular o tempo de execução

print('Vetor ordenado (amostra aleatoria):')
print(data)