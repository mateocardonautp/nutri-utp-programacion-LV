from src.src.ui.menu_principal import MostrarMenuPrincipal
from src.src.services.limpiar_pantalla import limpiar_terminal


def inicial():
    limpiar_terminal()
    inicializador = MostrarMenuPrincipal()
    inicializador.ejecutar_interfaz_menu_principal()


inicial()