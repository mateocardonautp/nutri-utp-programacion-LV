import csv
import os
from datetime import datetime

class GestorReportesCSV:
    """
    Clase encargada de la gestión y persistencia de reportes de ventas.
    """
    def __init__(self, ruta_archivo="src/data/ventas.csv"):
        """
        Inicializa el gestor con una ruta específica.
        """
        self.ruta = ruta_archivo
        self._inicializar_archivo()

    def _inicializar_archivo(self):
        """
        Verifica la existencia del archivo y el directorio
        """
        if not os.path.exists(self.ruta):
            # Crea directorios intermedios si no existen
            os.makedirs(os.path.dirname(self.ruta), exist_ok=True)
            with open(self.ruta, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Fecha", "Estudiante", "Plato", "Monto"])

    def registrar_venta(self, estudiante, plato, monto):
        """
        Añade una nueva fila al reporte de ventas.
        """
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.ruta, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([fecha, estudiante, plato, monto])

    def leer_todas_las_ventas(self):
        """
        Recupera el historial completo de ventas.
        """
        ventas = []
        if os.path.exists(self.ruta):
            with open(self.ruta, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    ventas.append(row)
        return ventas