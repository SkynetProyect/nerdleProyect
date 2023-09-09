from CJugador import Jugador


class Instrucciones:
    def __init__(self):
        self.instrucciones: str = ""

    def instrucciones(self) -> str:
        return self.instrucciones


class Sistema:
    def __init__(self):
        self.juego_nuevo = False
        self.jugador = None
        self.instrucciones: Instrucciones = Instrucciones()

    def registrar_jugador(self, nombre_jugador: str):
        self.jugador = Jugador(nombre_jugador)

    def inicar_juego(self):
        pass

    def anunciar_resultado(self):
        pass

