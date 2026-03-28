#Sofia Restrepo Villegas
import pygame
import sys
from configuracion import * 
from juego import *

def main():
    pygame.init()

    juego = Juego()
    juego.jugar()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



















