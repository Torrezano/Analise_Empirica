import random
import time
from xml.etree.ElementTree import tostring

Lista = {}
Lista['Insertion']  = {'Tempo':[],'Comparacoes':[],'Trocas':[]}
Lista['Selection']  = {'Tempo':[],'Comparacoes':[],'Trocas':[]}
Lista['Merge']  = {'Tempo':[],'Comparacoes':[],'Trocas':[]}
Lista['Heap']  = {'Tempo':[],'Comparacoes':[],'Trocas':[]}
Lista['Quick']  = {'Tempo':[],'Comparacoes':[],'Trocas':[]}

Media = {}
Media['Insertion']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
Media['Selection']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
Media['Merge']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
Media['Heap']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
Media['Quick']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}

Texto = {
    'Insertion':{
        "Tempo":"",
        "Comparacoes":"",
        "Trocas":""
        },
    'Selection':{
        "Tempo":"",
        "Comparacoes":"",
        "Trocas":""
        },
    'Merge':{
        "Tempo":"",
        "Comparacoes":"",
        "Trocas":""
        },
    'Heap':{
        "Tempo":"",
        "Comparacoes":"",
        "Trocas":""
        },
    'Quick':{
        "Tempo":"",
        "Comparacoes":"",
        "Trocas":""
        }
}

TAMANHO = 500 # tamanho padrão de todos utilizado para os vetores de amostra

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

#SelectionSort

def SelectionSort(array):
    #Inicializa o contador com 0, valor index inicial do vetor
    contador = 0
    while contador<len(array):
        #Inicializa o menor valor com um valor bem grande, para garantir que o algoritmo vai funcionar
        menorAtual = float('inf')
        IndexMenor = float('-inf')
        for i in range(contador,len(array)):
            #Se o valor da posição i do vetor for menor que o valor da variavel menorAtual, coloca o novo valor em menorAtual e o index em IndexMenor
            if array[i]<menorAtual:
                menorAtual = array[i]
                IndexMenor = i
        #Coloca o valor da posicao do contador na posicao do menorValor
        array[IndexMenor]=array[contador]
        #coloca o menor valor na posicao do contador
        array[contador]=menorAtual
        #Soma 1 ao contador para avançar o algoritmo
        contador = contador + 1
    return 0

TextoN = "N;"
# Ferramenta estatística
for t in range(100,1100,100):
    TextoN += str(t)+";"
    # loop para executar cada algoritmo 1000 vezez
    # a cada execução, é salvo seu valor do tempo 
    # de execução, comparações e trocas em uma lista apropriada
    for i in range(1000):
        data = amostraAleatoria(t,t)
        dataIn = data.copy()
        dataSelection = data.copy()
        dataMer = data.copy()
    
        dataQuick = data.copy()
        # -----------------------------Insertion Sort---------------------------------------
    
        start_time = time.time()
        insertionSort(dataIn)
        end_time = time.time()
    
        Lista['Insertion']['Tempo'].append((end_time-start_time)*1000)
        Lista['Insertion']['Comparacoes'].append(0) #todo calcular quantas comparações o algoritmo faz e colocar  no lugar do 0
        Lista['Insertion']['Trocas'].append(0) #todo calcular quantas trocas o algoritmo faz e colocar  no lugar do 0
    
        # -----------------------------Fim do Insertion Sort---------------------------------------
    
        # -----------------------------Selection Sort----------------------------------------------
    
        start_time = time.time()
        SelectionSort(dataSelection)
        end_time = time.time()
    
        Lista['Selection']['Tempo'].append((end_time-start_time)*1000)
        Lista['Selection']['Comparacoes'].append(0)
        Lista['Selection']['Trocas'].append(0)
    
        # -----------------------------Fim do Selection Sort---------------------------------------
    
        # -----------------------------Merge Sort----------------------------------------------
    
        start_time = time.time()
        mergeSort(dataMer)
        end_time = time.time()
    
        Lista['Merge']['Tempo'].append((end_time-start_time)*1000)
        Lista['Merge']['Comparacoes'].append(0)
        Lista['Merge']['Trocas'].append(0)
    
        # -----------------------------Fim do Merge Sort---------------------------------------
    
        # -----------------------------Heap Sort----------------------------------------------
        Lista['Heap']['Tempo'].append(0)
        Lista['Heap']['Comparacoes'].append(0)
        Lista['Heap']['Trocas'].append(0)
        # -----------------------------Fim do Heap Sort---------------------------------------
    
        # -----------------------------Quick Sort----------------------------------------------
        size = len(dataQuick)

        start_time = time.time()
        quickSort(dataQuick, 0, size - 1)
        end_time = time.time()
    
        Lista['Quick']['Tempo'].append((end_time-start_time)*1000)
        Lista['Quick']['Comparacoes'].append(0)
        Lista['Quick']['Trocas'].append(0)
        # -----------------------------Fim do Quick Sort---------------------------------------
    
    # loop para calcular as medidadas estatísticas (média e desvio padrão)
    # todo: calcular desvio padrão
    for algoritmo in Lista.keys():
        for metrica in Lista[algoritmo].keys():
            # if len(Lista[algoritimo][metrica]) == 0:
            #     print(f"Algoritmo: {algoritimo} ; Metrica {metrica}")
        
            Media[algoritmo][metrica] = sum(Lista[algoritmo][metrica]) / len(Lista[algoritmo][metrica])

    print(f"Media do Tempo de Execucao com N = {t}:")
    for algoritmo in Media.keys():
        print(f"{algoritmo}: {Media[algoritmo]['Tempo']} milesegundos")
        Texto[algoritmo]["Tempo"] +=  str(Media[algoritmo]['Tempo'])+";"

    print('')
    print('')

    print(f"Media das Trocas com N = {t}:")
    for algoritmo in Media.keys():
        print(f"{algoritmo}: {Media[algoritmo]['Trocas']} trocas")
        Texto[algoritmo]["Trocas"] +=  str(Media[algoritmo]['Trocas'])+";"

    print('')
    print('')

    print(f"Media das Comparacoes com N = {t}:")
    for algoritmo in Media.keys():
        print(f"{algoritmo}: {Media[algoritmo]['Comparacoes']} comparacoes")
        Texto[algoritmo]["Comparacoes"] +=  str(Media[algoritmo]['Comparacoes'])+";"

    print('----------------------------------------------------------------------------------------------------------------')

Texto_Completo = ""
for algoritmo in  Texto.keys():
    Texto_Completo +=  str(algoritmo)+"\n"
    Texto_Completo += TextoN+"\n"
    for metrica in Texto[algoritmo].keys():
        Texto_Completo += str(metrica)+";"+Texto[algoritmo][metrica]+"\n"
    Texto_Completo += "\n\n"

for metrica in ["Tempo","Trocas","Comparacoes"]:
    Texto_Completo +=  str(metrica)+"\n"
    Texto_Completo += TextoN+"\n"
    for algoritmo in Texto.keys():
        Texto_Completo += str(algoritmo)+";"+Texto[algoritmo][metrica]+"\n"
    Texto_Completo += "\n\n"

file = open('Analise_Empirica.txt','w')
file.write(Texto_Completo)
file.close()

exit()


