import tkinter as tk
import random
from PIL import Image, ImageTk
import sys
import os

# Alvarez_David_Tarea_03

# Crear una aplicación móvil en Android donde el usuario juegue al clásico juego de Piedra, Papel o Tijera contra la computadora.
# El jugador debe seleccionar una opción y la aplicación seleccionará aleatoriamente una de las tres opciones para competir. 
# Al final, el juego mostrará el resultado (si el jugador ganó, perdió o hubo empate).
# Función para obtener la ruta del recurso, ya sea en el código fuente o empaquetado en el .exe

# Obtiene la ruta de la carpeta de recursos dependiendo de si estamos en un archivo empaquetado o no
def obtener_ruta_recurso(ruta_recurso):
    if getattr(sys, 'frozen', False):  # Si estamos ejecutando el .exe
        return os.path.join(sys._MEIPASS, ruta_recurso)
    else:  # Si estamos ejecutando el código fuente
        return os.path.join(os.path.dirname(__file__), ruta_recurso)

class Juego:    # Esta clase maneja la lógica del juego
    
    def __init__(self):                    # Inicializar los puntajes en 0
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        self.opciones = ["Piedra", "Papel", "Tijera"]    #  Definir las opciones para el juego

    def elec_cpu(self):               # Genera la elección aleatoria para la computadora
        return random.choice(self.opciones)

    def resultado(self, jugador, computadora):    # Verifica el resultado
        if jugador == computadora:
            return "Empate"
        elif (jugador == "Piedra" and computadora == "Tijera") or \
             (jugador == "Papel" and computadora == "Piedra") or \
             (jugador == "Tijera" and computadora == "Papel"):
            self.puntaje_jugador += 1
            return "Ganaste"
        else:
            self.puntaje_computadora += 1
            return "Perdiste"


class InterfazJuego:     # Esta clase maneja la interfaz del juego, las opciones y resultados
    
    def __init__(self, juego):
        self.ventana_juego = tk.Tk()     # Crea la ventana del juego
        self.ventana_juego.title("Juego: Piedra, Papel o Tijera")
        self.ventana_juego.geometry("400x500")
        self.juego = juego          # Recibe la lógica del juego
        
        # Canvas para la imagen de fondo
        self.canvas1 = tk.Canvas(self.ventana_juego, width=400, height=500)
        self.canvas1.pack(fill="both", expand=True)

        # Cargar la imagen de fondo
        ruta_fondo = obtener_ruta_recurso("img_recursos/fondo2.jpg")
        self.img_fondo = Image.open(ruta_fondo)  # Abre la imagen
        self.img_fondo = self.img_fondo.resize((400, 500))  # Redimensiona la imagen 
        self.img_fondo_tk = ImageTk.PhotoImage(self.img_fondo)

        # Coloca la imagen en el canvas
        self.canvas1.create_image(0, 0, anchor="nw", image=self.img_fondo_tk)
        
        # Mostar puntuación
        self.label_puntuacion = tk.Label(self.ventana_juego, text="Jugador: 0           Computadora: 0", font=("Arial", 16))
        self.label_puntuacion.place(x=30, y=10)

        # Mostrar resultado
        self.label_resultado = tk.Label(self.ventana_juego, text="¡Elige tu opción!", font=("Arial", 18), fg="blue")
        self.label_resultado.place(x=100, y=60)

        # Contenedor para las opciones del jugador
        self.frame_botones = tk.Frame(self.ventana_juego)
        self.frame_botones.place(x=20, y=125)

        # Cargar imágenes de los botones
        ruta_piedra = obtener_ruta_recurso("img_recursos/boton1.png")
        ruta_papel = obtener_ruta_recurso("img_recursos/boton2.png")
        ruta_tijera = obtener_ruta_recurso("img_recursos/boton3.png")
        
        self.img_piedra = ImageTk.PhotoImage(Image.open(ruta_piedra).resize((100, 100)))
        self.img_papel = ImageTk.PhotoImage(Image.open(ruta_papel).resize((100, 100)))
        self.img_tijera = ImageTk.PhotoImage(Image.open(ruta_tijera).resize((100, 100)))

        # Botones con imágenes y funciones
        self.boton_piedra = tk.Button(self.frame_botones, image=self.img_piedra, command=lambda: self.jugar("Piedra"), bd=0, relief="flat")
        self.boton_piedra.grid(row=0, column=0, padx=10)

        self.boton_papel = tk.Button(self.frame_botones, image=self.img_papel, command=lambda: self.jugar("Papel"), bd=0, relief="flat")
        self.boton_papel.grid(row=0, column=1, padx=10)

        self.boton_tijera = tk.Button(self.frame_botones, image=self.img_tijera, command=lambda: self.jugar("Tijera"), bd=0, relief="flat")
        self.boton_tijera.grid(row=0, column=2, padx=10)

        # Mostrar la elección de la computadora
        self.label_cpu = tk.Label(self.ventana_juego, text="Computadora eligió: ", font=("Arial", 14, "bold"))
        self.label_cpu.place(x=110, y=270)

        self.img_cpu = tk.Label(self.ventana_juego)
        self.img_cpu.place(x=150, y=320)

    def jugar(self, eleccion_jugador):    # Lógica que se ejecuta al presionar el botón
        eleccion_computadora = self.juego.elec_cpu()

        # Mostrar imagen de la elección de la computadora según corresponda
        if eleccion_computadora == "Piedra":
            self.img_cpu.config(image=self.img_piedra)
        elif eleccion_computadora == "Papel":
            self.img_cpu.config(image=self.img_papel)
        elif eleccion_computadora == "Tijera":
            self.img_cpu.config(image=self.img_tijera)

        # Verificar el resultado
        resultado = self.juego.resultado(eleccion_jugador, eleccion_computadora)

        # Actualizar el resultado y la puntuación
        self.label_resultado.config(text=f"Resultado: {resultado}")
        self.label_puntuacion.config(text=f"Jugador: {self.juego.puntaje_jugador}           Computadora: {self.juego.puntaje_computadora}")

class InicioJuego: # Ventana principal del juego

    def __init__(self, root):       # Ventana principal de la app
        self.root = root
        self.root.title("Menú Juego")
        self.root.geometry("400x500")
        
        # # Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=400, height=550)
        self.canvas.pack(fill="both", expand=True)

        # Cargar la imagen de fondo
        ruta_fondo1 = obtener_ruta_recurso("img_recursos/fondo1.png")
        self.imagen_fondo = Image.open(ruta_fondo1)  # Abre la imagen
        self.imagen_fondo = self.imagen_fondo.resize((400, 550))  # Redimensiona la imagen
        self.imagen_fondo_tk = ImageTk.PhotoImage(self.imagen_fondo)

        # Coloca la imagen en el canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagen_fondo_tk)
        
        # Cargar imagen para el boton
        ruta_iniciar = obtener_ruta_recurso("img_recursos/boton4.png")
        self.img_iniciar = ImageTk.PhotoImage(Image.open(ruta_iniciar).resize((200, 80)))
        
        # Botón para iniciar el juego
        self.boton_iniciar = tk.Button(self.root, image=self.img_iniciar, command=self.iniciar_juego, bg="SkyBlue1", bd=0, relief="flat")
        self.boton_iniciar.place(x=100, y=360)

    def iniciar_juego(self):  # Abre la ventana del juego al presionar iniciar
        self.root.destroy()    # Cierra la ventana principal
        juego = Juego()  # Lógica del juego
        InterfazJuego(juego)  # Pasar la lógica del juego a la interfaz

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Ventana principal
    app = InicioJuego(root)  # Crear la interfaz de inicio
    root.mainloop()   # Mantenemos la ventana en ejecución