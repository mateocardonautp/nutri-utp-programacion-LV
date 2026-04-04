import sys
import os



sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.models.plato import Plato
from src.ui.menu_dia import FechaMenu
from src.models.comensal import  CalcularPrecioComensal
from src.services.gestor_de_archivo_tesoreria import GestorReportesCSV
from src.services.limpiar_pantalla import limpiar_terminal

class ProcesadorVenta:
    """
    Clase encargada de orquestar la lógica final de una transacción.
    """

    def __init__(self, calculadora: CalcularPrecioComensal, gestor_reportes: GestorReportesCSV):
        """
        Inicializa el procesador con sus herramientas de cálculo y persistencia.
        """
        self.calculadora = calculadora
        self.gestor_reportes = gestor_reportes 

    def generar_tiquete(self, plato: Plato):
        """
        Genera la representación visual de la venta y persiste los datos.
        """
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

        # Persistencia en el archivo de reportes
        self.gestor_reportes.registrar_venta(
            self.calculadora.comensal.id_estudiante, 
            plato.nombre, 
            precio_final
        )
        
        self.validar_pago(precio_final)

    def validar_pago(self, monto: float):
        """Simula la validación del pago con el sistema central de tesorería."""
        print(f"Comunicando con Tesorería UTP...")
        print(f"Estado: Pago de ${monto} validado correctamente.")
        return True
    

class InterfazCajaUTP:
    """
    Clase de interfaz de usuario (CLI) para el proceso de cobre
    """

    def __init__(self, procesador: ProcesadorVenta):
        self.procesador = procesador

    def ejecutar_cobro_menu_actual(self, menu_dia_instanciado):
        """
        Inicia el flujo de trabajo para cobrar un servicio de almuerzo.
        """
        limpiar_terminal()
        print("\n" + "="*15, "SISTEMA DE COBRO NUTRI-UTP", "="*15)
        
        id_comensal = input("Escriba la ID del estudiante: ")
        
        print("\nSeleccione el subsidio (Escriba tal cual):")
        print("- Subsidio | - Subsidio parcial | - Subsidio semi parcial | - None")
        subsidio_comensal = input("Subsidio: ")
        

        self.procesador.calculadora.comensal.id_estudiante = id_comensal
        self.procesador.calculadora.comensal.tipo_subsidio = subsidio_comensal

        print("\n¿Qué tipo de plato desea?")
        print("1. Menu Estándar")
        print("2. Menu Vegetariano")
        
        try:
            tipo_opcion = int(input("Seleccione (1/2): "))
            es_vegetariano = (tipo_opcion == 2)
    
            platos_filtrados = menu_dia_instanciado.seleccionar_opcion(es_vegetariano)

            if not platos_filtrados:
                print(f"\n[!] No hay platos {"vegetarianos" if es_vegetariano else "estándar"} disponibles hoy.")
                input("\nPresione ENTER para volver...")
                return
    

            print(f"\n--- OPCIONES {"VEGETARIANAS" if es_vegetariano else "ESTÁNDAR"} ---")
            for numero_de_plato, plato in enumerate(platos_filtrados):
                print(f"{numero_de_plato+1}. {plato.nombre} (${plato.precio})")
            
            opcion_del_plato = int(input("\nSeleccione el número del plato: ")) - 1
            
            if 0 <= opcion_del_plato < len(platos_filtrados):
    
                self.procesador.generar_tiquete(platos_filtrados[opcion_del_plato])
                input("\n>>> Venta finalizada. Presione ENTER para regresar al menú principal...")
                return 
            else:
                print("Error: Selección fuera de rango.")
                input("Presione ENTER para continuar...")

        except (ValueError, KeyError) as error:
            print(f"\n[!] Error en el proceso: {error}")
            input("Presione ENTER para volver...")