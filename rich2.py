'''
rich_2 example
'''

# from rich.console import Console

# def imprimir_lista_colores_alternados(lista_de_strings, color1="cyan", color2="magenta"):
#     """
#     Imprime una lista de strings con colores alternados para mejorar la legibilidad.

#     Args:
#         lista_de_strings (list): La lista de strings a imprimir.
#         color1 (str): El primer color a usar (ej. "cyan", "green", "red").
#         color2 (str): El segundo color a usar (ej. "magenta", "blue", "yellow").
#     """
#     console = Console()
    
#     for i, item in enumerate(lista_de_strings):
#         if i % 2 == 0:  # Si el índice es par, usa el primer color
#             console.print(f"[{color1}]{item}[/{color1}]")
#         else:  # Si el índice es impar, usa el segundo color
#             console.print(f"[{color2}]{item}[/{color2}]")

# # Ejemplo de uso con una lista de siete strings
# mis_strings = [
#     "Este es el primer string de la lista.",
#     "El segundo string tiene un color diferente.",
#     "Ahora volvemos al primer color para el tercero.",
#     "El cuarto string continúa con el segundo color.",
#     "Y así sucesivamente, alternando los colores.",
#     "El sexto string sigue la secuencia de colores.",
#     "Finalmente, el séptimo string cierra la lista."
# ]

# print("--- Lista con colores alternados ---")
# imprimir_lista_colores_alternados(mis_strings)

# print("\n--- Otra lista con diferentes colores ---")
# otra_lista = [f"Elemento {i+1}" for i in range(10)]
# imprimir_lista_colores_alternados(otra_lista, color1="green", color2="yellow")


from rich.console import Console

def imprimir_palabras_colores_alternados(frase, color1="cyan", color2="magenta", color3="green"):
    """
    Imprime palabras de una frase en una sola línea con colores alternados
    en grupos de 3 palabras.

    Args:
        frase (str): La frase cuyas palabras se imprimirán.
        color1 (str): El primer color a usar (ej. "cyan", "green", "red").
        color2 (str): El segundo color a usar (ej. "magenta", "blue", "yellow").
        color3 (str): El tercer color a usar (ej. "green", "white", "orange").
    """
    console = Console()
    palabras = frase.split() # Divide la frase en una lista de palabras
    
    output_parts = [] # Lista para almacenar las partes con color
    
    for i, palabra in enumerate(palabras):
        modulo = i % 3 # Calcula el módulo para alternar cada 3 palabras
        
        if modulo == 0: # Primera palabra del grupo de tres
            output_parts.append(f"[{color1}]{palabra}[/{color1}]")
        elif modulo == 1: # Segunda palabra del grupo de tres
            output_parts.append(f"[{color2}]{palabra}[/{color2}]")
        else: # Tercera palabra del grupo de tres
            output_parts.append(f"[{color3}]{palabra}[/{color3}]")
            
    # Unir todas las partes con un espacio y luego imprimir
    console.print(" ".join(output_parts))

# --- Ejemplos de uso ---

print("--- Frase con colores alternados (3 en 3) ---")
mi_frase = "Aquí tenemos una frase de ejemplo para ver cómo funciona la alternancia de colores en grupos de tres palabras en la misma línea de texto."
imprimir_palabras_colores_alternados(mi_frase)

print("\n--- Otra frase con diferentes colores y menos palabras ---")
otra_frase = "Python es muy versátil y rich ayuda mucho en la consola"
imprimir_palabras_colores_alternados(otra_frase, color1="red", color2="blue", color3="yellow")

print("\n--- Una frase más larga ---")
frase_larga = "La programación en Python es una habilidad muy valorada en el mundo actual y permite crear soluciones innovadoras para problemas complejos de diversas índoles y tamaños."
imprimir_palabras_colores_alternados(frase_larga, color1="white", color2="cyan", color3="orange")
