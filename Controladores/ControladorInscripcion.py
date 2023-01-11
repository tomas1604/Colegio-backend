from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Repositorios.RepositorioInscripcion import RepositorioInscripcion

from Modelos.Materia import Materia
from Modelos.Estudiante import Estudiante
from Modelos.Inscripcion import Inscripcion

class ControladorInscripcion():
    def __init__(self):
        print("Crear controlador inscripcion")
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioMateria = RepositorioMateria()
        self.repositorioInscripcion = RepositorioInscripcion()

    def crear(self, infoInscripcion, id_estudiante, id_materia):
        inscripcion = Inscripcion(infoInscripcion)
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = materia
        return self.repositorioInscripcion.save(inscripcion)

    def mostrarInscripcion(self, id):
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return inscripcion.__dict__

    def mostrarInscripciones(self):
        return self.repositorioInscripcion.findAll()

    def actualizar(self, id, infoInscripcion, id_estudiante, id_materia):
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcion.año = infoInscripcion['año']
        inscripcion.semestre = infoInscripcion['semestre']
        inscripcion.nota_final = infoInscripcion['nota_final']
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = materia
        return self.repositorioInscripcion.save(inscripcion)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)

    def listadoInscritosMateria(self,id_materia):
        return self.repositorioInscripcion.getListadoInscritosEnMateria(id_materia)

    def notaMayor(self):
        return self.repositorioInscripcion.getMayorNotaPorCurso()

    def promedioMateria(self, id_materia):
        return self.repositorioInscripcion.getPromedioNotasEnMateria(id_materia)
