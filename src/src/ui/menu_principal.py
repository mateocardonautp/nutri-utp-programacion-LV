from src.src.ui.menu_acerca import MostrarMenuAcerca
from src.src.ui.menu_plato import MostrarMenuPlato
from src.src.ui.menu_dia import SeleccionarMenuDelDia, MostrarMenu
from src.src.ui.menu_caja import MostrarMenuCaja
from src.src.ui.interfaz_saliendo_del_programa import saliendo_del_programa

from src.src.models.comensal import Comensal, CalcularPrecioComensal
from src.src.services.procesador_venta import ProcesadorVenta, InterfazCajaUTP
from src.src.services.gestor_de_archivo_tesoreria import GestorReportesCSV
from src.src.services.limpiar_pantalla import limpiar_terminal
from src.src.tools.funcionalidad_menu_dia import FuncionalidadMenuDia, archivo_platos, archivo_menu


class MostrarMenuPrincipal:
    def __init__(self):
        limpiar_terminal()

    def ejecutar_interfaz_menu_principal(self):
        while True:
            self._encabezado_menu_principal()
            self._opciones_menu_principal()

            selector_opcion = SeleccionarMenuPrincipal()
            verificador = selector_opcion.verificar_opcion_menu_principal()

            if verificador == "volver_anterior":
                limpiar_terminal()
                continue
            elif verificador == "salir_del_programa":
                break

    @staticmethod
    def _encabezado_menu_principal():
        print("\n", "=" * 10, "NUTRI-UTP", "=" * 10)

    @staticmethod
    def _opciones_menu_principal():
        print("-1. MENU DEL DIA")
        print("-2. GESTOR DE PLATOS")
        print("-3. NUTRI-UTP CAJA")
        print("-4. ACERCA")
        print("-5. SALIR")
        print("=" * 33)


class SeleccionarMenuPrincipal:

    def verificar_opcion_menu_principal(self):
        while True:
            try:
                opcion = int(input("\nEscriba la opcion que desee (1/5) : "))
            except ValueError:
                print("Error: Ingrese un valor numérico (1/5).")
                continue                      

        
            if opcion == 1:
                return self._ejecutar_menu_dia()
            elif opcion == 2:
                return self._ejecutar_menu_plato()
            elif opcion == 3:
                return self._ejecutar_menu_caja()
            elif opcion == 4:
                return self._ejecutar_menu_acerca()
            elif opcion == 5:
                if saliendo_del_programa() == "salir_del_programa":
                    return "salir_del_programa"
                return "volver_anterior"
            else:
                print("Opción no válida. Intente de nuevo.")

    def _ejecutar_menu_dia(self):
        selector         = FuncionalidadMenuDia(archivo_platos, archivo_menu)
        menu_instanciado = selector.preparar_y_obtener()
        interfaz_selector = SeleccionarMenuDelDia(menu_instanciado)
        platos_filtrados = interfaz_selector.ejecutar_interfaz_seleccion()
        MostrarMenu.mostrar_menu_del_dia(platos_filtrados)
        input("\nPresione Enter para volver...")
        return "volver_anterior"

    def _ejecutar_menu_plato(self):
        selector = MostrarMenuPlato()
        selector.ejecutar_interfaz_plato()
        return "volver_anterior"

    def _ejecutar_menu_caja(self):
        caja = self._construir_caja()
        caja.ejecutar_interfaz_caja()
        return "volver_anterior"

    def _ejecutar_menu_acerca(self):
        selector = MostrarMenuAcerca()
        selector.ejecutar_interfaz_acerca_menu()
        return "volver_anterior"

    def _construir_caja(self):
        ruta_ventas  = "src/src/tesoreria/ventas.csv"
        motor_archivos       = FuncionalidadMenuDia(archivo_platos, archivo_menu)
        menu_hoy     = motor_archivos.preparar_y_obtener()
        gestor_reportes   = GestorReportesCSV(ruta_ventas)
        estudiante   = Comensal(id_estudiante="", tipo_subsidio="None")
        calculadora  = CalcularPrecioComensal(estudiante)
        procesador   = ProcesadorVenta(calculadora, gestor_reportes)
        return MostrarMenuCaja(InterfazCajaUTP(procesador), menu_hoy, gestor_reportes)