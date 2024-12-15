import tkinter as tk
import random

# Alvarez_David_Tarea_03

# Crear una aplicación móvil en Android donde el usuario juegue al clásico juego de Piedra, Papel o Tijera contra la computadora.
# El jugador debe seleccionar una opción y la aplicación seleccionará aleatoriamente una de las tres opciones para competir. 
# Al final, el juego mostrará el resultado (si el jugador ganó, perdió o hubo empate).

class Juego:
    """Clase que contiene la lógica del juego Piedra, Papel o Tijera."""
    def __init__(self):
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        self.opciones = ["Piedra", "Papel", "Tijera"]

    def obtener_eleccion_computadora(self):
        """Genera una elección aleatoria para la computadora."""
        return random.choice(self.opciones)

    def determinar_resultado(self, jugador, computadora):
        """
        Determina el resultado del juego.
        :param jugador: Elección del jugador.
        :param computadora: Elección de la computadora.
        :return: Resultado del juego: 'Ganaste', 'Perdiste', 'Empate'.
        """
        if jugador == computadora:
            return "Empate"
        elif (jugador == "Piedra" and computadora == "Tijera") or \
             (jugador == "Tijera" and computadora == "Papel") or \
             (jugador == "Papel" and computadora == "Piedra"):
            self.puntaje_jugador += 1
            return "Ganaste"
        else:
            self.puntaje_computadora += 1
            return "Perdiste"


class Interfaz(Juego):
    """Clase que contiene la interfaz gráfica del juego y hereda de la lógica."""
    def __init__(self, raiz):
        super().__init__()  # Inicializa la lógica del juego desde la clase padre
        self.raiz = raiz
        self.raiz.title("Piedra, Papel o Tijera")
        self.raiz.geometry("400x400")

        # Widgets
        self.texto_resultado = tk.Label(raiz, text="¡Elige tu opción!", font=("Arial", 14))
        self.texto_resultado.pack(pady=20)

        self.texto_computadora = tk.Label(raiz, text="Computadora eligió: ", font=("Arial", 12))
        self.texto_computadora.pack(pady=10)

        self.puntaje = tk.Label(
            raiz,
            text=f"Jugador: {self.puntaje_jugador} | Computadora: {self.puntaje_computadora}",
            font=("Arial", 12)
        )
        self.puntaje.pack(pady=10)

        # Botones para las opciones
        self.botones_frame = tk.Frame(raiz)
        self.botones_frame.pack(pady=20)
        self.crear_botones()

    def crear_botones(self):
        """Crea los botones de Piedra, Papel y Tijera."""
        for opcion in self.opciones:
            boton = tk.Button(
                self.botones_frame,
                text=opcion,
                width=10,
                height=2,
                command=lambda eleccion=opcion: self.jugar(eleccion)
            )
            boton.pack(side=tk.LEFT, padx=10)

    def jugar(self, eleccion_jugador):
        """Maneja la interacción del jugador al elegir una opción."""
        eleccion_computadora = self.obtener_eleccion_computadora()
        resultado = self.determinar_resultado(eleccion_jugador, eleccion_computadora)

        # Actualizar la interfaz
        self.texto_resultado.config(text=f"{resultado}")
        self.texto_computadora.config(text=f"Computadora eligió: {eleccion_computadora}")
        self.puntaje.config(
            text=f"Jugador: {self.puntaje_jugador} | Computadora: {self.puntaje_computadora}"
        )

# Ejecutar el programa
if __name__ == "__main__":
    raiz = tk.Tk()
    app = Interfaz(raiz)
    raiz.mainloop()