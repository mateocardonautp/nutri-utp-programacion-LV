class Comensal:
    """
    Representa a un estudiante que hace uso del servicio de comedor.
    """
    def __init__(self, **kwargs):
        """
        Inicializa un Comensal con valores por defecto si no se proporcionan.
        """
        default_comensal_estudiante = {
            "id_estudiante": "0000",
            "tipo_subsidio": "None",
        }
        default_comensal_estudiante.update(kwargs)
        self.id_estudiante  = default_comensal_estudiante["id_estudiante"]
        self._tipo_subsidio = default_comensal_estudiante["tipo_subsidio"]

    @property
    def tipo_subsidio(self):
        """Retorna el tipo de subsidio asignado al comensal."""
        return self._tipo_subsidio

    @tipo_subsidio.setter
    def tipo_subsidio(self, valor: str):
        """
        Valida que el subsidio asignado pertenezca a las categorías oficiales.
        """
        subsidios_validos = {"Subsidio", "Subsidio parcial", "Subsidio semi parcial", "None"}
        if valor not in subsidios_validos:
            raise ValueError(f"Subsidio inválido: {valor}")
        self._tipo_subsidio = valor


class CalcularPrecioComensal:
    """
    Motor de cálculo para determinar el costo final de un plato según el perfil del comensal.
    """
    def __init__(self, comensal: Comensal):
    
        self._comensal = comensal             

    @property
    def comensal(self):                       
    
        return self._comensal

    def calcular_descuento(self, valor_plato: float):
        return self._operacion_matematica_subsidio(valor_plato)

    def _operacion_matematica_subsidio(self, valor_base: float):
        politica_descuentos = {
            "Subsidio"             : 1.0,
            "Subsidio parcial"     : 0.5,
            "Subsidio semi parcial": 0.25,
            "None"                 : 0.0,
        }
        porcentaje_del_subsidio = politica_descuentos.get(self._comensal.tipo_subsidio, 0.0)
        return valor_base * porcentaje_del_subsidio

    def obtener_precio_final(self, valor_plato: float):
        descuento = self.calcular_descuento(valor_plato)
        return valor_plato - descuento


class MostrarComensal:
    """
    Encargada de la representación visual de los datos del comensal en consola.
    """
    def __init__(self, comensal: Comensal):
    
        self._comensal = comensal             

    def descripcion_detallada_comensal(self):
        
        self._encabezado_descripcion_detallada_comensal()
        self._informacion_del_comensal()

    @staticmethod                            
    def _encabezado_descripcion_detallada_comensal():

        print("\n", "=" * 15, "Descripción Del Comensal", "=" * 15)

    def _informacion_del_comensal(self):
        print(f"- Id del comensal  : {self._comensal.id_estudiante}")
        print(f"- Tipo de subsidio : {self._comensal.tipo_subsidio}")
        print("\n")