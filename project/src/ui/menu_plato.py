from project.src.services.limpiar_pantalla import limpiar_terminal
from project.src.tools.funcionalidad_menu_plato import MostrarGuardarPlato, MostrarVistaPlatos

class MostrarMenuPlato:

    def ejecutar_interfaz_plato(self):
        self._limpiar_pantalla_externa()
        
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


    def _limpiar_pantalla_externa(self):

        limpiar_terminal()


class SeleccionarMenuPlato:

    def verificar_opcion_menu_plato(self):
        while True:
            try:
                opcion = int(input("\nEscriba la opcion que desee (1/3) : "))
                return self._procesar_seleccion(opcion)
            except ValueError:
                print("Error: Ingrese un valor numerico (1/3).")

    def _procesar_seleccion(self, opcion):
        opciones = {
            1: self._ejecutar_flujo_guardado,
            2: self._ejecutar_flujo_visualizacion,
        }
        
        if opcion in opciones:
            return opciones[opcion]()
        elif opcion == 3:
            print("Volviendo al menu principal...")
            return "volver_anterior"




    def _ejecutar_flujo_guardado(self):
    
        interfaz = MostrarGuardarPlato()
        return interfaz.ejecutar_interfaz_guardado_de_plato()

    def _ejecutar_flujo_visualizacion(self):
        
        interfaz = MostrarVistaPlatos()
        return interfaz.ejecutar_interfaz_visualizar_platos()