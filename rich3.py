'''
rich3 example
'''


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

# print("\n--- Otra frase con diferentes colores y menos palabras ---")
# otra_frase = "Python es muy versátil y rich ayuda mucho en la consola"
# imprimir_palabras_colores_alternados(otra_frase, color1="red", color2="blue", color3="yellow")

# print("\n--- Una frase más larga ---")
# frase_larga = "La programación en Python es una habilidad muy valorada en el mundo actual y permite crear soluciones innovadoras para problemas complejos de diversas índoles y tamaños."
# imprimir_palabras_colores_alternados(frase_larga, color1="white", color2="cyan", color3="orange")
