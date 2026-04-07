import csv
import os
from datetime import datetime

class GestorReportesCSV:
    
    def __init__(self, ruta_archivo_configurada="src/data/ventas.csv"):
    
        self.ruta_del_archivo_de_ventas = ruta_archivo_configurada
        self._verificar_y_preparar_entorno_de_persistencia_externo()

    def registrar_venta(self, nombre_del_estudiante_parametro, nombre_del_plato_parametro, monto_total_de_venta):
    
        fecha_y_hora_del_registro_actual = self._obtener_fecha_y_hora_formateada_externa()
        
        datos_de_la_venta_para_guardar = [
            fecha_y_hora_del_registro_actual, 
            nombre_del_estudiante_parametro, 
            nombre_del_plato_parametro, 
            monto_total_de_venta
        ]
        
        self._escribir_linea_en_archivo_csv_externo(datos_de_la_venta_para_guardar)

    def leer_todas_las_ventas(self):
       
        if not self._verificar_existencia_del_archivo_fisico_externo():
            return []
            
        return self._leer_datos_estructurados_del_csv_externo()

  

    def _verificar_y_preparar_entorno_de_persistencia_externo(self):
      
        if not os.path.exists(self.ruta_del_archivo_de_ventas):
           
            nombre_del_directorio_padre = os.path.dirname(self.ruta_del_archivo_de_ventas)
            os.makedirs(nombre_del_directorio_padre, exist_ok=True)
            
           
            lista_de_encabezados_del_reporte = ["Fecha", "Estudiante", "Plato", "Monto"]
            self._crear_archivo_con_encabezados_externo(lista_de_encabezados_del_reporte)

    def _crear_archivo_con_encabezados_externo(self, lista_de_columnas_parametro):
       
        with open(self.ruta_del_archivo_de_ventas, mode='w', newline='', encoding='utf-8') as archivo_de_escritura_inicial:
            escritor_de_datos_csv = csv.writer(archivo_de_escritura_inicial)
            escritor_de_datos_csv.writerow(lista_de_columnas_parametro)

    def _obtener_fecha_y_hora_formateada_externa(self):
      
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _escribir_linea_en_archivo_csv_externo(self, lista_de_datos_de_la_fila):
     
        with open(self.ruta_del_archivo_de_ventas, mode='a', newline='', encoding='utf-8') as archivo_de_ventas_existente:
            escritor_de_datos_csv = csv.writer(archivo_de_ventas_existente)
            escritor_de_datos_csv.writerow(lista_de_datos_de_la_fila)

    def _verificar_existencia_del_archivo_fisico_externo(self):
    
        return os.path.exists(self.ruta_del_archivo_de_ventas)

    def _leer_datos_estructurados_del_csv_externo(self):
       
        lista_de_ventas_acumuladas = []
        with open(self.ruta_del_archivo_de_ventas, mode='r', encoding='utf-8') as archivo_de_lectura_de_datos:
            lector_de_diccionarios_csv = csv.DictReader(archivo_de_lectura_de_datos)
            for fila_de_datos_extraida in lector_de_diccionarios_csv:
                lista_de_ventas_acumuladas.append(fila_de_datos_extraida)
        return lista_de_ventas_acumuladas