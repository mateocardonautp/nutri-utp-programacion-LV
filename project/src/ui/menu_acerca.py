from project.src.services.limpiar_pantalla import limpiar_terminal

class InterfazAcerca:

    @staticmethod
    def imprimir_acerca():
        print("\nRealizado por Mateo Osorio Cardona | Programación IV | Universidad Tecnológica de Pereira")


class MostrarMenuAcerca:

  
    def ejecutar_interfaz_acerca_menu(self):
    
        self._ejecutar_limpieza_pantalla()
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

    def _ejecutar_limpieza_pantalla(self):
        
        limpiar_terminal()


class SeleccionarMenuAcerca:

    def verificar_opcion_menu_acerca(self):

        while True:
            try:
                opcion = int(input("\nEscriba la opcion que desee (1/2) : "))
                return self._procesar_seleccion(opcion)
            except ValueError:
                print("Error: Ingrese un valor numérico (1/2).")

    def _procesar_seleccion(self, opcion):
    
        if opcion == 1:
            self._ejecutar_limpieza_pantalla()
            self._mostrar_info_acerca_externa()
            return "volver_acerca"
        
        elif opcion == 2:
            print("Volviendo al menu principal...")
            return "volver_anterior"
        
        else:
            print("Opcion no valida. Intente de nuevo.")
            return "reintentar"
        
    def _ejecutar_limpieza_pantalla(self):

        limpiar_terminal()

    def _mostrar_info_acerca_externa(self):
    
        InterfazAcerca.imprimir_acerca()