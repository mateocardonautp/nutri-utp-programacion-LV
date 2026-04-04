import random
import sys
import os
from datetime import datetime

# Ajuste de ruta para importaciones desde la raíz del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.ui.menu_dia import MenuDia
from src.services.gestor_de_archivos_csv import GestorArchivoCSV, ServicioCargaPlatos

class GeneradorMenuDia:
    """
    Lógica de negocio para la selección aleatoria de platos del día.
    """

    def __init__(self, archivo_plato, archivo_menu):
        """
        Inicializa el generador con los servicios de carga y gestión de archivos.
        """
        self._archivo_plato = archivo_plato
        self._gestor_dia = archivo_menu

    def generar_si_no_existe(self):
        """
        Verifica si ya existe un menú para el día de hoy. 
        """
        if self._gestor_dia.leer_objetos():
            return
        
        seleccion = self._seleccionar_platos()
        self._guardar_seleccion(seleccion)

    def _seleccionar_platos(self):
        """
        Realiza la selección aleatoria de platos.
        """
        lista_de_todos_los_platos = self._archivo_plato.obtener_todos_los_platos()
        
        platos_vegetarianos = [plato for plato in lista_de_todos_los_platos if plato.es_vegetariano is True]
        platos_estandar = [plato for plato in lista_de_todos_los_platos if plato.es_vegetariano is False]
        
        if not platos_vegetarianos and not platos_estandar:
            raise ValueError("No se pudieron cargar platos desde platos.csv")
            
        return (random.sample(platos_estandar,  min(len(platos_estandar),  3)) +
                random.sample(platos_vegetarianos, min(len(platos_vegetarianos), 1)))

    def _guardar_seleccion(self, seleccion: list):
        for plato in seleccion:
            self._gestor_dia.guardar_objeto(plato)


class FuncionalidadMenuDia:
    """
    Fachada (Facade) para la preparación del menú diario.
    """

    def __init__(self, motor_plato: GestorArchivoCSV, motor_menu: GestorArchivoCSV):
        """Inicializa la funcionalidad con los motores de persistencia necesarios."""
        self._motor_plato = motor_plato         
        self._motor_menur  = motor_menu

    def preparar_y_obtener(self):
        """
        Orquesta la generación del menú (si es necesario) y retorna un objeto MenuDia.
        """
        generador = GeneradorMenuDia(
            ServicioCargaPlatos(self._motor_plato), 
            self._motor_menur                       
        )
        
        generador.generar_si_no_existe()
        

        platos_hoy = ServicioCargaPlatos(self._motor_plato).obtener_todos_los_platos()
        return MenuDia(opciones=platos_hoy)



fecha_archivo  = f"menu_{datetime.now().strftime('%d_%m_%Y')}"
archivo_platos = GestorArchivoCSV("platos")
archivo_menu   = GestorArchivoCSV(fecha_archivo)