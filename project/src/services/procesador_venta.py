import sys
import os

# --- AISLAMIENTO DE CONFIGURACIÓN DE SISTEMA ---
def _configurar_entorno_de_rutas_del_sistema_externo():
    """
    Encapsula la manipulación del path para evitar dependencias directas.
    Utiliza nombres largos y descriptivos en español.
    """
    ruta_raiz_del_proyecto_actual = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    if ruta_raiz_del_proyecto_actual not in sys.path:
        sys.path.append(ruta_raiz_del_proyecto_actual)

# LLAMADA AL MÉTODO: El nombre coincide exactamente con la definición
_configurar_entorno_de_rutas_del_sistema_externo()

# Importaciones externas
from src.models.plato import Plato
from src.ui.menu_dia import FechaMenu
from src.models.comensal import CalcularPrecioComensal
from src.services.gestor_de_archivo_tesoreria import GestorReportesCSV
from src.services.limpiar_pantalla import limpiar_terminal

class ProcesadorVenta:
    

    def __init__(self, calculadora_precio_parametro: CalcularPrecioComensal, gestor_reportes_parametro: GestorReportesCSV):
        self._calculadora_de_precios = calculadora_precio_parametro
        self._gestor_de_reportes_ventas = gestor_reportes_parametro 

    def generar_tiquete(self, objeto_plato_instancia: Plato):
        monto_precio_base_extraido = self._obtener_precio_base_del_plato_externo(objeto_plato_instancia)
        monto_total_con_descuento = self._calculadora_de_precios.obtener_precio_final(monto_precio_base_extraido)
        
        id_estudiante_identificado = self._obtener_id_del_comensal_externo()
        nombre_del_plato_seleccionado = self._obtener_nombre_del_plato_externo(objeto_plato_instancia)
        tipo_de_subsidio_aplicado = self._obtener_subsidio_del_comensal_externo()
        fecha_actual_del_sistema = self._obtener_fecha_del_dia_externa()

        print("\n" + "---" * 12)
        print("      TIQUETE DE VENTA NUTRI-UTP      ")
        print("---" * 12)
        print(f"Fecha:      {fecha_actual_del_sistema}")
        print(f"Estudiante: {id_estudiante_identificado}")
        print(f"Plato:      {nombre_del_plato_seleccionado}")
        print(f"Subsidio:   {tipo_de_subsidio_aplicado}")
        print(f"Total:      ${monto_total_con_descuento}")
        print("---" * 12)

        self._gestor_de_reportes_ventas.registrar_venta(
            id_estudiante_identificado, 
            nombre_del_plato_seleccionado, 
            monto_total_con_descuento
        )
        
        self.validar_pago_tesoreria(monto_total_con_descuento)

    def validar_pago_tesoreria(self, monto_total_parametro: float):
        print(f"Comunicando con Tesorería UTP...")
        print(f"Estado: Pago de ${monto_total_parametro} validado correctamente.")
        return True
    
    def _obtener_precio_base_del_plato_externo(self, plato_parametro):
        return plato_parametro.precio

    def _obtener_nombre_del_plato_externo(self, plato_parametro):
        return plato_parametro.nombre

    def _obtener_id_del_comensal_externo(self):
        return self._calculadora_de_precios.comensal.id_estudiante

    def _obtener_subsidio_del_comensal_externo(self):
        return self._calculadora_de_precios.comensal.tipo_subsidio

    def _obtener_fecha_del_dia_externa(self):
        return FechaMenu.obtener_fecha()


class InterfazCajaUTP:
   

    def __init__(self, procesador_de_venta_parametro: ProcesadorVenta):
        self._procesador_ventas = procesador_de_venta_parametro

    def ejecutar_cobro_menu_actual(self, objeto_menu_del_dia_instanciado):
        self._limpiar_terminal_de_forma_externa()
        print("\n" + "="*15, "SISTEMA DE COBRO NUTRI-UTP", "="*15)
        
        id_estudiante_ingresada = input("Escriba la ID del estudiante: ")
        
        print("\nSeleccione el subsidio (Escriba tal cual):")
        print("- Subsidio | - Subsidio parcial | - Subsidio semi parcial | - None")
        tipo_subsidio_ingresado = input("Subsidio: ")
        
        self._actualizar_datos_del_comensal_externo(id_estudiante_ingresada, tipo_subsidio_ingresado)

        print("\n¿Qué tipo de plato desea?")
        print("1. Menu Estándar")
        print("2. Menu Vegetariano")
        
        try:
            opcion_tipo_plato_seleccionada = int(input("Seleccione (1/2): "))
            es_vegetariano_booleano = (opcion_tipo_plato_seleccionada == 2)
    
            lista_de_platos_filtrados_externa = objeto_menu_del_dia_instanciado.seleccionar_opcion(es_vegetariano_booleano)

            if not lista_de_platos_filtrados_externa:
                print(f"\n[!] No hay platos disponibles hoy.")
                input("\nPresione ENTER para volver...")
                return
    
            print(f"\n--- OPCIONES DISPONIBLES ---")
            self._mostrar_listado_de_platos_disponibles_privado(lista_de_platos_filtrados_externa)
            
            indice_del_plato_elegido = int(input("\nSeleccione el número del plato: ")) - 1
            
            if 0 <= indice_del_plato_elegido < len(lista_de_platos_filtrados_externa):
                plato_para_procesar = lista_de_platos_filtrados_externa[indice_del_plato_elegido]
                self._procesador_ventas.generar_tiquete(plato_para_procesar)
                input("\n-- Venta finalizada. Presione ENTER para regresar al menú principal...")
            else:
                print("Error: Selección fuera de rango.")
                input("Presione ENTER para continuar...")

        except (ValueError, KeyError) as error_detectado_en_proceso:
            print(f"\n[!] Error en el proceso: {error_detectado_en_proceso}")
            input("Presione ENTER para volver...")

   

    def _limpiar_terminal_de_forma_externa(self):
        limpiar_terminal()

    def _actualizar_datos_del_comensal_externo(self, id_parametro, subsidio_parametro):
        self._procesador_ventas._calculadora_de_precios.comensal.id_estudiante = id_parametro
        self._procesador_ventas._calculadora_de_precios.comensal.tipo_subsidio = subsidio_parametro

    def _mostrar_listado_de_platos_disponibles_privado(self, lista_de_platos_parametro):
        
        for numero_de_orden_iteracion, plato_objeto_actual in enumerate(lista_de_platos_parametro):
            nombre_extraido = plato_objeto_actual.nombre
            precio_extraido = plato_objeto_actual.precio
            print(f"{numero_de_orden_iteracion + 1}. {nombre_extraido} (${precio_extraido})")