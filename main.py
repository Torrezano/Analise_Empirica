import random
import time
from xml.etree.ElementTree import tostring
import math
import statistics

NumTrocasInsert = 0
NumTrocasMerge = 0
NumTrocasQuick = 0
NumTrocasSelection = 0
NumTrocasHeap = 0

NumCompInsert = 0
NumCompMerge = 0
NumCompQuick = 0
NumCompSelection = 0
NumCompHeap = 0

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

DesvioP = {}
DesvioP['Insertion']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
DesvioP['Selection']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
DesvioP['Merge']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
DesvioP['Heap']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}
DesvioP['Quick']  = {'Tempo':0,'Comparacoes':0,'Trocas':0}

TextoM = {
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

TextoDesvioP = {
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

# InsertionSort 

def insertionSort(array):
    global NumCompInsert
    global NumTrocasInsert
    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1
           
        while j >= 0 and chave < array[j]:
            NumCompInsert += 1
            NumTrocasInsert += 1
            array[j + 1] = array[j]
            j = j - 1

        if j+1!=i   :            
            NumTrocasInsert = NumTrocasInsert + 1
        if j>=0:
            NumCompInsert = NumCompInsert + 1
        array[j + 1] = chave
      
  
# MergeSort

def mergeSort(array):
    global NumCompMerge
    global NumTrocasMerge
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
            NumCompMerge = NumCompMerge + 1
            if A[i] < B[j]:
                NumTrocasMerge = NumTrocasMerge + 1
                array[k] = A[i]
                i += 1
            else:
                NumTrocasMerge = NumTrocasMerge + 1
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

# QuickSort

# função que faz a partição e retorna a posição onde ela ocorreu
# (escolhe um pivo e coloca ele na posição correta, retornando o indice dessa posição)
def partition(array, low, high):
  global NumCompQuick
  global NumTrocasQuick
# low = menor posição do vetor
# high = maior posição do vetor

  # escolhe o elemento mais a direita como pivo
  pivot = array[high]

  # i aponta para o elemento que será usado na troca
  i = low - 1

  # percorre todo o vetor e compara cada elemento com o pivo
  for j in range(low, high):
    NumCompQuick = NumCompQuick + 1
    if array[j] <= pivot:
      # Se um elemento menor do que o pivo for encontrado
      # troca ele com o elemento apontado por i
      i = i + 1

      # troca o elemento na posição i com o elemento na posição j
      NumTrocasQuick = NumTrocasQuick + 1
      (array[i], array[j]) = (array[j], array[i])

  # troca o pivo com o elemento seguinte do elemento apontado por i (i+1)
  NumTrocasQuick = NumTrocasQuick + 1
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
    global NumCompSelection
    global NumTrocasSelection 
    contador = 0 #Inicializa o contador com 0, valor index inicial do vetor
    while contador<len(array):       
        menorAtual = float('inf')  #Inicializa o menor valor com um valor bem grande, para garantir que o algoritmo vai funcionar
        IndexMenor = float('-inf')
        for i in range(contador,len(array)):            
            NumCompSelection = NumCompSelection + 1
            #Se o valor da posição i do vetor for menor que o valor da variavel menorAtual, coloca o novo valor em menorAtual e o index em IndexMenor
            if array[i]<menorAtual:
                menorAtual = array[i]
                IndexMenor = i
        #Se indexMenor for diferente de contador, faz a troca dos valores
        if IndexMenor!=contador:
            NumTrocasSelection = NumTrocasSelection + 1
            #Coloca o valor da posicao do contador na posicao do menorValor
            array[IndexMenor]=array[contador]
            #coloca o menor valor na posicao do contador
            array[contador]=menorAtual                
        contador = contador + 1 #Soma 1 ao contador para avançar o algoritmo

#HeapSort

def heapify(array, n, i):
    global NumCompHeap
    global NumTrocasHeap
    largest = i  # Inicializa a raiz da arvore com o maior elemento
    l = 2 * i + 1  # lado esquerdo = 2*i + 1
    r = 2 * i + 2  # lado direito = 2*i + 2
 # Verificando se existe um filho esquerdo e se é maior que a raiz
    NumCompHeap = NumCompHeap + 1
    if l < n and array[i] < array[l]:
        largest = l
 # Verificando se existe um filho direito e se é maior que a raiz
    NumCompHeap = NumCompHeap + 1
    if r < n and array[largest] < array[r]:
        largest = r
 # Se necessario, faz a troca da raiz
    if largest != i:
        NumTrocasHeap = NumTrocasHeap + 1
        (array[i], array[largest]) = (array[largest], array[i])  # swap
  # Faça o heapify da raiz.
        heapify(array, n, largest)
 
 
# Função do HeapSort
def HeapSort(array):
    global NumTrocasHeap
    n = len(array)
 # Constroi um max heap (ordenação crescente)
 # Como o ultimo pai estara na posicao ((n//2)-1) começamos o heapify aqui.
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
 # Extraindo os elementos
    for i in range(n - 1, 0, -1):
        NumTrocasHeap = NumTrocasHeap + 1 
        (array[i], array[0]) = (array[0], array[i])  # Troca
        heapify(array, i, 0)


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
        dataHeap = data.copy()
        dataQuick = data.copy()
        # -----------------------------Insertion Sort---------------------------------------
        NumCompInsert = 0
        NumTrocasInsert = 0
        start_time = time.time()
        insertionSort(dataIn)
        end_time = time.time()
    
        Lista['Insertion']['Tempo'].append((end_time-start_time)*1000)
        Lista['Insertion']['Comparacoes'].append(NumCompInsert)
        Lista['Insertion']['Trocas'].append(NumTrocasInsert)
    
        # -----------------------------Fim do Insertion Sort---------------------------------------
    
        # -----------------------------Selection Sort----------------------------------------------

        NumCompSelection = 0
        NumTrocasSelection = 0
        start_time = time.time()
        SelectionSort(dataSelection)
        end_time = time.time()
    
        Lista['Selection']['Tempo'].append((end_time-start_time)*1000)
        Lista['Selection']['Comparacoes'].append(NumCompSelection)
        Lista['Selection']['Trocas'].append(NumTrocasSelection)
    
        # -----------------------------Fim do Selection Sort---------------------------------------
    
        # -----------------------------Merge Sort----------------------------------------------

        NumCompMerge = 0
        NumTrocasMerge = 0
        start_time = time.time()
        mergeSort(dataMer)
        end_time = time.time()
    
        Lista['Merge']['Tempo'].append((end_time-start_time)*1000)
        Lista['Merge']['Comparacoes'].append(NumCompMerge)
        Lista['Merge']['Trocas'].append(NumTrocasMerge)
    
        # -----------------------------Fim do Merge Sort---------------------------------------
    
        # -----------------------------Heap Sort----------------------------------------------
        NumCompHeap = 0
        NumTrocasHeap = 0
        start_time = time.time()
        HeapSort(dataHeap)
        end_time = time.time()
        
        Lista['Heap']['Tempo'].append((end_time-start_time)*1000)
        Lista['Heap']['Comparacoes'].append(NumCompHeap)
        Lista['Heap']['Trocas'].append(NumTrocasHeap)
        # -----------------------------Fim do Heap Sort---------------------------------------
    
        # -----------------------------Quick Sort----------------------------------------------
        size = len(dataQuick)

        NumCompQuick = 0
        NumTrocasQuick = 0
        start_time = time.time()
        quickSort(dataQuick, 0, size - 1)
        end_time = time.time()
    
        Lista['Quick']['Tempo'].append((end_time-start_time)*1000)
        Lista['Quick']['Comparacoes'].append(NumCompQuick)
        Lista['Quick']['Trocas'].append(NumTrocasQuick)
        # -----------------------------Fim do Quick Sort---------------------------------------
    
    # loop para calcular as medidadas estatísticas (média e desvio padrão)
    # todo: calcular desvio padrão
    for algoritmo in Lista.keys():
        for metrica in Lista[algoritmo].keys():
            # if len(Lista[algoritimo][metrica]) == 0:
            #     print(f"Algoritmo: {algoritimo} ; Metrica {metrica}")
        
            Media[algoritmo][metrica] = sum(Lista[algoritmo][metrica]) / len(Lista[algoritmo][metrica])
            DesvioP[algoritmo][metrica] = statistics.pstdev(Lista[algoritmo][metrica])

    print(f"Media do Tempo de Execucao com N = {t}:")
    for algoritmo in Media.keys():
        print(f"{algoritmo}: {Media[algoritmo]['Tempo']} milesegundos")
        TextoM[algoritmo]["Tempo"] +=  str(Media[algoritmo]['Tempo'])+";"
        TextoDesvioP[algoritmo]["Tempo"] += str(DesvioP[algoritmo]['Tempo'])+";"

    print('')
    print('')

    print(f"Media das Trocas com N = {t}:")
    for algoritmo in Media.keys():
        print(f"{algoritmo}: {Media[algoritmo]['Trocas']} trocas")
        TextoM[algoritmo]["Trocas"] +=  str(Media[algoritmo]['Trocas'])+";"
        TextoDesvioP[algoritmo]["Trocas"] +=  str(DesvioP[algoritmo]['Trocas'])+";"

    print('')
    print('')

    print(f"Media das Comparacoes com N = {t}:")
    for algoritmo in Media.keys():
        print(f"{algoritmo}: {Media[algoritmo]['Comparacoes']} comparacoes")
        TextoM[algoritmo]["Comparacoes"] +=  str(Media[algoritmo]['Comparacoes'])+";"
        TextoDesvioP[algoritmo]["Comparacoes"] +=  str(DesvioP[algoritmo]['Comparacoes'])+";"

    print('----------------------------------------------------------------------------------------------------------------')

Texto_Completo = ""
for algoritmo in  TextoM.keys():
    Texto_Completo +=  str(algoritmo)+" Média\n"
    Texto_Completo += TextoN+"\n"
    for metrica in TextoM[algoritmo].keys():
        Texto_Completo += str(metrica)+";"+TextoM[algoritmo][metrica]+"\n"
    Texto_Completo += "\n\n"
    
    Texto_Completo +=  str(algoritmo)+" Devio Padrão\n"
    Texto_Completo += TextoN+"\n"
    for metrica in TextoDesvioP[algoritmo].keys():
        Texto_Completo += str(metrica)+";"+TextoDesvioP[algoritmo][metrica]+"\n"
    Texto_Completo += "\n\n"

for metrica in ["Tempo","Trocas","Comparacoes"]:
    Texto_Completo +=  str(metrica)+" Média\n"
    Texto_Completo += TextoN+"\n"
    for algoritmo in TextoM.keys():
        Texto_Completo += str(algoritmo)+";"+TextoM[algoritmo][metrica]+"\n"
    Texto_Completo += "\n\n"
    
for metrica in ["Tempo","Trocas","Comparacoes"]:
    Texto_Completo +=  str(metrica)+" Devio Padrão\n"
    Texto_Completo += TextoN+"\n"
    for algoritmo in TextoDesvioP.keys():
        Texto_Completo += str(algoritmo)+";"+TextoDesvioP[algoritmo][metrica]+"\n"
    Texto_Completo += "\n\n"

file = open('Analise_Empirica.txt','w')
file.write(Texto_Completo)
file.close()

exit()


