from project.src.ui.menu_principal import MostrarMenuPrincipal
from project.src.services.limpiar_pantalla import limpiar_terminal


def inicial():
    """
    Inicializa la aplicación limpiando la terminal y ejecutando 
    """
    limpiar_terminal()
    inicializador = MostrarMenuPrincipal()
    inicializador.ejecutar_interfaz_menu_principal()


if __name__ == "__main__":
    inicial()