import csv
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) 
from src.models.plato import Plato, MostrarPlato
from src.services.limpiar_pantalla import limpiar_terminal
from src.services.gestor_de_archivos_csv import GestorArchivoCSV, GuardarPlatos , ServicioCargaPlatos , VisualizadorPlato

class GuardardadoDePlato:

    @staticmethod
    def obtener_si_es_vegetariano(entrada):
        if entrada.lower() == "s":
            return True
        return False
        
    def crear_plato(self):
   
        nombre_plato_para_crear = input("- Ingrese el nombre del plato (o salir para volver): ")
        if nombre_plato_para_crear.lower() == "salir":
            return "volver_plato"

        precio_plato_para_crear = input("- Ingrese el precio base del plato: ")
        es_vegetariano_plato_para_crear = input("- ¿Es vegetariano? (s/n): ")
        
        es_vegetariano_plato_confirmacion = GuardardadoDePlato.obtener_si_es_vegetariano(es_vegetariano_plato_para_crear)

        plato_creado = Plato(
            nombre=nombre_plato_para_crear, 
            precio_base=float(precio_plato_para_crear), 
            es_vegetariano=es_vegetariano_plato_confirmacion
        )


        print("\n--- Registro de Ingredientes ---")
        while True:
            ingrediente = input("- Ingrese un ingrediente (o 'fin' para terminar): ")
            if ingrediente.lower() == 'fin':
                break
            if ingrediente.strip():
                plato_creado.agregar_ingrediente(ingrediente)

        self.guardar_plato(plato_creado)
        return "continuar"
    
    def guardar_plato(self, plato: Plato):
        archivo = GestorArchivoCSV("platos")
        guardarPlatos = GuardarPlatos(archivo)
        guardarPlatos.ejecutar_guardado(plato)

class MostrarGuardarPlato:
    def __init__(self):
        try:
            limpiar_terminal()
        except:
            pass
        
    def ejecutar_interfaz_guardado_de_plato(self):
        actividad = GuardardadoDePlato()
        while True:
            self._encabezado_menu_acerca()
            verificador = actividad.crear_plato()
            
    
            if verificador == "volver_plato":
                return "volver_plato"

    def _encabezado_menu_acerca(self):
        print("\n", "=" * 10, "GUARDAR PLATO", "=" * 10)


class CargadorDePlatos:                          
    def obtener_platos(self):
        archivo = GestorArchivoCSV("platos")
        lista_de_platos = ServicioCargaPlatos(archivo)
        return lista_de_platos.obtener_todos_los_platos()


class MostrarVistaPlatos:
    def __init__(self):
        try:
            limpiar_terminal()
        except Exception as error:
            print(f"Advertencia: {error}")

    def ejecutar_interfaz_visualizar_platos(self):
        self._encabezado_visualizacion()
        cargador = CargadorDePlatos()
        lista_de_platos    = cargador.obtener_platos()
        self._mostrar_lista(lista_de_platos)               
        input("\nPresione Enter para volver...")  
        return "volver_plato"

    @staticmethod
    def _encabezado_visualizacion():
        print("\n", "=" * 10, "CATALOGO DE PLATOS", "=" * 10)

    @staticmethod
    def _mostrar_lista(lista: list):
        if not lista:
            print("\n--- No hay platos registrados ---")
            return
        presentador = VisualizadorPlato()
        presentador.visualizar_lista_platos(lista)