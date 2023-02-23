# Imprime lista de numeros desde archivo txt, segun el numero objetivo.
# numeros de prueba = 1,9,5,0,20,-4,12,16,7
# valor objetivo = 12

nombre_archivo = 'numeros_prueba.txt'
with open(nombre_archivo, 'r') as archivo:             # Leer archivo numeros.txt.
    numeros_plano = archivo.read()
lista_numeros = [int(num) for num in numeros_plano.split(',')]   #  separar números con split y pse los pasa a enteros
objetivo = int(input("Digita el Valor objetivo: "))    # Pedir al usuario ingresar el valor objetivo
pares = {}                                             # Crear un diccionario vacío y se almacenan los pares de enteros

for i in range(len(lista_numeros)):                          # ciclo for para recorrer la lista de números
    diferencia = objetivo - lista_numeros[i]                 # estima diferencia del valor objetivo y el número actual
    if diferencia in pares:                                  # Si diferencia está diccionario = un par que suma al valor objetivo
        print(f'+ {lista_numeros[i]},{diferencia}')          # Imprimir el par de enteros encontrados
    else:
        pares[lista_numeros[i]] = True                       # Agregar el número actual al diccionario con valor True
