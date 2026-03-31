class Plato:
    """Representa un plato del menú con sus atributos básicos."""

    def __init__(self, **kwargs):
        plato_por_defecto = Plato.default_plato()
        plato_por_defecto.update(kwargs)
    
        self._nombre = plato_por_defecto["nombre"]
        self._precio_base = plato_por_defecto["precio_base"]
        self._es_vegetariano = plato_por_defecto["es_vegetariano"]
        self._ingredientes = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):

        return self._precio_base

    @property
    def es_vegetariano(self):
    
        return self._es_vegetariano

    @property
    def ingredientes(self):
    
        return list(self._ingredientes)

    @nombre.setter
    def nombre(self, nuevo_nombre: str):

        if not nuevo_nombre or not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser un string no vacío")
        self._nombre = nuevo_nombre.strip()

    @es_vegetariano.setter
    def es_vegetariano(self, valor: bool):

        if not isinstance(valor, bool):
            raise ValueError("es_vegetariano debe ser booleano")
        self._es_vegetariano = valor


    def agregar_ingrediente(self, ingrediente: str):
    
        if not ingrediente or not isinstance(ingrediente, str):
            raise ValueError("El ingrediente debe ser un string no vacío")
        self._ingredientes.append(ingrediente.strip())

    def quitar_ingrediente(self, ingrediente: str):
        if ingrediente in self._ingredientes:
            self._ingredientes.remove(ingrediente)
            return True
        return False

    def to_dict(self):

  
        cadena_ingredientes = ""
        for numero_ingrediente, ingrediente in enumerate(self._ingredientes):
            cadena_ingredientes += ingrediente
            if numero_ingrediente < len(self._ingredientes) - 1:
                cadena_ingredientes += " - "
        
        return {
            "nombre": self._nombre,
            "_precio_base": self._precio_base,
            "es_vegetariano": self._es_vegetariano,
            "_ingredientes": cadena_ingredientes
        }

    @staticmethod
    def default_plato():
        return {
            "nombre": "Almuerzo Genérico",
            "precio_base": 10,
            "es_vegetariano": True,
        }


class MostrarPlato:

    def __init__(self, plato: Plato):
        self._plato = plato  

    def descripcion_detallada(self):
    
        self._encabezado()
        self._informacion()
        self._ingredientes()
        self._pie()

    def _encabezado(self):
        print("\n", "=" * 15, "Descripción Del Plato", "=" * 15)

    def _informacion(self):
    
        print(f"\n- Nombre del plato : {self._plato.nombre}")
        print(f"- Precio base del plato    : ${self._plato.precio}")
        
        tipo_de_plato = "Sí es vegetariano" if self._plato.es_vegetariano else "No es vegetariano"
        print(f"- Es vegetariano   : {tipo_de_plato}")

    def _ingredientes(self):
        print("\nIngredientes del plato:")
    
        ingredientes = self._plato.ingredientes
        
        if not ingredientes:
            print("- No hay ingredientes registrados.")
        else:
            for ingrediente in ingredientes:
                print(f"  - {ingrediente}")

    def _pie(self):
        print("=" * 49)

