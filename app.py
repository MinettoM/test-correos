from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    
    if data is None:
        return jsonify({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}), 400
    
    email = data.get('email')
    name = data.get('name')
    date = data.get('date')

    if not email or not name or not date:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    # Simplemente imprime los datos recibidos en la consola
    print('Email:', email)
    print('Name:', name)
    print('Date:', date)

    return jsonify({'message': 'Datos recibidos correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)
