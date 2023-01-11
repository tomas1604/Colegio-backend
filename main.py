from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorInscripcion import ControladorInscripcion



app = Flask(__name__)
cors = CORS(app)

miControladorEstudiante = ControladorEstudiante()
miControladorDepartamento = ControladorDepartamento()
miControladorMateria = ControladorMateria()
miControladorInscripcion = ControladorInscripcion()

@app.route("/",methods=['GET'])
def test():
    json={}
    json['mensaje'] = "Servidor corriendo correctamente..."
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def CrearEstudiante():
    datos = request.get_json()
    respuesta = miControladorEstudiante.crear(datos)
    return jsonify(respuesta)

@app.route("/estudiantes",methods=['GET'])
def ObtenerEstudiantes():
    respuesta = miControladorEstudiante.mostrarEstudiantes()
    return jsonify(respuesta)

@app.route("/estudiantes/<string:id>", methods=['GET'])
def ObtenerEstudiante(id):
    respuesta = miControladorEstudiante.mostrarEstudiante(id)
    return jsonify(respuesta)

@app.route("/estudiantes/<string:id>", methods=['PUT'])
def ActualizarEstudiante(id):
    datos = request.get_json()
    respuesta = miControladorEstudiante.actualizar(id,datos)
    return jsonify(respuesta)

@app.route("/estudiantes/<string:id>", methods = ['DELETE'])
def EliminarEstudiante(id):
    respuesta = miControladorEstudiante.eliminar(id)
    return jsonify(respuesta)

#OPERACIONES CRUD CONTROLADOR DEPARTAMENTO
@app.route("/departamentos",methods=['POST'])
def CrearDepartamento():
    datos = request.get_json()
    respuesta = miControladorDepartamento.crear(datos)
    return jsonify(respuesta)

@app.route("/departamentos",methods=['GET'])
def ObtenerDepartamentos():
    respuesta = miControladorDepartamento.mostrarDepartamentos()
    return jsonify(respuesta)

@app.route("/departamentos/<string:id>", methods=['GET'])
def ObtenerDepartamento(id):
    respuesta = miControladorDepartamento.mostrarDepartamento(id)
    return jsonify(respuesta)

@app.route("/departamentos/<string:id>", methods=['PUT'])
def ActualizarDepartamento(id):
    datos = request.get_json()
    respuesta = miControladorDepartamento.actualizar(id,datos)
    return jsonify(respuesta)

@app.route("/departamentos/<string:id>", methods = ['DELETE'])
def EliminarDepartamento(id):
    respuesta = miControladorDepartamento.eliminar(id)
    return jsonify(respuesta)

#OPERACIONES CRUD CONTROLADOR MATERIA
@app.route("/materias",methods=['POST'])
def CrearMateria():
    datos = request.get_json()
    respuesta = miControladorMateria.crear(datos)
    return jsonify(respuesta)

@app.route("/materias",methods=['GET'])
def ObtenerMaterias():
    respuesta = miControladorMateria.mostrarMaterias()
    return jsonify(respuesta)

@app.route("/materias/<string:id>", methods=['GET'])
def ObtenerMateria(id):
    respuesta = miControladorMateria.mostrarMateria(id)
    return jsonify(respuesta)

@app.route("/materias/<string:id>", methods=['PUT'])
def ActualizarMateria(id):
    datos = request.get_json()
    respuesta = miControladorMateria.actualizar(id,datos)
    return jsonify(respuesta)

@app.route("/materias/<string:id>", methods = ['DELETE'])
def EliminarMateria(id):
    respuesta = miControladorMateria.eliminar(id)
    return jsonify(respuesta)

@app.route("/materias/<string:id>/departamentos/<string:id_departamento>",methods=['PUT'])
def asignarDepartamento(id, id_departamento):
    respuesta = miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(respuesta)

#OPERACIONES CRUD INSCRIPCIONES

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods =['POST'])
def crearInscripcion(id_estudiante, id_materia):
    datos = request.get_json()
    respuesta = miControladorInscripcion.crear(datos, id_estudiante, id_materia)
    return jsonify(respuesta)

@app.route("/inscripciones/<string:id>",methods =['GET'])
def consultarInscripcion(id):
    respuesta = miControladorInscripcion.mostrarInscripcion(id)
    return jsonify(respuesta)

@app.route("/inscripciones", methods = ['GET'])
def consultarInscripciones():
    respuesta = miControladorInscripcion.mostrarInscripciones()
    return jsonify(respuesta)

@app.route("/inscripciones/<string:id>/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods =['PUT'])
def actualizarInscripcion(id, id_estudiante, id_materia):
    datos = request.get_json()
    respuesta = miControladorInscripcion.actualizar(id,datos,id_estudiante, id_materia)
    return jsonify(respuesta)

@app.route("/inscripciones/<string:id>", methods = ['DELETE'])
def eliminarInscripcion(id):
    respuesta = miControladorInscripcion.delete(id)
    return jsonify(respuesta)

@app.route("/inscripciones/materia/<string:id_materia>", methods = ['GET'])
def inscritosMateria (id_materia):
    respuesta = miControladorInscripcion.listadoInscritosMateria(id_materia)
    return jsonify(respuesta)

@app.route("/inscripciones/notaMayor", methods =['GET'])
def notasMayores():
    respuesta = miControladorInscripcion.notaMayor()
    return jsonify(respuesta)

@app.route("/inscripciones/promedio/materia/<string:id_materia>", methods =['GET'])
def promedioMateria(id_materia):
    respuesta = miControladorInscripcion.promedioMateria(id_materia)
    return jsonify(respuesta)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: "+dataConfig['url-backend']+" puerto "+str(dataConfig['port']))
    serve(app, host = dataConfig['url-backend'], port = dataConfig['port'])
