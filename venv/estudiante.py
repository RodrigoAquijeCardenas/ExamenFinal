import sqlite3
from datetime import datetime

def crear_insertar_datos():
    # Conexión a la base de datos
    conn = sqlite3.connect('alumnos.db')
    cur = conn.cursor()

    # Verificar si la tabla 'alumnos' está vacía
    cur.execute('SELECT COUNT(*) FROM alumnos')
    count = cur.fetchone()[0]

    if count == 0:  # Solo insertar si la tabla está vacía
        # Crear la tabla 'alumnos' si no existe
        cur.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            aprobado BOOLEAN NOT NULL,
            nota REAL NOT NULL,
            fecha TIMESTAMP NOT NULL
        )
        ''')

        # Lista de alumnos a insertar
        alumnos = [
            ('Juan', 'Pérez', True, 7.5, '2024-09-01 00:00:00'),
            ('María', 'López', False, 4.2, '2024-09-02 00:00:00'),
            ('Carlos', 'García', True, 8.9, '2024-09-03 00:00:00'),
            ('Lucía', 'Martínez', True, 9.1, '2024-09-04 00:00:00'),
            ('Sofía', 'Fernández', False, 5.0, '2024-09-05 00:00:00')
        ]

        # Insertar los registros en la tabla 'alumnos'
        cur.executemany('''
            INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha)
            VALUES (?, ?, ?, ?, ?)
        ''', alumnos)

        # Guardar los cambios y cerrar la conexión
        conn.commit()
        print("Base de datos creada y registros insertados correctamente.")
    else:
        print("La base de datos ya contiene registros.")

    # Cerrar la conexión
    conn.close()


def insertar_alumno(nombre, apellido, aprobado, nota):
    # Obtener la fecha actual
    fecha = datetime.today().strftime('%Y-%m-%d')
    
    # Conectar a la base de datos
    conn = sqlite3.connect('alumnos.db')
    cur = conn.cursor()
    
    # Insertar el alumno
    cur.execute('''
        INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, apellido, aprobado, nota, fecha))
    
    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def alumnos_desaprobados():
    conn = sqlite3.connect('alumnos.db')
    cur = conn.cursor()
    
    # Consultar alumnos desaprobados (aprobado == False)
    cur.execute('SELECT * FROM alumnos WHERE aprobado = 0')
    alumnos = cur.fetchall() 
    
    conn.close()
    
    return alumnos

def alumnos_aprobados():
    conn = sqlite3.connect('alumnos.db')
    cur = conn.cursor()
    
    # Consultar alumnos desaprobados (aprobado == False)
    cur.execute('SELECT * FROM alumnos WHERE aprobado = 1')
    alumnos = cur.fetchall() 
    
    conn.close()
    
    return alumnos