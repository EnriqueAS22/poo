from datetime import date
from enum import Enum
from random import randint

class Sexo(Enum):
    MASCULINO = 1
    FEMENINO = 2

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
    



