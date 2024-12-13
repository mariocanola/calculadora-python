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
            CREATE TABLE IF NOT EXISTS operacion (
                id INT AUTO_INCREMENT PRIMARY KEY,
                numero1 FLOAT,
                operador CHAR(1),
                numero2 FLOAT
            )""")
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS resultado (
                id INT AUTO_INCREMENT PRIMARY KEY,
                resultado FLOAT
            )""")
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operacion_resultado (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_operador INT,
                id_resultado INT,
                FOREIGN KEY (id_operacion) REFERENCES operacion(id),
                FOREIGN KEY (id_resultado) REFERENCES resultado(id)
            )""")
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al crear tablas: {e}")

    def agregar_operacion(self, numero1, operador, numero2):
        try:
            consulta = "INSERT INTO operacion (numero1, operador, numero2) VALUES (%s, %s, %s)"
            self.cursor.execute(consulta, (numero1, operador, numero2))
            self.conn.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Error al agregar la operación: {e}")
            return None

    def agregar_resultado(self, resultado):
        try:
            consulta = "INSERT INTO resultado (resultado) VALUES (%s)"
            self.cursor.execute(consulta, (resultado,))
            self.conn.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Error al agregar el resultado: {e}")
            return None

    def agregar_al_historial(self, id_operador, id_resultado):
        try:
            consulta = "INSERT INTO operacion_resultado (id_operador, id_resultado) VALUES (%s, %s)"
            self.cursor.execute(consulta, (id_operador, id_resultado))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al agregar al historial: {e}")

    def obtener_historial(self):
        try:
            consulta = """
            SELECT op.id, o.numero1, o.operador, o.numero2, r.resultado
            FROM operacion_resultado AS op
            JOIN operacion AS o ON op.id_operador = o.id
            JOIN resultado AS r ON op.id_resultado = r.id
            ORDER BY op.id DESC
            """
            self.cursor.execute(consulta)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al obtener el historial: {e}")
            return []
