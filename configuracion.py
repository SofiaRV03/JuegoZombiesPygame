#Sofia Restrepo Villegas
import pygame
import os

anchoPantalla=800
altoPantalla=800


tamanoJugador= 30
velocidadJugador= 20

tamanoZombie= 30
velocidadZombie=15
timpoDireccionZombies= {  2:2000,
    3:3000,
    4:4000,
    5:5000}


tamanoBotella= 25
puntosPorBotella= 10


tamanoCorazones=30


playing="playing"
gameOver="gameOver"
inicio="inicio"
victoria="victory"


negro=(0,0,0)
blanco=(255,255,255)


tamanoCelda=40


toleranciaColision= 4
velocidadDesplazamientoParedes=1


nivel = [
    "11111111111111101111",
    "1P000000060000020001",
    "10111101111110111101",
    "10000200030010000001",
    "10110111101111101101",
    "10006000100000000001",
    "11111110101111111111",
    "10000000100000060001",
    "10111111101111111101",
    "10500000004000600001",
    "11101111111111110111",
    "10000010000010000001",
    "10111110111010111101",
    "10000060000030000001",
    "11101111101111110111",
    "10000002000001000011",
    "10000011111110111011",
    "10000006000000010001",
    "14000005000000000011",
    "11111111111111111111"
]
# nivel = [
#     "100",
#     "P03"
# ]



def cargar_imagen(nombre):
    return pygame.image.load(os.path.join("imagenes", nombre)).convert_alpha()
