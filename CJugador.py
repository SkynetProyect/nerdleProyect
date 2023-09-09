from CEstadisticas import Estadisticas


class Jugador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estadisticas: Estadisticas = Estadisticas()
