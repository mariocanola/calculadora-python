class VistaCalculadora:
    def menu(self):
        print("\n=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver Historial")
        print("6. Salir")

    def obtener_opcion(self):
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion not in range(1, 7):
                raise ValueError("La opción debe estar entre 1 y 6.")
            return opcion
        except ValueError as e:
            print(f"ERROR: {e}")
            return None

    def obtener_numeros(self):
        while True:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                return a, b
            except ValueError:
                print("Por favor, ingrese números válidos.")

    def mostrar_resultado(self, resultado):
        print(f"\nEl resultado es: {resultado}")

    def mostrar_historial(self, historial):
        if not historial:
            print("\nNo hay operaciones registradas en el historial.")
            return

        print("\n--- Historial de Operaciones ---")
        print(f"{'ID':<5} {'Operación':<20} {'Resultado':<10}")
        print("-" * 40)
        for id, operacion, resultado in historial:
            print(f"{id:<5} {operacion:<20} {resultado:<10}")

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")