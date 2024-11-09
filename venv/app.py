from flask import Flask, render_template, request, redirect, url_for
import estudiante
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    estudiante.crear_insertar_datos()

    
    conn = sqlite3.connect('alumnos.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM alumnos')
    alumnos = cur.fetchall() 
    conn.close()
    
   
    return render_template('listar_alumnos.html', alumnos=alumnos)

@app.route('/listar_alumnos')
def listar_alumnos():
    conn = sqlite3.connect('alumnos.db')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM alumnos')
    alumnos = cur.fetchall() 
    

    conn.close()
    
    return render_template('listar_alumnos.html', alumnos=alumnos)


@app.route('/insertar_alumno', methods=['GET', 'POST'])
def insertar_alumno():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = request.form['aprobado']
        nota = request.form['nota']
        
        estudiante.insertar_alumno(nombre, apellido, aprobado, nota)
        
        return redirect(url_for('index'))

    return render_template('insertar_alumno.html')

@app.route('/alumnos_desaprobados')
def alumnos_desaprobados_view():
    alumnos = estudiante.alumnos_desaprobados()
    return render_template('alumnos_desaprobados.html', alumnos=alumnos)


@app.route('/alumnos_aprobados')
def alumnos_aprobados_view():
    alumnos = estudiante.alumnos_aprobados()
    return render_template('alumnos_aprobados.html', alumnos=alumnos)


if __name__ == '__main__':
    app.run(debug=True)
