from datetime import date
from enum import Enum
from random import randint

class Sexo(Enum):
    MASCULINO = 1
    FEMENINO = 2

class Carnet(Enum):
    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    C = 5 
    D = 6
    E = 7

class Cargo(Enum):
    ADMINISTRATIVO = 1
    PROFESOR = 2
    DIRECTOR = 3


class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.fecha_nacimiento = date.today()
        self.sexo = Sexo(randint(1, 2))
        self.dni = ""

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"
    
    def edad(self):
        return date.today() - self.fecha_nacimiento
    
    def presentarme(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad()} años"
    
    # Te transforma el objeto en cadena
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre_completo()}"
    
    def __repr__(self):
        return.self.__str__()
    

class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.fecha_matriculacion = None
        self.carnets = []
    
    def matricularse(self, carnet: Carnet):
        self.fecha_matriculacion = date.today()
        self.carnets.append(carnet)

    def nombre_completo(self):
        nombre = super().nombre_completo()
        if self.sexo == Sexo.FEMENINO:
            return f"Dña {nombre}"
        else: 
            return f"D {nombre}"


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.fecha_antiguedad = None
        self.cargo = None
        self.sueldo_base = 0
        
    def contratar(self, cargo: Cargo, sueldo: float):
        self.cargo = cargo
        self.sueldo_base = sueldo
        self.fecha_antiguedad = date.today()

    def despedir(self):
        return "Pendiente de contruir"
        

