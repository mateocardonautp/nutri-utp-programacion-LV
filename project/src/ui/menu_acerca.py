from project.src.services.limpiar_pantalla import limpiar_terminal


class InterfazAcerca:
    """
    Clase de utilidad para la visualización de Acerca.
    """
    @staticmethod
    def imprimir_acerca():
        print("\nRealizado por Mateo Osorio Cardona | Programación IV | Universidad Tecnológica de Pereira")


class MostrarMenuAcerca:
    """
    Clase encargada de la capa de presentación del menú 'Acerca de'.
    """
    def __init__(self):
        """Inicializa la interfaz limpiando la pantalla de la terminal."""
        
        
    def ejecutar_interfaz_acerca_menu(self):
        """
        Mantiene el bucle de la interfaz activo.
        """
        limpiar_terminal()
        while True:
            self._encabezado_menu_acerca()
            self._opciones_menu_acerca()
            selector_opcion = SeleccionarMenuAcerca()
            verificador = selector_opcion.verificar_opcion_menu_acerca()
            if verificador == "volver_acerca":
                continue
            elif verificador == "volver_anterior":
                return "volver_anterior"
        

    @staticmethod
    def _encabezado_menu_acerca():
        print("\n", "=" * 10, "ACERCA-UTP", "=" * 10)

    @staticmethod
    def _opciones_menu_acerca():
        print("- 1. ACERCA")
        print("- 2. VOLVER")
        print("=" * 34)


class SeleccionarMenuAcerca:
    """
    Clase encargada de la lógica de control para el menú Acerca de.
    """
    def verificar_opcion_menu_acerca(self):
        """
        Solicita y valida la opción ingresada por el usuario.
        """
        while True:
            try:
                opcion = int(input("\nEscriba la opcion que desee (1/2) : "))
                if opcion == 1:
                    limpiar_terminal()
                    InterfazAcerca.imprimir_acerca()     
                    return "volver_acerca"
                elif opcion == 2:
                    print("Volviendo al menu principal...")
                    return "volver_anterior"                        
                else:
                    print("Opcion no valida. Intente de nuevo.")
            except ValueError:
                print("Error: Ingrese un valor numérico (1/2).")