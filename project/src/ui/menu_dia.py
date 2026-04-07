import sys
import os
from datetime import datetime
from src.models.plato import Plato

def _configurar_rutas_de_importacion_del_sistema():
    
    ruta_raiz_del_proyecto = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
    if ruta_raiz_del_proyecto not in sys.path:
        sys.path.append(ruta_raiz_del_proyecto)

_configurar_rutas_de_importacion_del_sistema()

class FechaMenu:

    @staticmethod                                   
    def obtener_fecha():
        return FechaMenu._obtener_fecha_formateada_externa()

    @staticmethod
    def _obtener_fecha_formateada_externa():
        
        return datetime.now().strftime("%d/%m/%Y") 

class MenuDia:

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
        self._menu_del_dia = menu_del_dia       

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
                opcion_escogida_usuario = int(input("\nEscriba el menu de su preferencia (1/2): "))
                return self._procesar_redireccion_segun_opcion(opcion_escogida_usuario)
            except ValueError:
                print("Error: Ingrese un valor numerico (1/2).")

    def _procesar_redireccion_segun_opcion(self, opcion_parametro):

        if opcion_parametro == 1:
            return self._menu_del_dia.seleccionar_opcion(False)  
        elif opcion_parametro == 2:
            return self._menu_del_dia.seleccionar_opcion(True)   
        
        print("Opcion invalida.")
        return []

class MostrarMenu:
    @staticmethod
    def mostrar_menu_del_dia(lista_de_platos_para_mostrar):
        print(f"\n","="*10 , "Menu del día para su seleccion", "=" * 10)
        if not lista_de_platos_para_mostrar:
            print("No hay platos disponibles para la selección.")
            return
            
        for numero_de_plato_iteracion, plato_objeto_instancia in enumerate(lista_de_platos_para_mostrar):
    
            MostrarMenu._imprimir_detalles_del_plato_externo(numero_de_plato_iteracion, plato_objeto_instancia)

    @staticmethod
    def _imprimir_detalles_del_plato_externo(indice_conteo, objeto_plato_externo):
    
        nombre_del_plato_extraido = objeto_plato_externo.nombre
        precio_del_plato_extraido = objeto_plato_externo.precio
        tipo_es_vegetariano_extraido = objeto_plato_externo.es_vegetariano
        
        print(f"{indice_conteo + 1}. - Nombre del plato : {nombre_del_plato_extraido} | "
            f"Precio del plato : ${precio_del_plato_extraido} | "
            f"Tipo de plato : {tipo_es_vegetariano_extraido}")