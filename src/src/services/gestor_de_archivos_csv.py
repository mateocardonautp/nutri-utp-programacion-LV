import csv
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) 

from src.models.plato import Plato , MostrarPlato


class GestorArchivoCSV:
    def __init__(self, nombre_del_archivo: str):
        if not nombre_del_archivo.endswith(".csv"):
            nombre_del_archivo += ".csv"
        self.nombre_del_archiv = nombre_del_archivo

    def guardar_objeto(self, objeto):

        datos = objeto.to_dict()
        archivo_existe = os.path.isfile(self.nombre_del_archiv)
        try:
            with open(self.nombre_del_archiv, mode='a', newline='', encoding='utf-8') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=datos.keys())
                if not archivo_existe:
                    escritor.writeheader()
                escritor.writerow(datos)
            print(f"Guardado: {objeto.nombre}")
        except Exception as error:
            print(f"Error al guardar: {error}")

    def leer_objetos(self):
        if not os.path.isfile(self.nombre_del_archiv):
            return []
        try:
            with open(self.nombre_del_archiv, mode='r', encoding='utf-8') as archivo:
                return list(csv.DictReader(archivo))
        except Exception as error:
            print(f"Error al leer: {error}")
            return []


class GuardarPlatos:
    def __init__(self, gestor_csv):
        self.gestor = gestor_csv

    def ejecutar_guardado(self, plato: Plato):
    
        self.gestor.guardar_objeto(plato)

class ServicioCargaPlatos:
    def __init__(self, gestor_csv):
        self.gestor = gestor_csv

    def obtener_todos_los_platos(self):
        datos_crudos = self.gestor.leer_objetos()
        objetos_plato = []
        
        for dato in datos_crudos: 
    
            nuevo_plato = Plato(
                nombre=dato["nombre"], 
                precio_base=float(dato["_precio_base"]), 
                es_vegetariano=dato["es_vegetariano"] == "True"
            )


            if dato["_ingredientes"]:
                for ingrediente in dato["_ingredientes"].split(" - "):
                    nuevo_plato.agregar_ingrediente(ingrediente)
            
            objetos_plato.append(nuevo_plato)
            
        return objetos_plato


class VisualizadorPlato:
    def visualizar_lista_platos(self, lista_platos: list):
        for plato in lista_platos:
        
            vista = MostrarPlato(plato)
            vista.descripcion_detallada()

