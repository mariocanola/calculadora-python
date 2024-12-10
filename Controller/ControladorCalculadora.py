class ControladorCalculadora:
    def __init__(self, modelo, vista):
        """
        Inicializa el controlador con el modelo y la vista.
        """
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        """
        Ejecuta el ciclo principal de la calculadora.
        """
        self.modelo.crear_tabla()

        while True:
            self.vista.menu()
            opcion = self.vista.obtener_opcion()

            if opcion is None:
                self.vista.mostrar_mensaje("Por favor, ingrese una opción válida.")
                continue

            if opcion == 6:
                self.vista.mostrar_mensaje("Gracias por usar nuestra calculadora.")
                break

            if opcion == 5:
                historial = self.modelo.obtener_historial()
                self.vista.mostrar_historial(historial)
                continue

            try:
                a, b = self.vista.obtener_numeros()
            except ValueError as e:
                self.vista.mostrar_mensaje(f"Error en la entrada: {e}")
                continue

            try:
                resultado, operacion = self.realizar_operacion(opcion, a, b)
                if resultado is not None:
                    self.vista.mostrar_resultado(resultado)
                    self.modelo.guardar_operacion(operacion, resultado)

            except ValueError as e:
                self.vista.mostrar_mensaje(f"Error en la operación: {e}")
            except Exception as e:
                self.vista.mostrar_mensaje(f"Error inesperado: {e}")

    def realizar_operacion(self, opcion, a, b):
        match opcion:
            case 1:
                return self.modelo.sumar(a, b), f"{a} + {b}"
            case 2:
                return self.modelo.restar(a, b), f"{a} - {b}"
            case 3:
                return self.modelo.multiplicar(a, b), f"{a} * {b}"
            case 4:
                return self.modelo.dividir(a, b), f"{a} / {b}"
            case _:
                self.vista.mostrar_mensaje("Opción no válida, intente de nuevo.")
                return None, None
