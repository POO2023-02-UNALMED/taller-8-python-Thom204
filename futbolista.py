from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "futbol", añosPracticando)
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
    
    def getNombre(self):
        super.getNombre()

    def get_golesMarcados(self):
        return self.__golesMarcados

    def set_golesMarcados(self, golesMarcados):
        self.__golesMarcados = golesMarcados

    def get_tarjetasRojas(self):
        return self.__tarjetasRojas

    def set_tarjetasRojas(self, tarjetasRojas):
        self.__tarjetasRojas = tarjetasRojas

    def get_piernaHabil(self):
        return self.__piernaHabil

    def set_piernaHabil(self, piernaHabil):
        self.__piernaHabil = piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.get_nombre()}, soy profesional en el deporte {self.get_deporte()}. Tengo {self.get_edad()} años de edad y llevo {self.get_añosPracticando()} años en el deporte"
