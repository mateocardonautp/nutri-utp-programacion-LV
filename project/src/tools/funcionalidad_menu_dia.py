import random
import sys
import os
from datetime import datetime


def _configurar_entorno_de_rutas_del_sistema():

    ruta_raiz_del_proyecto = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if ruta_raiz_del_proyecto not in sys.path:
        sys.path.append(ruta_raiz_del_proyecto)

_configurar_entorno_de_rutas_del_sistema()

from src.ui.menu_dia import MenuDia
from src.services.gestor_de_archivos_csv import GestorArchivoCSV, ServicioCargaPlatos

class GeneradorMenuDia:
    

    def __init__(self, archivo_plato_parametro, archivo_menu_parametro):
    
        self._archivo_plato = archivo_plato_parametro
        self._gestor_dia = archivo_menu_parametro

    def generar_si_no_existe(self):
    
        if self._verificar_existencia_de_datos_externos():
            return
        
        seleccion_de_platos_aleatorios = self._seleccionar_platos()
        self._guardar_seleccion_en_persistencia(seleccion_de_platos_aleatorios)

    def _seleccionar_platos(self):
    
        lista_de_todos_los_platos = self._archivo_plato.obtener_todos_los_platos()
        
        platos_vegetarianos = [plato for plato in lista_de_todos_los_platos if plato.es_vegetariano is True]
        platos_estandar = [plato for plato in lista_de_todos_los_platos if plato.es_vegetariano is False]
        
        if not platos_vegetarianos and not platos_estandar:
            raise ValueError("No se pudieron cargar platos desde platos.csv")
            
        
        cantidad_estandar = min(len(platos_estandar), 3)
        cantidad_vegeteriana = min(len(platos_vegetarianos), 1)
        
        return (self._obtener_muestra_aleatoria_externa(platos_estandar, cantidad_estandar) +
                self._obtener_muestra_aleatoria_externa(platos_vegetarianos, cantidad_vegeteriana))



    def _verificar_existencia_de_datos_externos(self):

        return self._gestor_dia.leer_objetos()

    def _obtener_muestra_aleatoria_externa(self, lista_fuente, cantidad_muestreo):
    
        return random.sample(lista_fuente, cantidad_muestreo)

    def _guardar_seleccion_en_persistencia(self, lista_seleccionada):
    
        for plato_objeto_instancia in lista_seleccionada:
            self._gestor_dia.guardar_objeto(plato_objeto_instancia)


class FuncionalidadMenuDia:


    def __init__(self, motor_plato_parametro: GestorArchivoCSV, motor_menu_parametro: GestorArchivoCSV):
        self._motor_plato = motor_plato_parametro         
        self._motor_menu  = motor_menu_parametro

    def preparar_y_obtener(self):

        servicio_carga = self._instanciar_servicio_carga_externo(self._motor_plato)
        
        generador_instancia = GeneradorMenuDia(servicio_carga, self._motor_menu)
        generador_instancia.generar_si_no_existe()
        
        platos_de_hoy_extraidos = servicio_carga.obtener_todos_los_platos()
        
        return self._crear_objeto_menu_dia_externo(platos_de_hoy_extraidos)

    def _instanciar_servicio_carga_externo(self, motor_persistencia):

        return ServicioCargaPlatos(motor_persistencia)

    def _crear_objeto_menu_dia_externo(self, lista_de_opciones):
        
        return MenuDia(opciones=lista_de_opciones)




def _obtener_nombre_archivo_fecha_externo():

    formato_fecha_archivo = datetime.now().strftime('%d_%m_%Y')
    return f"menu_{formato_fecha_archivo}"


nombre_archivo_menu_diario = _obtener_nombre_archivo_fecha_externo()
archivo_platos = GestorArchivoCSV("platos")
archivo_menu   = GestorArchivoCSV(nombre_archivo_menu_diario)