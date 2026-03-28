#Sofia Restrepo Villegas
import pygame
import sys
from configuracion import *
from sprites import *

class Juego:
    def __init__(self):
        self.pantalla=pygame.display.set_mode((anchoPantalla,altoPantalla))
        pygame.display.set_caption("Zombies")

        self.reloj=pygame.time.Clock()

        self.jugando=True
        self.estadoJuego= inicio
        self.jugador=None
        self.puntaje=0
        self.zombies=[]

        self.paredes=[]
        self.medicinas=[]
        self.salvaVidas=[]
        self.niveles()
        self.fuente=pygame.font.Font(None, 36)
        self.fuenteTitulo= pygame.font.Font("C:\Windows\Fonts\Arial.ttf",74)



    def pantallaInicio(self):
        titulo= self.fuenteTitulo.render("ZOMBIES", True, negro)
        textoEmpezar= self.fuente.render("Presiona ESPACIO para comenzar", True, negro)
        textoControles= self.fuente.render("Usa las flechas para desplazarte", True, negro)
        
        tituloRectangulo= titulo.get_rect(center=(anchoPantalla/2, altoPantalla/3))
        empezarRectangulo= textoEmpezar.get_rect(center=(anchoPantalla/2, altoPantalla/2))
        controlesRectangulo= textoControles.get_rect(center=(anchoPantalla/2, 2*altoPantalla/3))

        self.pantalla.fill(blanco)
        self.pantalla.blit(titulo, tituloRectangulo)
        self.pantalla.blit(textoEmpezar,empezarRectangulo)
        self.pantalla.blit(textoControles,controlesRectangulo)

    def pantallaPerdio(self):
        textoPerdio= self.fuenteTitulo.render("Game Over", True, negro)
        textoPuntaje=self.fuenteTitulo.render(f"Puntaje:{self.puntaje} ", True, negro)
        textoReiniciar=self.fuente.render("Presiona ESPACIO para reiniciar", True, negro)
        perdioRectangulo= textoPerdio.get_rect(center=(anchoPantalla/2, altoPantalla/3))
        puntajeRectangulo= textoPuntaje.get_rect(center=(anchoPantalla/2, altoPantalla/2))
        reinicioRectangulo= textoReiniciar.get_rect(center=(anchoPantalla/2, 2*altoPantalla/3))

        self.pantalla.fill(blanco)
        self.pantalla.blit(textoPerdio,perdioRectangulo)
        self.pantalla.blit(textoPuntaje,puntajeRectangulo)
        self.pantalla.blit(textoReiniciar,reinicioRectangulo)

    def pantallaVictoria(self):
        textoVictoria= self.fuenteTitulo.render("VICTORY", True, negro)
        textoPuntaje=self.fuenteTitulo.render(f"Puntaje:{self.puntaje} ", True, negro)
        textoReiniciar=self.fuente.render("Presiona ESPACIO para jugar de nuevo", True, negro)
        perdioRectangulo= textoVictoria.get_rect(center=(anchoPantalla/2, altoPantalla/3))
        puntajeRectangulo= textoPuntaje.get_rect(center=(anchoPantalla/2, altoPantalla/2))
        reinicioRectangulo= textoReiniciar.get_rect(center=(anchoPantalla/2, 2*altoPantalla/3))

        self.pantalla.fill(blanco)
        self.pantalla.blit(textoVictoria,perdioRectangulo)
        self.pantalla.blit(textoPuntaje,puntajeRectangulo)
        self.pantalla.blit(textoReiniciar,reinicioRectangulo)


    def niveles(self):
        for indexFila,fila in enumerate(nivel):
            for indexCol, columna in enumerate (fila):
                if columna == "1":
                    self.paredes.append(Pared(indexCol,indexFila))
                elif columna == "0":
                    self.medicinas.append(Medicina(indexCol,indexFila))
                elif columna == "P":
                    self.jugador=Jugador(indexCol,indexFila)
                elif columna =="2":
                    self.zombies.append(Zombie(indexCol,indexFila,2))
                elif columna =="3":
                    self.zombies.append(Zombie(indexCol,indexFila,3))
                elif columna =="4":
                    self.zombies.append(Zombie(indexCol,indexFila,4))
                elif columna =="5":
                    self.zombies.append(Zombie(indexCol,indexFila,5))
                elif columna == "6":
                    self.salvaVidas.append(salvaVidas(indexCol,indexFila))

    def controlEventos(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.jugando=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.estadoJuego == inicio:
                        self.estadoJuego=playing

                    elif self.estadoJuego in ["gameOver","victory"]:
                        self.puntaje=0
                        self.niveles()
                        self.estadoJuego=playing

    def actualizar(self):
        if self.estadoJuego == playing:
            self.jugador.actualizar(self.paredes)

            for zombie in self.zombies:
                zombie.actualizar(self.paredes)


            for zombie in self.zombies:
                if self.jugador.rectangulo.colliderect(zombie.rectangulo):
                    tiempoActual= pygame.time.get_ticks()
                    if tiempoActual - self.jugador.ultimo_daño > self.jugador.tiempo_cooldown:
                        self.jugador.energia-=25
                        self.jugador.ultimo_daño= tiempoActual
                        if self.jugador.energia<=0:
                            self.estadoJuego= gameOver
                            self.medicinas=[]
                            self.zombies=[]

            for medicina in self.medicinas:
                if self.jugador.rectangulo.colliderect(medicina.rectangulo):
                    self.medicinas.remove(medicina)
                    self.puntaje += puntosPorBotella
                    if len(self.medicinas) == 0:
                        self.estadoJuego = "victory"
                        self.medicinas=[]
                        self.zombies=[]

            for salvavida in self.salvaVidas:
                if self.jugador.rectangulo.colliderect(salvavida.rectangulo):
                    self.salvaVidas.remove(salvavida)
                    if self.jugador.energia < 100:
                        self.jugador.energia+=25
                        if self.jugador.energia>100:
                            self.jugador.energia=100

    def dibujar(self):
        if self.estadoJuego == inicio:
            self.pantallaInicio()

        elif self.estadoJuego== gameOver:
            self.pantallaPerdio()

        elif self.estadoJuego == victoria:
            self.pantallaVictoria()

        elif self.estadoJuego == playing:
            self.pantalla.fill(blanco)

            for pared in self.paredes:
                pared.dibujar(self.pantalla)
            
            self.vidaJugador()

            for medicina in self.medicinas:
                medicina.dibujar(self.pantalla)
            
            for salvavida in self.salvaVidas:
                salvavida.dibujar(self.pantalla)
                
            self.jugador.dibujar(self.pantalla)

            textoPuntaje= self.fuente.render(f"Puntaje: {self.puntaje}", True, blanco)
            self.pantalla.blit(textoPuntaje,(625,10))

            for zombie in self.zombies:
                zombie.dibujar(self.pantalla)

        pygame.display.flip()
         
    def vidaJugador(self):
        corazonVacio=cargar_imagen("corazonvacio.png")
        corazonVacio= pygame.transform.scale(corazonVacio, (tamanoCorazones, tamanoCorazones))
        corazonLleno=cargar_imagen("corazonlleno.png")
        corazonLleno= pygame.transform.scale(corazonLleno, (tamanoCorazones, tamanoCorazones))

        for i in range(4):
            if self.jugador.energia >= ((i+1)*25):
                self.pantalla.blit(corazonLleno, (5+i*50,5))   

            else:
                self.pantalla.blit(corazonVacio, (5+i*50,5))   

    def jugar(self):
        while self.jugando:
            self.controlEventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(10)
