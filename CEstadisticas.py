
class Estadisticas:
    def __init__(self):
        self.partidas_jugadas: int = 0
        self.partidas_perdidas: int = 0
        self.partidas_ganadas: int = 0
        self.intentos_promedio: float = 0.0
        self.partidas_ganadas_un_intento: int = 0

    def promedio(self) -> tuple:
        promedio_aciertos = self.partidas_ganadas/self.partidas_jugadas
        promedio_perdidas = 1 - promedio_aciertos
        promedios: tuple = (promedio_aciertos, promedio_perdidas)
        return promedios
