from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)

# Obtener el valor de la variable de entorno o establecer un valor por defecto
elapsed_time_readiness = int(os.getenv('ELAPSED_TIME_READINESS', 60))
elapsed_time_liveness = int(os.getenv('ELAPSED_TIME_LIVENESS', 120))
elapsed_time_startup = int(os.getenv('ELAPSED_TIME', 30))

start_time = time.time()

# Endpoint para verificar la preparación del servidor
@app.route('/readiness')
def readiness():
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time < elapsed_time_readiness:  
        status_code = 500
    else:
        status_code = 200
    response = {
        "elapsed_time": elapsed_time,
        "endpoint": "/readiness",
        "status_code": status_code
    }
    print(response)
    return jsonify(response), status_code

# Endpoint para verificar la capacidad de respuesta del servidor
@app.route('/liveness')
def liveness():
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time < elapsed_time_liveness: 
        status_code = 500
    else:
        status_code = 200
    response = {
        "elapsed_time": elapsed_time,
        "endpoint": "/liveness",
        "status_code": status_code
    }
    print(response)
    return jsonify(response), status_code

# Endpoint para verificar el inicio del servidor
@app.route('/startup')
def startup():
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time < elapsed_time_startup: 
        status_code = 500
    else:
        status_code = 200
    response = {
        "elapsed_time": elapsed_time,
        "endpoint": "/startup",
        "status_code": status_code
    }
    print(response)
    return jsonify(response), status_code

# Endpoint para mostrar todo el contenido y cabeceras HTTP
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def routes():
    routes = {}
    for rule in app.url_map.iter_rules():
        routes[rule.endpoint] = [str(rule.methods)]
    return jsonify(routes), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080 )
   #app.run(host='0.0.0.0', port=5000, debug=True)