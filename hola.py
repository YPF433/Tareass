#Ejercicio 1
# def ordenar_lista_en_sitio(numeros):
#     numeros.sort()
#     return numeros

# # Ejemplo de uso
# lista = [7, 2, 9, 1, 5]
# ordenar_lista_en_sitio(lista)
# print(lista)  # Salida: [1, 2, 5, 7, 9]

# Ejercicio 2
# conjunto = set(input("Ingresa elementos separados por espacio: ").split())
# print("Conjunto actual:", conjunto)
# elemento = input("Elemento a eliminar: ")
# conjunto.discard(elemento) 
# print("Conjunto final:", conjunto)

# Ejercicio 3
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))
# print("Faltan en B:", A - B)
# print("Faltan en A:", B - A)

# Ejercicio 4
# def eliminar_duplicados():
#     lista_cadenas = input("Ingresa las cadenas separadas por espacio: ").split()
#     lista_unica = list(set(lista_cadenas))
#     return lista_unica

# resultado = eliminar_duplicados()
# print("Lista de cadenas únicas:", resultado)

# Ejercicio 5
# def factorial():
#     n = int(input("Ingresa un número entero positivo: "))
#     if n < 0:
#         return "El número debe ser positivo"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         resultado = 1
#         for i in range(2, n + 1):
#             resultado *= i
#         return resultado

# print(factorial())

# Ejercicio 6

# def contar_ocurrencias():
#     lista = input("Ingresa los elementos de la lista separados por espacio: ").split()
#     elemento = input("Ingresa el elemento a contar: ")
#     ocurrencias = lista.count(elemento)
#     return f"El elemento '{elemento}' aparece {ocurrencias} veces en la lista."
# print(contar_ocurrencias())
 

# Ejercicio 7
# def suma_recursiva(n):
#     if n == 0:
#         return 0
#     else:
#         return n + suma_recursiva(n - 1)
# n = int(input("Ingresa un número entero positivo: "))
# resultado = suma_recursiva(n)
# print(f"La suma de los primeros {n} números naturales es: {resultado}")


