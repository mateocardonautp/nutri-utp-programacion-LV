import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.services.limpiar_pantalla import limpiar_terminal
from src.services.tesoreria_mostrar  import ReporteVisualizador  #

class MostrarMenuCaja:
    def __init__(self, interfaz_caja_utp, menu_hoy, gestor_reportes): 
        self.interfaz_caja_utp = interfaz_caja_utp
        self.menu_hoy = menu_hoy
        self.gestor_reportes = gestor_reportes 
        
    def ejecutar_interfaz_caja(self):
        while True:
            limpiar_terminal()
            self._encabezado_menu_caja()
            self._opciones_menu_caja()
            
    
            selector = SeleccionarMenuCaja(self.interfaz_caja_utp, self.menu_hoy, self.gestor_reportes)
            verificador = selector.verificar_opcion_menu_caja()
            
            if verificador == "volver_menu_caja":
                continue 
            elif verificador == "volver_anterior":
                return "volver_anterior" 
        
    @staticmethod
    def _encabezado_menu_caja():
        print("\n", "=" * 10, "GESTION DE CAJA NUTRI-UTP", "=" * 10)

    @staticmethod
    def _opciones_menu_caja():
        print("- 1. PROCESAR VENTA")
        print("- 2. VER RESUMEN DE VENTAS (Reporte)") 
        print("- 3. VOLVER AL MENU PRINCIPAL")
        print("=" * 47)


class SeleccionarMenuCaja:

    def __init__(self, interfaz_caja_utp, menu_hoy, gestor_reportes):
        self.interfaz_caja_utp = interfaz_caja_utp
        self.menu_hoy = menu_hoy
        self.gestor_reportes = gestor_reportes

    def verificar_opcion_menu_caja(self):
        try:
            opcion = int(input("\nEscriba la opción que desee (1/3): "))
            
            if opcion == 1:
            
                self.interfaz_caja_utp.ejecutar_cobro_menu_actual(self.menu_hoy)
                return "volver_menu_caja"
                
            elif opcion == 2:
        
                datos_ventas = self.gestor_reportes.leer_todas_las_ventas()
                
                # B. Llamamos al visualizador para que los muestre bonitos
                ReporteVisualizador.mostrar_resumen(datos_ventas)
                
                return "volver_menu_caja"
                
            elif opcion == 3:
                return "volver_anterior"
                
            else:
                print("Opción no válida. Intente de nuevo.")
                input("Presione ENTER...")
                return "volver_menu_caja"
                
        except ValueError:
            print("Error: Ingrese un valor numérico (1/3).")
            input("Presione ENTER...")
            return "volver_menu_caja"