#Ejercicio 1

# def calcular_precio_final(precio_original: float, porcentaje_descuento: float) -> float:
#     """
#     Calcula el precio final de un producto después de aplicar un descuento.
    
#     Parámetros:
#     precio_original (float): El precio original del producto.
#     porcentaje_descuento (float): El porcentaje de descuento a aplicar (0-100).
    
#     Retorna:
#     float: El precio final del producto después del descuento.
#     """
#     if porcentaje_descuento < 0 or porcentaje_descuento > 100:
#         raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")
    
#     descuento = (porcentaje_descuento / 100) * precio_original
#     precio_final = precio_original - descuento
#     return precio_final

# # Ejemplo de uso
# precio_original = 100.0
# porcentaje_descuento = 20.0
# print(f"Precio final: {calcular_precio_final(precio_original, porcentaje_descuento)}")


# #Ejercicio 2
# def convertir_temperatura(temperatura: float, unidad_origen: str, unidad_destino: str) -> float:
#     """
#     Convierte temperaturas entre Celsius y Fahrenheit.
    
#     Parámetros:
#     temperatura (float): La temperatura a convertir.
#     unidad_origen (str): La unidad de origen ('C' para Celsius, 'F' para Fahrenheit).
#     unidad_destino (str): La unidad de destino ('C' para Celsius, 'F' para Fahrenheit).
    
#     Retorna:
#     float: La temperatura convertida.
    
#     Ejemplos de uso:
#     convertir_temperatura(100, 'C', 'F') -> 212.0
#     convertir_temperatura(32, 'F', 'C') -> 0.0
#     """
#     if unidad_origen == 'C' and unidad_destino == 'F':
#         return (temperatura * 9/5) + 32
#     elif unidad_origen == 'F' and unidad_destino == 'C':
#         return (temperatura - 32) * 5/9
#     else:
#         raise ValueError("Unidades no válidas. Use 'C' para Celsius o 'F' para Fahrenheit")

# # Ejemplo de uso
# temperatura = 132
# unidad_origen = 'C'
# unidad_destino = 'F'
# print(f"Temperatura convertida: {convertir_temperatura(temperatura, unidad_origen, unidad_destino)}")

# ejercicio 3

# def es_palindromo(texto: str) -> bool:
#     """
#     Verifica si una palabra o frase es un palíndromo.
    
#     Parámetros:
#     texto (str): La cadena de texto a evaluar.
    
#     Retorna:
#     bool: True si es un palíndromo, False en caso contrario.
    
#     Ejemplos de uso:
#     es_palindromo("Amor Roma") -> True
#     es_palindromo("Como estas") -> False
#     """
#     texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
#     return texto_limpio == texto_limpio[::-1]

# Ejemplo
# print(es_palindromo("Amor Roma"))  
# print(es_palindromo("Como estas"))  


#Ejercicio 4

# def analizar_texto(texto: str) -> dict:
#     """
#     Analiza un texto contando la cantidad de palabras y caracteres.
    
#     Parámetros:
#     texto (str): La cadena de texto a analizar.
    
#     Retorna:
#     dict: Un diccionario con las siguientes claves:
#         - 'palabras': (int) cantidad de palabras en el texto.
#         - 'caracteres': (int) cantidad total de caracteres en el texto (incluyendo espacios y signos de puntuación).
    
#     Ejemplos de uso:
#     analizar_texto("Hola mundo") -> {'palabras': 2, 'caracteres': 10}
#     analizar_texto("Aguante Boca") -> {'palabras':2 , 'caracteres': 12}
#     """
#     palabras = texto.split()
#     caracteres = len(texto)
    
#     return {'palabras': len(palabras), 'caracteres': caracteres}

# # Ejemplo
# print(analizar_texto("Hola mundo"))  # {'palabras': 2, 'caracteres': 10}
# print(analizar_texto("Aguante Boca"))  # {'palabras': 2, 'caracteres': 12}

#Ejercicio 5

# def generar_primos(hasta):
#     """
#     Genera una lista de números primos hasta un número dado.
    
#     Un número primo es un número natural mayor que 1 que solo es divisible por 
#     1 y por sí mismo. Ejemplos de números primos son: 2, 3, 5, 7, 11, etc.
    
#     Parámetros:
#     hasta (int): Número entero positivo hasta el cual se generarán los primos.
    
#     Retorna:
#     list: Lista de números primos hasta el número dado (inclusive si es primo).
#     """
#     if hasta < 2:
#         return []
    
#     primos = []
#     for num in range(2, hasta + 1):
#         es_primo = all(num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1))
#         if es_primo:
#             primos.append(num)
    
#     return primos

# Ejemplo de uso
# print(generar_primos(20))

# Ejercicio 6

def generar_primos(hasta):
    """
    Genera una lista de números primos hasta un número dado.
    
    Un número primo es un número natural mayor que 1 que solo es divisible por 
    1 y por sí mismo. Ejemplos de números primos son: 2, 3, 5, 7, 11, etc.
    
    Parámetros:
    hasta (int): Número entero positivo hasta el cual se generarán los primos.
    
    Retorna:
    list: Lista de números primos hasta el número dado (inclusive si es primo).
    """
    if hasta < 2:
        return []
    
    primos = []
    for num in range(2, hasta + 1):
        es_primo = all(num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1))
        if es_primo:
            primos.append(num)
    
    return primos

# def actualizar_inventario(inventario, productos_vendidos):
#     """
#     Actualiza el inventario de una tienda tras la venta de productos.
    
#     Parámetros:
#     inventario (dict): Diccionario con productos como claves y cantidades como valores.
#     productos_vendidos (list): Lista de productos vendidos.
    
#     Retorna:
#     dict: Inventario actualizado después de las ventas.
    
#     Ejemplo:
#     >>> inventario = {'manzanas': 10, 'bananas': 5, 'naranjas': 8}
#     >>> productos_vendidos = ['manzanas', 'bananas', 'bananas', 'naranjas']
#     >>> actualizar_inventario(inventario, productos_vendidos)
#     {'manzanas': 9, 'bananas': 3, 'naranjas': 7}
#     """
#     for producto in productos_vendidos:
#         if producto in inventario and inventario[producto] > 0:
#             inventario[producto] -= 1
    
#     return inventario

# # Ejemplo de uso
# print(generar_primos(20))

# inventario = {'manzanas': 10, 'bananas': 5, 'naranjas': 8}
# productos_vendidos = ['manzanas', 'bananas', 'bananas', 'naranjas']
# print(actualizar_inventario(inventario, productos_vendidos))

# Ejercicio 7

# Lista de cadenas
input_list = ["hola", "adios"]

# Usando map para convertir cada cadena en una lista de caracteres
output_list = list(map(list, input_list))

# Mostrar el resultado
print(output_list)

