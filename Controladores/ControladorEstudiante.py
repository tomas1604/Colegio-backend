from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
class ControladorEstudiante():
    def __init__(self):
        print("Creando Controlador Estudiante")
        self.repositorioEstudiante = RepositorioEstudiante()

    def crear(self, infoEstudiante):
        print("Crear un estudiante")
        estudiante = Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(estudiante)

    def mostrarEstudiante(self, id):
        print("Mostrando el estudiante con id: "+id)
        estudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return estudiante.__dict__

    def mostrarEstudiantes(self):
        print("Mostrando todos los estudiantes")
        return self.repositorioEstudiante.findAll()

    def actualizar(self,id, infoEstudiante):
        print("Actualizando el estudiante con id: "+id)
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        if infoEstudiante["cedula"] != "":
            estudianteActual.cedula = infoEstudiante["cedula"]
        if infoEstudiante["apellido"] != "":
            estudianteActual.apellido = infoEstudiante["apellido"]
        if infoEstudiante["nombre"] != "":
            estudianteActual.nombre = infoEstudiante["nombre"]
        return self.repositorioEstudiante.update(id,estudianteActual)

    def eliminar(self, id):
        print("Eliminando el estudiante con id: "+id)
        return self.repositorioEstudiante.delete(id)