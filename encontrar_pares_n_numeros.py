#Julián Rene Muñoz
#se ingresa lista de numeros desde consola y objetivo a obtener
def encuentra_pares(lista_num, objetivo):
    pares = []
    for i in range(len(lista_num)):                           # ciclo para recorrer cada número de la lista
        for j in range(i+1, len(lista_num)):                  # Compara el número actual con los números de la lista
             if lista_num[i] + lista_num[j] == objetivo:       # suma de los dos números = objetivo, agregamos el par a la lista de pares
                pares.append((lista_num[i], lista_num[j]))
    return pares                                               # retorna la lista de pares encontrados

numeros = input("Lista de números separados por comas: ")   # ingreso de los números y el valor objetivo 
objetivo = int(input("Valor objetivo: "))

lista_num = [int(n) for n in numeros.split(',')]   # Convertir los números ingresados a una lista de enteros

pares_encontrados = encuentra_pares(lista_num, objetivo)  # Encontrar los pares que la suma = valor objetivo y se imprime
for par in pares_encontrados:
    print("+", par[0], ",", par[1])
