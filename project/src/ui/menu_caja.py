import sys
import os


def _configurar_entorno_de_rutas_del_sistema_externo():
    
    ruta_raiz_del_proyecto_actual = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if ruta_raiz_del_proyecto_actual not in sys.path:
        sys.path.append(ruta_raiz_del_proyecto_actual)

_configurar_entorno_de_rutas_del_sistema_externo()


from src.services.limpiar_pantalla import limpiar_terminal
from src.services.tesoreria_mostrar import ReporteVisualizador

class MostrarMenuCaja:

    def __init__(self, interfaz_caja_utp_parametro, menu_hoy_parametro, gestor_reportes_parametro): 
        self.interfaz_caja_utp = interfaz_caja_utp_parametro
        self.menu_hoy = menu_hoy_parametro
        self.gestor_reportes = gestor_reportes_parametro 
        
    def ejecutar_interfaz_caja(self):
    
        while True:
            self._ejecutar_limpieza_de_pantalla_externa()
            self._encabezado_menu_caja()
            self._opciones_menu_caja()
            
            selector_de_opciones_caja = SeleccionarMenuCaja(
                self.interfaz_caja_utp, 
                self.menu_hoy, 
                self.gestor_reportes
            )
            
            verificador_de_estado_de_navegacion = selector_de_opciones_caja.verificar_opcion_menu_caja()
            
            if verificador_de_estado_de_navegacion == "volver_menu_caja":
                continue 
            elif verificador_de_estado_de_navegacion == "volver_anterior":
                return "volver_anterior" 
    
    def _ejecutar_limpieza_de_pantalla_externa(self):

        limpiar_terminal()

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


    def __init__(self, interfaz_caja_utp_recibida, menu_hoy_recibido, gestor_reportes_recibido):
    
        self._interfaz_caja_utp = interfaz_caja_utp_recibida
        self._menu_hoy = menu_hoy_recibido
        self._gestor_reportes = gestor_reportes_recibido

    def verificar_opcion_menu_caja(self):
    
        try:
            opcion_escogida_por_usuario = int(input("\nEscriba la opción que desee (1/3): "))
            return self._procesar_redireccion_de_caja(opcion_escogida_por_usuario)
                
        except ValueError:
            print("Error: Ingrese un valor numérico (1/3).")
            input("Presione ENTER para continuar...")
            return "volver_menu_caja"

    def _procesar_redireccion_de_caja(self, numero_de_opcion_parametro):

        if numero_de_opcion_parametro == 1:
            self._ejecutar_proceso_de_cobro_externo()
            return "volver_menu_caja"
            
        elif numero_de_opcion_parametro == 2:
            self._ejecutar_visualizacion_de_reporte_externo()
            return "volver_menu_caja"
            
        elif numero_de_opcion_parametro == 3:
            return "volver_anterior"
            
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione ENTER para continuar...")
            return "volver_menu_caja"



    def _ejecutar_proceso_de_cobro_externo(self):
    
        self._interfaz_caja_utp.ejecutar_cobro_menu_actual(self._menu_hoy)

    def _ejecutar_visualizacion_de_reporte_externo(self):
    
        lista_de_datos_de_ventas_extraida = self._gestor_reportes.leer_todas_las_ventas()
        ReporteVisualizador.mostrar_resumen(lista_de_datos_de_ventas_extraida)