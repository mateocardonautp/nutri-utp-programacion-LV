class Comensal:
  
    def __init__(self, **kwargs):
      
        configuracion_por_defecto_del_comensal_estudiante = {
            "id_estudiante": "0000",
            "tipo_subsidio": "None",
        }
        configuracion_por_defecto_del_comensal_estudiante.update(kwargs)
        
        self.id_estudiante = configuracion_por_defecto_del_comensal_estudiante["id_estudiante"]
        self._tipo_subsidio = configuracion_por_defecto_del_comensal_estudiante["tipo_subsidio"]

    @property
    def tipo_subsidio(self):
    
        return self._tipo_subsidio

    @tipo_subsidio.setter
    def tipo_subsidio(self, valor_del_subsidio_parametro: str):
      
        if not self._verificar_validez_del_subsidio_externo(valor_del_subsidio_parametro):
            raise ValueError(f"Subsidio inválido detectado: {valor_del_subsidio_parametro}")
        self._tipo_subsidio = valor_del_subsidio_parametro

    def _verificar_validez_del_subsidio_externo(self, cadena_de_subsidio_a_validar):
    
        conjunto_de_subsidios_validos_oficiales = {
            "Subsidio", 
            "Subsidio parcial", 
            "Subsidio semi parcial", 
            "None"
        }
        return cadena_de_subsidio_a_validar in conjunto_de_subsidios_validos_oficiales


class CalcularPrecioComensal:

    def __init__(self, objeto_comensal_instanciado: Comensal):
        self._comensal_asignado_al_calculo = objeto_comensal_instanciado             

    @property
    def comensal(self):                       
        return self._comensal_asignado_al_calculo

    def calcular_descuento(self, monto_valor_del_plato_base: float):
    
        return self._ejecutar_operacion_matematica_de_subsidio_privada(monto_valor_del_plato_base)

    def _ejecutar_operacion_matematica_de_subsidio_privada(self, monto_base_para_calculo: float):
    
        tabla_de_politica_de_descuentos_oficial = {
            "Subsidio"             : 1.0,
            "Subsidio parcial"     : 0.5,
            "Subsidio semi parcial": 0.25,
            "None"                 : 0.0,
        }
        
        tipo_de_subsidio_del_estudiante = self._comensal_asignado_al_calculo.tipo_subsidio
        porcentaje_de_descuento_aplicable = tabla_de_politica_de_descuentos_oficial.get(
            tipo_de_subsidio_del_estudiante, 0.0
        )
        
        return monto_base_para_calculo * porcentaje_de_descuento_aplicable

    def obtener_precio_final(self, monto_valor_del_plato_inicial: float):

        monto_del_descuento_calculado = self.calcular_descuento(monto_valor_del_plato_inicial)
        return monto_valor_del_plato_inicial - monto_del_descuento_calculado


class MostrarComensal:

    def __init__(self, objeto_comensal_para_visualizar: Comensal):
        self._comensal_visualizado = objeto_comensal_para_visualizar             

    def descripcion_detallada_comensal(self):
    
        self._imprimir_encabezado_de_descripcion_detallada_privado()
        self._imprimir_lineas_de_informacion_del_comensal_privado()

    @staticmethod                            
    def _imprimir_encabezado_de_descripcion_detallada_privado():
        print("\n", "=" * 15, "Descripción Del Comensal", "=" * 15)

    def _imprimir_lineas_de_informacion_del_comensal_privado(self):
    
        id_del_estudiante_extraida = self._comensal_visualizado.id_estudiante
        tipo_de_subsidio_extraido = self._comensal_visualizado.tipo_subsidio
        
        print(f"- Id del comensal  : {id_del_estudiante_extraida}")
        print(f"- Tipo de subsidio : {tipo_de_subsidio_extraido}")
        print("\n")