import mysql.connector 

class  ModeloCalculadora:
    def __init__(self) :
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "calculadora"
        )
        self.cursor = self.conn.cursor()

    def cerrar_conexion(self):
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS historial (
                id INT AUTO_INCREMENT PRIMARY KEY,
                operacion TEXT,
                resultado REAL
            )
        """)
        self.conn.commit()

    def guardar_operacion(self, operacion, resultado):
        consulta = "INSERT INTO historial (operacion, resultado) VALUES (%s, %s)" 
        self.cursor.execute(consulta, (operacion, resultado))
        self.conn.commit()
    
    def obtener_historial(self):
        self.cursor.execute(""" SELECT * FROM historial """)
        return self.cursor.fetchall()
    
    def validar_numeros(self, *valores):
        for valor in valores:
            if not isinstance(valor, (int, float)):
                raise TypeError(f"El valor {valor} no es un número válido.")
        
    def sumar(self, a, b):
        self.validar_numeros(a, b)
        return a + b
    
    def restar(self, a, b):
        self.validar_numeros(a, b)
        return a - b
    
    def multiplicar(self, a, b):
        self.validar_numeros(a, b)
        return a * b
    
    def dividir(self, a, b):
        self.validar_numeros(a, b)
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
    