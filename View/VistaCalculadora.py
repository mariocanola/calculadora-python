class VistaCalculadora:
    def menu(self):
        print("=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver historial")
        print("6. Salir")

    def obtener_opcion(self):
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion not in range(1, 7):
                raise ValueError("Opción fuera de rango (1-6)")
            return opcion
        except ValueError as e:
            print(f"ERROR: {e}")
            return None

    def obtener_numeros(self):
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            raise ValueError("Debe ingresar números válidos")

    def mostrar_resultado(self, resultado):
        print(f"El resultado es: {resultado}")

    '''def mostrar_historial(self, historial):
        if not historial:
            print("No hay operaciones registradas.")
        else:
            print("--- Historial ---")
            print("ID   | Primer_Numero | Operacion | Segundo_Numero | Resultado |")
            for id, numero1, operador, numero2, resultado in historial:
                print(f"ID({id}):{numero1}       |{operador}           |{numero2}          |{resultado}             |")'''

    def mostrar_historial(self, historial):
        if not historial:
            print("No hay operaciones registradas.")
        else:
            print("--- Historial ---")
            print(f"ID | Primer_Numero | Operacion | Segundo_Numero | Resultado")
            print("-" * 65)
            for id, numero1, operador, numero2, resultado in historial:
                print(f"ID({id}): {numero1} {operador} {numero2} = {resultado}")

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")
