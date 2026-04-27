#metodo de ordenamiento de seleccion (selectionsort)
from random import sample 
lista = list(range(100))
vectorselect = sample(lista,8)

def selectionsort(vectorselect):
    """esta fumcion ordenara el vector que le pases como argumento con el metodo de selection sort """

    print ("el vector a ordenar es:",vectorselect)

    largo = 0 
    for _ in vectorselect:

        largo +=1 

    for _ in range(largo):

        minimo = 1 
        for j in range(i+1, largo):
            if vectorselect[minimo] > vectorselect[j]:
                minimo = j 
                vectorselect[j]; vectorselect[minimo] = vectorselect[minimo], vectorselect[i]

                print("el vector ordenado es:", vectorselect)

                selectionsort(vectorselect=)