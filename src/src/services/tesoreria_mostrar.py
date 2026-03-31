
from src.services.limpiar_pantalla import limpiar_terminal

class ReporteVisualizador:

    @staticmethod
    def mostrar_resumen(ventas):
        limpiar_terminal()
        total_dinero = 0.0
        conteo_platos = {}

        print("\n" + "╔" + "═"*45 + "╗")
        print("║       RESUMEN GENERAL DE VENTAS (CSV)       ║")
        print("╠" + "═"*45 + "╣")

        if not ventas:
            print("║       No hay ventas registradas aún.        ║")
        else:
            for venta in ventas:
                monto = float(venta['Monto'])
                plato = venta['Plato']
                total_dinero += monto
                conteo_platos[plato] = conteo_platos.get(plato, 0) + 1
            
            print(f"║ TOTAL RECAUDADO:  ${total_dinero:,.2f}")
            print(f"║ TOTAL SERVICIOS:  {len(ventas)}")
            print("╟" + "─"*45 + "╢")
            print("║ DETALLE POR PLATO:                          ║")
            for plato, cantidad in conteo_platos.items():
                print(f"║ • {plato[:25].ljust(25)} : {str(cantidad).rjust(10)} ║")

        print("╚" + "═"*45 + "╝")
        input("\nPresione ENTER para regresar...")