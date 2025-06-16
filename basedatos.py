import sqlite3

class BaseDatos:
    def __init__(self, nombre_bd="vehiculos.db"):
        self.nombre_bd = nombre_bd
        self.conexion = None

    def conectar(self):
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.crear_tabla()
    
    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehiculos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       marca TEXT NOT NULL,
                       modelo TEXT NOT NULL,
                       anio INTEGER NOT NULL);           
        ''')
        self.conexion.commit()

    def insertar_vehiculo(self, vehiculo):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO vehiculos (marca, modelo, anio) VALUES (?, ?, ?)", (vehiculo.marca, vehiculo.modelo, vehiculo.anio))
        self.conexion.commit()
    
    def listar_vehiculos(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos")
        return cursor.fetchall()
    
    def buscar_vehiculo(self, id_vehiculo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos WHERE id= ?", (id_vehiculo,))
        return cursor.fetchone()
    
    def eliminar_vehiculo(self, id_vehiculo):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM vehiculos WHERE id = ?", (id_vehiculo,))
        self.conexion.commit()

    def cerrar(self):
        if self.conexion:
            self.conexion.close()

    def actualizar_vehiculo(self, id, nueva_marca, nuevo_modelo, nuevo_anio):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE vehiculos SET marca=?, modelo=?, anio=? WHERE id=?",(nueva_marca, nuevo_modelo, nuevo_anio))
        self.conexion.commit()


    


