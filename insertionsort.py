def insertionSort(array):
    for step in range(1, len(array)):
        #Guarda o elemento posterior ao que vamos comparar.
        key = array[step]
        #Posição do elemento que vai ser comparado.
        j = step - 1
        # Se o elemento posterior for menor que o anterior, entra no laço.
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key

lista = [5,31,77,25,23,1,3,33,55,37,41,23,123,13,19,9,65,89,73,39]
insertionSort(lista)
print(lista)

