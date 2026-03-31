from src.src.services.limpiar_pantalla import limpiar_terminal


class InterfazAcerca:
    @staticmethod
    def imprimir_acerca():
        print("\nRealizado por Mateo Osorio Cardona | Programación IV | Universidad Tecnológica de Pereira")


class MostrarMenuAcerca:
    def __init__(self):
        limpiar_terminal()
        
    def ejecutar_interfaz_acerca_menu(self):
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
        print("- 2. MANUAL DE USO")
        print("- 3. VOLVER")
        print("=" * 34)


class SeleccionarMenuAcerca:
    def verificar_opcion_menu_acerca(self):
        while True:
            try:
                opcion = int(input("\nEscriba la opcion que desee (1/3) : "))
                if opcion == 1:
                    InterfazAcerca.imprimir_acerca()     
                    return "volver_acerca"
                elif opcion == 2:
                    print("Función de MANUAL DE USO no implementada aún.")
                elif opcion == 3:
                    print("Volviendo al menú principal...")
                    return "volver_anterior"                        
                else:
                    print("Opcion no valida. Intente de nuevo.")
            except ValueError:
                print("Error: Ingrese un valor numérico (1/3).")