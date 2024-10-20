from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

# Inscripción en curso
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return f"Datos recibidos: Nombre: {nombre}, Apellidos: {apellidos}, Curso: {curso}"
    return render_template('inscripcion.html')

# Registro de usuarios
@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        contrasena = request.form['contrasena']
        return f"Datos recibidos: Nombre: {nombre}, Apellidos: {apellidos}, Email: {email}"
    return render_template('registro_usuarios.html')

# Registro de productos
@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"Datos recibidos: Producto: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"
    return render_template('registro_productos.html')

# Registro de libros
@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return f"Datos recibidos: Título: {titulo}, Autor: {autor}, Medio: {medio}"
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)
