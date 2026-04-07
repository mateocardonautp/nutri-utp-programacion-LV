import os
import sys


def _configurar_rutas_sistema():
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_rutas_sistema()


from src.models.plato import Plato
from src.services.limpiar_pantalla import limpiar_terminal
from src.services.gestor_de_archivos_csv import GestorArchivoCSV, GuardarPlatos, ServicioCargaPlatos, VisualizadorPlato

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
        
        es_vegetariano_plato_confirmacion = self.obtener_si_es_vegetariano(es_vegetariano_plato_para_crear)

        plato_creado = self._instanciar_plato_externo(
            nombre=nombre_plato_para_crear, 
            precio=float(precio_plato_para_crear), 
            es_vegetariano=es_vegetariano_plato_confirmacion
        )

        print("\n--- Registro de Ingredientes ---")
        while True:
            ingrediente = input("- Ingrese un ingrediente (o fin para terminar): ")
            if ingrediente.lower() == 'fin':
                break
            if ingrediente.strip():
        
                plato_creado.agregar_ingrediente(ingrediente)

        self.guardar_plato(plato_creado)
        return "continuar"
    


    def _instanciar_plato_externo(self, nombre, precio, es_vegetariano):

        return Plato(
            nombre=nombre, 
            precio_base=precio, 
            es_vegetariano=es_vegetariano
        )

    def guardar_plato(self, plato_objeto):
    
        archivo = GestorArchivoCSV("platos")
        guardarPlatos = GuardarPlatos(archivo)
        guardarPlatos.ejecutar_guardado(plato_objeto)


class MostrarGuardarPlato:

    def ejecutar_interfaz_guardado_de_plato(self):
        self._ejecutar_limpieza_externa()
        actividad = GuardardadoDePlato()
        while True:
            self._encabezado_menu_acerca()
            verificador = actividad.crear_plato()
            
            if verificador == "volver_plato":
                return "volver_plato"

    def _ejecutar_limpieza_externa(self):
    
        limpiar_terminal()

    @staticmethod
    def _encabezado_menu_acerca():
        print("\n", "=" * 10, "GUARDAR PLATO", "=" * 10)


class CargadorDePlatos:

    def obtener_platos(self):
        return self._cargar_desde_archivo_externo()

    def _cargar_desde_archivo_externo(self):
        archivo = GestorArchivoCSV("platos")
        lista_de_platos_servicio = ServicioCargaPlatos(archivo)
        return lista_de_platos_servicio.obtener_todos_los_platos()


class MostrarVistaPlatos:
    def __init__(self):
        self._intentar_limpieza_externa()

    def ejecutar_interfaz_visualizar_platos(self):
        self._encabezado_visualizacion()
        cargador = CargadorDePlatos()
        lista_de_platos = cargador.obtener_platos()
        
        self._presentar_lista_externa(lista_de_platos)               
        input("\nPresione Enter para volver...")  
        return "volver_plato"

    def _intentar_limpieza_externa(self):
    
        try:
            limpiar_terminal()
        except Exception as error:
            print(f"Advertencia: {error}")

    def _presentar_lista_externa(self, lista):
        
        if not lista:
            print("\n--- No hay platos registrados ---")
            return
        presentador = VisualizadorPlato()
        presentador.visualizar_lista_platos(lista)

    @staticmethod
    def _encabezado_visualizacion():
        print("\n", "=" * 10, "CATALOGO DE PLATOS", "=" * 10)