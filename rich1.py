'''
rich_1 example
'''

from rich.console import Console
from rich.text import Text
from rich.align import Align

console = Console()


if __name__ ==  '__main__':    
    console.print('\n\tcasa\n')
    # Imprimir texto con color y estilo
    console.print("[bold magenta]Hola, mundo![/bold magenta]")
    console.print("Este es un texto [green]verde[/green] y este es [underline blue]subrayado azul[/underline blue].")

    # Usando el objeto Text para una mayor granularidad
    text = Text("¡Rich es ")
    text.append("increíble", style="italic yellow")
    text.append(" para la terminal!", style="bold red on white")
    console.print(text)

    # Imprimir algo diferente
    console.print("Aquí hay un [bold green]emoji[/bold green] :smiley: y un [bold blue]icono[/bold blue] :thumbs_up:.")

    # Centrar texto
    console.print(Align.center("[bold cyan]Texto Centrado[/bold cyan]"))

    # Justificar texto a la derecha
    console.print(Align.right("[bold red]Texto a la Derecha[/bold red]"))