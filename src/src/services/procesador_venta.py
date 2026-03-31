import sys
import os
from datetime import datetime

# 1. Configuración de Rutas para importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


from src.models.plato import Plato
from src.ui.menu_dia import FechaMenu
from src.models.comensal import Comensal, CalcularPrecioComensal
from src.tools.funcionalidad_menu_dia import FuncionalidadMenuDia, archivo_platos, archivo_menu

from src.models.plato import Plato
from src.models.comensal import CalcularPrecioComensal
from src.ui.menu_dia import FechaMenu
from src.services.gestor_de_archivo_tesoreria import  GestorReportesCSV

from src.services.limpiar_pantalla import limpiar_terminal

limpiar_terminal()


class ProcesadorVenta:
    """
    Responsabilidad: Coordinar la transacción final.
    """

    def __init__(self, calculadora: CalcularPrecioComensal, gestor_reportes: GestorReportesCSV):
        self.calculadora = calculadora
        self.gestor_reportes = gestor_reportes 

    def generar_tiquete(self, plato: Plato):
        precio_final = self.calculadora.obtener_precio_final(plato.precio)
        
        print("\n" + "---" * 12)
        print("      TIQUETE DE VENTA NUTRI-UTP      ")
        print("---" * 12)
        print(f"Fecha:      {FechaMenu.obtener_fecha()}")
        print(f"Estudiante: {self.calculadora.comensal.id_estudiante}")
        print(f"Plato:      {plato.nombre}")
        print(f"Subsidio:   {self.calculadora.comensal.tipo_subsidio}")
        print(f"Total:      ${precio_final}")
        print("---" * 12)

        self.gestor_reportes.registrar_venta(
            self.calculadora.comensal.id_estudiante, 
            plato.nombre, 
            precio_final
        )
        
        self.validar_pago(precio_final)

    def validar_pago(self, monto: float):
        print(f"Comunicando con Tesorería UTP...")
        print(f"Estado: Pago de ${monto} validado correctamente.")
        return True
    
    

class InterfazCajaUTP:
   
    def __init__(self, procesador: ProcesadorVenta):
        self.procesador = procesador

    def ejecutar_cobro_menu_actual(self, menu_dia_instanciado):
        limpiar_terminal()
        print("\n" + "="*15, "SISTEMA DE COBRO NUTRI-UTP", "="*15)
        
     
        id_user = input("Escriba la ID del estudiante: ")
        
        print("\nSeleccione el subsidio (Escriba tal cual):")
        print("- Subsidio | - Subsidio parcial | - Subsidio semi parcial | - None")
        subsidio_user = input("Subsidio: ")
        
    
        self.procesador.calculadora.comensal.id_estudiante = id_user
        self.procesador.calculadora.comensal._tipo_subsidio = subsidio_user

   
        print("\n¿Qué tipo de plato desea?")
        print("1. Menu Estándar")
        print("2. Menu Vegetariano")
        
        try:
            tipo_opcion = int(input("Seleccione (1/2): "))
            es_vege = (tipo_opcion == 2)
            
        
            platos_filtrados = menu_dia_instanciado.seleccionar_opcion(es_vege)

            if not platos_filtrados:
                print(f"\n[!] No hay platos {'vegetarianos' if es_vege else 'estándar'} disponibles hoy.")
                input("\nPresione ENTER para volver...")
                return

            # 3. Selección de plato y generación de tiquete
            print(f"\n--- OPCIONES {'VEGETARIANAS' if es_vege else 'ESTÁNDAR'} ---")
            for i, plato in enumerate(platos_filtrados):
                print(f"{i+1}. {plato.nombre} (${plato.precio})")
            
            opcion_idx = int(input("\nSeleccione el número del plato: ")) - 1
            
            if 0 <= opcion_idx < len(platos_filtrados):
                # GENERACIÓN DEL TICKET REAL
                self.procesador.generar_tiquete(platos_filtrados[opcion_idx])
                
                # PAUSA CRÍTICA: Permite leer el ticket antes de volver
                input("\n>>> Venta finalizada. Presione ENTER para regresar al menú principal...")
                return # Volvemos al bucle del menú principal
            else:
                print("Error: Selección fuera de rango.")
                input("Presione ENTER para continuar...")

        except (ValueError, KeyError) as e:
            print(f"\n[!] Error en el proceso: {e}")
            input("Presione ENTER para volver...")
