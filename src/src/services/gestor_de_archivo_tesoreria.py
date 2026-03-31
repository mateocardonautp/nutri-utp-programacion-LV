

import csv
import os
from datetime import datetime

class GestorReportesCSV:
    def __init__(self, ruta_archivo="src/data/ventas.csv"):
        self.ruta = ruta_archivo
        self._inicializar_archivo()

    def _inicializar_archivo(self):

        if not os.path.exists(self.ruta):
            os.makedirs(os.path.dirname(self.ruta), exist_ok=True)
            with open(self.ruta, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Fecha", "Estudiante", "Plato", "Monto"])

    def registrar_venta(self, estudiante, plato, monto):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.ruta, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([fecha, estudiante, plato, monto])

    def leer_todas_las_ventas(self):
        ventas = []
        if os.path.exists(self.ruta):
            with open(self.ruta, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    ventas.append(row)
        return ventas