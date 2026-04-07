


from project.src.ui.menu_acerca import MostrarMenuAcerca
from project.src.ui.menu_plato import MostrarMenuPlato
from project.src.ui.menu_dia import SeleccionarMenuDelDia, MostrarMenu
from project.src.ui.menu_caja import MostrarMenuCaja
from project.src.ui.interfaz_saliendo_del_programa import saliendo_del_programa

from project.src.models.comensal import Comensal, CalcularPrecioComensal
from project.src.services.procesador_venta import ProcesadorVenta, InterfazCajaUTP
from project.src.services.gestor_de_archivo_tesoreria import GestorReportesCSV
from project.src.services.limpiar_pantalla import limpiar_terminal
from project.src.tools.funcionalidad_menu_dia import FuncionalidadMenuDia, archivo_platos, archivo_menu

class AppFactory:

    
    @staticmethod
    def construir_modulo_caja():
        ruta_ventas = "project/src/tesoreria/ventas.csv"
        
        motor_archivos = FuncionalidadMenuDia(archivo_platos, archivo_menu)
        menu_hoy = motor_archivos.preparar_y_obtener()
        
        gestor_reportes = GestorReportesCSV(ruta_ventas)
        estudiante = Comensal(id_estudiante="", tipo_subsidio="None")
        calculadora = CalcularPrecioComensal(estudiante)
        procesador = ProcesadorVenta(calculadora, gestor_reportes)
        
        return MostrarMenuCaja(InterfazCajaUTP(procesador), menu_hoy, gestor_reportes)

    @staticmethod
    def construir_menu_dia():
        selector_funcion = FuncionalidadMenuDia(archivo_platos, archivo_menu)
        menu_instanciado = selector_funcion.preparar_y_obtener()
        return SeleccionarMenuDelDia(menu_instanciado)


class MostrarMenuPrincipal:
    def ejecutar_interfaz_menu_principal(self):
        selector_opcion = SeleccionarMenuPrincipal()
        
        while True:
            self._limpiar_pantalla_externa()
            self._dibujar_interfaz()
            
            resultado = selector_opcion.gestionar_entrada_usuario()

            if resultado == "salir_del_programa":
                break
    
    def _dibujar_interfaz(self):
        print("\n", "=" * 10, "NUTRI-UTP", "=" * 10)
        print("-1. MENU DEL DIA")
        print("-2. GESTOR DE PLATOS")
        print("-3. NUTRI-UTP CAJA")
        print("-4. ACERCA")
        print("-5. SALIR")
        print("=" * 33)


    def _limpiar_pantalla_externa(self):
        limpiar_terminal()


class SeleccionarMenuPrincipal:
    
    def gestionar_entrada_usuario(self):
        try:
            opcion = int(input("\nEscriba la opcion que desee (1/5) : "))
        except ValueError:
            print("Error: Ingrese un valor numerico (1/5).")
            input("Presione Enter para continuar...")
            return "volver_anterior"

        return self._redireccionar(opcion)

    def _redireccionar(self, opcion):
        opciones = {
            1: self._flujo_menu_dia,
            2: self._flujo_menu_plato,
            3: self._flujo_menu_caja,
            4: self._flujo_menu_acerca,
        }

        if opcion in opciones:
            return opciones[opcion]()
        elif opcion == 5:
            return self._ejecutar_salida_externa() 
        
        print("Opción no válida.")
        input("Presione Enter para continuar...")
        return "volver_anterior"


    def _flujo_menu_dia(self):
    
        interfaz_selector = AppFactory.construir_menu_dia()
        platos_filtrados = interfaz_selector.ejecutar_interfaz_seleccion()
        
        MostrarMenu.mostrar_menu_del_dia(platos_filtrados)
        
        input("\nPresione Enter para volver...")
        return "volver_anterior"

    def _flujo_menu_plato(self):
    
        menu_plato = MostrarMenuPlato()
        menu_plato.ejecutar_interfaz_plato()
        return "volver_anterior"

    def _flujo_menu_caja(self):

        caja = AppFactory.construir_modulo_caja()
        caja.ejecutar_interfaz_caja()
        return "volver_anterior"

    def _flujo_menu_acerca(self):

        menu_acerca = MostrarMenuAcerca()
        menu_acerca.ejecutar_interfaz_acerca_menu()

        return "volver_anterior"

    def _ejecutar_salida_externa(self):
    
        return saliendo_del_programa()