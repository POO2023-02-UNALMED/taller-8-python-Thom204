class Deportista:
    def __init__(self, deporte="Futbol", añosPracticando=0):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando

    def get_deporte(self):
        return self.__deporte

    def set_deporte(self, deporte):
        self.__deporte = deporte

    def get_añosPracticando(self):
        return self.__añosPracticando

    def set_añosPracticando(self, añosPracticando):
        self.__añosPracticando = añosPracticando