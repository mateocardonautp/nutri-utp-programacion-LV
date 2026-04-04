from project.src.services.limpiar_pantalla import limpiar_terminal
from project.src.tools.funcionalidad_menu_plato import MostrarGuardarPlato , MostrarVistaPlatos


class MostrarMenuPlato:
    """
    Clase encargada de la capa de presentación para la gestión de platos.
    """
        
    def ejecutar_interfaz_plato(self):
        limpiar_terminal()
        """
        Mantiene el bucle de la interfaz de gestión de platos activo.
        """
        while True:
            self._encabezado_menu_plato()
            self._opciones_menu_plato()
            selector_opcion = SeleccionarMenuPlato()
            verificador = selector_opcion.verificar_opcion_menu_plato()
            if verificador == "volver_plato":
                continue
            elif verificador == "volver_anterior":
                return "volver_anterior"
        

    @staticmethod
    def _encabezado_menu_plato():

        print("\n", "=" * 10, "GESTION PLATO", "=" * 10)

    @staticmethod
    def _opciones_menu_plato():

        print("- 1. AGREGAR PLATO")
        print("- 2. VER PLATOS")
        print("- 3. VOLVER")
        print("=" * 34)


class SeleccionarMenuPlato:
    """
    Clase de lógica de control para la navegación del menú de platos.
    """
    def verificar_opcion_menu_plato(self):
        while True:
            try:
                opcion = int(input("\nEscriba la opcion que desee (1/3) : "))
                if opcion == 1:
                    selector = MostrarGuardarPlato()
                    validador = selector.ejecutar_interfaz_guardado_de_plato()
                    if validador == "volver_plato":
                        return "volver_plato"
    
                elif opcion == 2:
                    selector = MostrarVistaPlatos()
                    validador = selector.ejecutar_interfaz_visualizar_platos()
                    if validador == "volver_plato":
                        return "volver_plato"
                elif opcion == 3:
                    print("Volviendo al menu principal...")
                    return "volver_anterior"                        
                else:
                    print("Opción no valida. Intente de nuevo.")
            except ValueError:
                print("Error: Ingrese un valor numerico (1/3).")