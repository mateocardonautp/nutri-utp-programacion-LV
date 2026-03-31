import sys

import os

from datetime import datetime
from src.models.plato import Plato



sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) 
class FechaMenu:
    @staticmethod                                   
    def obtener_fecha():
        return datetime.now().strftime("%d/%m/%Y") 

class MenuDia:
    """ 
    Representa la oferta gastronómica del día actual.
    """
    def __init__(self, **kwargs):
        default_menu = {
            "fecha": FechaMenu.obtener_fecha(),
            "opciones": []
        }
        default_menu.update(kwargs)
        self.fecha = default_menu["fecha"]
        self._opciones = default_menu["opciones"]

    @property
    def opciones_del_menu(self):
        return list(self._opciones)

    def agregar_nuevo_plato(self, plato: Plato):
    
        self._opciones.append(plato)

    def seleccionar_opcion(self, tipo_preferencia: bool):
        return self._aislar_seleccion(tipo_preferencia)

    def _aislar_seleccion(self, criterio_es_vegetariano: bool):
        return [plato for plato in self._opciones if plato.es_vegetariano == criterio_es_vegetariano]

class GestionarMenu:
    def __init__(self, menu_del_dia: MenuDia):                 
        self._menu_del_dia = menu_del_dia

    def agregar_plato(self, plato: Plato):

        self._menu_del_dia.agregar_nuevo_plato(plato)

class SeleccionarMenuDelDia:
    def __init__(self, menu_del_dia: MenuDia):
        self.menu_del_dia = menu_del_dia

    def ejecutar_interfaz_seleccion(self):
        self._encabezado_menu_del_dia_seleccion_tipo()
        self._opciones_de_tipo_menu_del_dia()
        return self.verificar_opcion()

    def _encabezado_menu_del_dia_seleccion_tipo(self):
         print("\n", "=" * 10, "Selección Tipo de Plato", "=" * 10)

    def _opciones_de_tipo_menu_del_dia(self):
        print("1. Menu estándar")
        print("2. Menu vegetariano")

    def verificar_opcion(self):
        while True:
            try:
                opcion = int(input("\nEscriba el menu de su preferencia (1/2): "))
                if opcion == 1:
                    return self.menu_del_dia.seleccionar_opcion(False)
                elif opcion == 2:
                    return self.menu_del_dia.seleccionar_opcion(True)
                print("Opcion invalida.")
            except ValueError:
                print("Error: Ingrese un valor numerico (1/2).")

class MostrarMenu:
    @staticmethod
    def mostrar_menu_del_dia(lista_de_platos):
        print(f"\n","="*10 , "Menu del día para su selección", "=" * 10)
        if not lista_de_platos:
            print("No hay platos disponibles para la selección.")
        for numero_de_plato, plato in enumerate(lista_de_platos):
            print(f"{numero_de_plato + 1}. - Nombre del plato : {plato.nombre} | Precio del plato : ${plato.precio} | Tipo de plato : {plato.es_vegetariano}")
