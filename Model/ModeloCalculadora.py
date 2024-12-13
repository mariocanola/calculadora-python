import mysql.connector

class ModeloCalculadora:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="calculadora"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error de conexión a la base de datos: {e}")

    def crear_tablas(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operadores (
                id_operador INT AUTO_INCREMENT PRIMARY KEY,
                simbolo VARCHAR(5) NOT NULL
            )""")
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operaciones (
                id_operacion INT AUTO_INCREMENT PRIMARY KEY,
                op1 INT NOT NULL,
                op2 INT NOT NULL,
                id_operador INT NOT NULL,
                resultado INT NOT NULL,
                FOREIGN KEY (id_operador) REFERENCES operadores(id_operador)
            )""")
            
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al crear tablas: {e}")

    def agregar_operacion(self, op1, id_operador, op2, resultado):
        try:
            consulta = "INSERT INTO operaciones (op1, id_operador, op2, resultado) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(consulta, (op1, id_operador, op2, resultado))
            self.conn.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Error al agregar la operación: {e}")
            return None #aqui debemos corregir 

    def agregar_resultado(self, operaciones):
        try:
            consulta = "INSERT INTO operaciones (op1, id_operador, op2, resultado) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(consulta, (operaciones,))
            self.conn.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Error al agregar el resultado: {e}")
            return None #posiblemente esto esta haciendo lo mismo que la funcion anterior agregar_operacion

    def agregar_al_historial(self, op1, id_operador, op2, resultado):
        try:
            consulta = "INSERT INTO operaciones (op1 ,id_operador, op2, resultado) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(consulta, (op1, id_operador, op2, resultado))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al agregar al historial: {e}")

    def obtener_historial(self):
        try:
            consulta = """
            SELECT op.id_operacion, op.op1, or.id_operador, op.op2, op.resultado
            FROM operaciones AS op
            JOIN operadores AS or ON or.id_operador = op.id_operador
            ORDER BY op.id_operador DESC
            """
            self.cursor.execute(consulta)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al obtener el historial: {e}")
            return []
