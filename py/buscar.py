
#forma 1
'''''
import array as array

array1 = array.array ('i', [5,6,7,8,9,10,11,12])
    


print (array1.index(12))
'''''


#forma 2
'''
lista = [10,11,12,13,14,15,16,17,18,19,20]
elemento = float (input ('Ingrese el numero a buscar'))

posiciones = []  # nuestra lista para guardar las posiciones
posicion = -1  # empezaremos a buscar en posicion + 1 (que es 0 inicialmente)

try:
    while True:
        # buscamos empezando a buscar desde la última posición encontrada
        posicion = lista.index(elemento, posicion + 1)
        posiciones.append(posicion)
except:
    pass  # no hacemos nada si index lanza ValueError

print(posiciones)

'''


#forma 3
numero = [12,13,14,15,16,16]


def buscar(objetivo):
  target_indices = []
  for i in range(len(numero)):
    if numero[i] == objetivo:
      target_indices.append(i)  
  if target_indices == []:
     print("No se encontró, intentá otro número ")
  else:
    print(f"{objetivo} se encontró en el índice :{target_indices}")
    

buscar(float (input ('Ingrese el numero a buscar')))


