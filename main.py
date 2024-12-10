from Model.ModeloCalculadora import ModeloCalculadora
from View.VistaCalculadora import VistaCalculadora
from Controller.ControladorCalculadora import ControladorCalculadora

def main(): # funcion que inicializa el programa 
    try:
        vista_calculadora = VistaCalculadora()
        modelo_calculadora = ModeloCalculadora()
        controlador_calculadora = ControladorCalculadora(modelo_calculadora, vista_calculadora)
        
        controlador_calculadora.ejecutar()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido. ¡Hasta luego!")
    except Exception as e:
        print(f"ERROR inesperado: {e}")

if __name__ == "__main__":
    main()
