from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Repositorios.RepositorioMateria import RepositorioMateria
from Modelos.Departamento import Departamento
from Modelos.Materia import Materia

class ControladorMateria():
    def __init__(self):
        print("Creando Controlador Materia")
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def crear(self, infoMateria):
        print("Crear una materia")
        materia = Materia(infoMateria)
        return self.repositorioMateria.save(materia)

    def mostrarMateria(self, id):
        print("Mostrando la materia con id: " + id)
        materia = Materia(self.repositorioMateria.findById(id))
        return materia.__dict__

    def mostrarMaterias(self):
        print("Mostrando todos las materias")
        return self.repositorioMateria.findAll()

    def actualizar(self, id, infoMateria):
        print("Actualizando la Materia con id: " + id)
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.update(id, materiaActual)

    def eliminar(self, id):
        print("Eliminando la materia con id: " + id)
        return self.repositorioMateria.delete(id)

    #Relación Materia y Departamento
    def asignarDepartamento(self,id, id_departamento):
        materia = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materia.departamento = departamentoActual
        return self.repositorioMateria.save(materia)

