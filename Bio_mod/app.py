from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def principal():
    return render_template ('index.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/servicios')
def Servicios():
    return render_template('servicios.html')

if __name__== '__main__':
    app.run(debug=True)

@app.route('/')
def principal():
    return render_template ('index.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/servicios')
def Servicios():
    return render_template('servicios.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


