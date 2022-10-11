import random
import time

TAMANHO = 200 # tamanho padrão de todos utilizado para os vetores de amostra

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

# Quick sort in Python

# função que faz a partição e retorna a posição onde ela ocorreu
# (escolhe um pivo e coloca ele na posição correta, retornando o indice dessa posição)
def partition(array, low, high):
# low = menor posição do vetor
# high = maior posição do vetor

  # escolhe o elemento mais a direita como pivo
  pivot = array[high]

  # i aponta para o elemento que será usado na troca
  i = low - 1

  # percorre todo o vetor e compara cada elemento com o pivo
  for j in range(low, high):
    if array[j] <= pivot:
      # Se um elemento menor do que o pivo for encontrado
      # troca ele com o elemento apontado por i
      i = i + 1

      # troca o elemento na posição i com o elemento na posição j
      (array[i], array[j]) = (array[j], array[i])

  # troca o pivo com o elemento seguinte do elemento apontado por i (i+1)
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # retorna o indicine de onde ocorreu a partição do vetor
  return i + 1

# função que faz o quicksort
def quickSort(array, low, high):
# low = menor posição do vetor
# high = maior posição do vetor
  if low < high:

    # pi é a posição do pivo
    # após a função "partition":
    # os elementos maiores que o pivo estão na sua direita no vetor
    # os elementos menores que o pivo estão na sua esquerda no vetor
    pi = partition(array, low, high)

    # chamada recursica para os elementos à esquerda do pivo
    quickSort(array, low, pi - 1)

    # chamada recursica para os elementos à direita do pivo
    quickSort(array, pi + 1, high)




# Abaixo estão códigos feitos apenas para testar os algoritmos

# ---------------------gerando amostras e testando o Insertion Sort ----------------------------------------------

data = amostraAleatoria(TAMANHO,100)
# print('Vetor nao ordenado')
# print(data)

print('------------------------------------------------------------------')

data2 = amostraInversa(TAMANHO)
# print('Vetor inversamente ordenado')
# print(data2)

print('------------------------------------------------------------------')

data3 = amostraSemiOrdenada(TAMANHO)
# print('Vetor semi-ordenado')
# print(data3)

# Executando o Inserction Sort e calculando o seu tempo de execução
start_time = time.time()
dataSel = data
insertionSort(dataSel)
end_time = time.time()
finish_time = end_time - start_time # calcula o tempo de execução do programa
print('Tempo em milesegundos da execucao do inserction sort:')
print(finish_time*1000) # o valor de "finish_time" é dado em segundos, então é multiplicado por 1000 para exibir em milesegundos
#Nota: se o tamanho do vetor for muito pequeno (como n=20), não será possível calcular o tempo de execução

# print('Vetor ordenado (amostra aleatoria):')
# print(data)

# ---------------------gerando uma nova amostra testar o Merge Sort ----------------------------------------------
print('------------------------------------------------------------------')

# Executando o Merge Sort e calculando o seu tempo de execução
start_time = time.time()
dataMer = data
mergeSort(dataMer)
end_time = time.time()
finish_time = end_time - start_time # calcula o tempo de execução do programa
print('Tempo em milesegundos da execucao do Merge sort:')
print(finish_time*1000) # o valor de "finish_time" é dado em segundos, então é multiplicado por 1000 para exibir em milesegundos
#Nota: se o tamanho do vetor for muito pequeno (como n=20), não será possível calcular o tempo de execução

# print('Vetor ordenado (amostra aleatoria):')
# print(data)

# ---------------------gerando uma nova amostra testar o Quick Sort ----------------------------------------------

dataQuick = data
size = len(dataQuick)

start_time = time.time()
quickSort(dataQuick, 0, size - 1)
end_time = time.time()

finish_time = end_time - start_time # calcula o tempo de execução do programa
print('Tempo em milesegundos da execucao do Quick sort:')
print(finish_time*1000) # o valor de "finish_time" é dado em segundos, então é multiplicado por 1000 para exibir em milesegundos
#Nota: se o tamanho do vetor for muito pequeno (como n=20), não será possível calcular o tempo de execução

#print('Vetor ordenado (amostra aleatoria):')
#print(data)