from project.src.ui.menu_principal import MostrarMenuPrincipal

class AplicacionInicio:
    def __init__(self):
        self._interfaz = self._inicializar_interfaz_externa()

    def iniciar(self):
        self._ejecutar_interfaz(self._interfaz)


    def _inicializar_interfaz_externa(self):
        return MostrarMenuPrincipal()

    def _ejecutar_interfaz(self, interfaz):
        interfaz.ejecutar_interfaz_menu_principal()


if __name__ == "__main__":

    applicacion = AplicacionInicio()
    applicacion.iniciar()