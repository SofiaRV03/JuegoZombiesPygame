#Sofia Restrepo Villegas
from configuracion import *
import pygame
import random
class Pared:
    def __init__(self,x,y):
        
        self.rectangulo=pygame.Rect(x*tamanoCelda, y * tamanoCelda, tamanoCelda,tamanoCelda)
        self.imagen=cargar_imagen("muro.png")
        self.imagen = pygame.transform.scale(self.imagen, (tamanoCelda, tamanoCelda))

        
    def dibujar(self,pantalla):
        pantalla.blit(self.imagen, self.rectangulo)



class Item:
    def __init__(self, x, y, nombre_imagen, ancho, alto):
        self.x = x * tamanoCelda + tamanoCelda // 2
        self.y = y * tamanoCelda + tamanoCelda // 2

        self.imagen = cargar_imagen(nombre_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rectangulo = self.imagen.get_rect(center=(self.x, self.y))

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rectangulo)

class Medicina(Item):
    def __init__(self, x, y):
        super().__init__(x, y, "medicina.png", tamanoBotella, tamanoBotella)


class salvaVidas(Item):
    def __init__(self, x, y):
        super().__init__(x, y, "corazonlleno.png", tamanoBotella, tamanoBotella)


class Jugador:
    def __init__(self,x,y):
        self.x= x* tamanoCelda+tamanoCelda//2
        self.y=y* tamanoCelda+tamanoCelda//2
        self.energia=100
        self.ultimo_daño = 0  
        self.tiempo_cooldown = 1000  

        self.sprite =cargar_imagen("kate.png")        
        self.frame=0
        self.intento_alternativo = False

        self.sprite.set_clip(pygame.Rect(10, 12, 32, 62))
        self.imagen = self.sprite.subsurface(self.sprite.get_clip())
        self.imagen= pygame.transform.scale(self. imagen, (tamanoJugador,tamanoJugador))
        
        self.rectangulo=self.imagen.get_rect(center=(self.x,self.y))

        self.direccion="parardoDerecha"
        self.izquierda_frames = {0: (12 , 90 , 28, 62 ), 1: (60 , 91 , 42  , 60 ), 2: (162 , 92 , 44 , 60)}
        self.derecha_frames = {0: (12 , 166  , 28  , 62 ), 1: (54 , 168 , 42, 60), 2: (158 , 168 , 44, 60)}
        self.arriba_frames = {0: (10 , 242 , 32 , 60 ), 1: (64 , 244 , 32 , 58 ), 2: (164 , 244 , 32, 58)}
        self.abajo_frames = {0: (10 , 12  , 32 , 62 ), 1: (62 , 14 , 32, 60 ), 2: (166 , 14 , 32 , 60)}

    def get_frame(self, frame_set):  
        self.frame += 1
        if self.frame > len(frame_set) - 1:
            self.frame = 0
        return frame_set[self.frame]
    
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:  
            rect = self.get_frame(clipped_rect)
        else:
            rect = clipped_rect
        self.sprite.set_clip(pygame.Rect(rect))
        return self.sprite.subsurface(self.sprite.get_clip())
    
    def desplazar(self, paredes):
        if self.dx != 0:
            if not self.checkColisiones(paredes, self.dx, 0):
                self.x += self.dx
            #     # self.intento_alternativo = False
            # else:
            #     if not self.intento_alternativo:
            #         if self.checkColisiones(paredes, self.dx, -velocidadDesplazamientoParedes):
            #             if not self.checkColisiones(paredes, 0, velocidadDesplazamientoParedes):
            #                 self.y += velocidadDesplazamientoParedes
            #         else:
            #             self.y -= velocidadDesplazamientoParedes
            #         self.intento_alternativo = True 

        if self.dy != 0:
            if not self.checkColisiones(paredes, 0, self.dy):
                self.y += self.dy
            #     # self.intento_alternativo = False
            # else:
            #     if not self.intento_alternativo:
            #         if self.checkColisiones(paredes, -velocidadDesplazamientoParedes, self.dy):
            #             if not self.checkColisiones(paredes, velocidadDesplazamientoParedes, 0):
            #                 self.x += velocidadDesplazamientoParedes
            #         else:
            #             self.x -= velocidadDesplazamientoParedes
            #         self.intento_alternativo = True

        
    




        nueva_x=self.x
        nueva_y=self.y
    
        if nueva_x > anchoPantalla - tamanoJugador:
            self.x = anchoPantalla - tamanoJugador 
        elif nueva_x < tamanoJugador:
            self.x = tamanoJugador
        else:
            self.x = nueva_x    


        if nueva_y > altoPantalla - tamanoJugador:
            self.y = altoPantalla - tamanoJugador
        elif nueva_y < tamanoJugador//2:
            self.y = tamanoJugador//2
        else:
            self.y = nueva_y 

        self.rectangulo.center = (self.x, self.y)



        

    def manejarEntradas(self):
        keys=pygame.key.get_pressed()

        self.dx=0
        self.dy=0
        
        if keys[pygame.K_RIGHT]:
            self.direccion= "derecha"
            self.dx= velocidadJugador

        elif keys [pygame.K_LEFT]:
            
            self.direccion="izquierda"
            self.dx= -velocidadJugador

        elif keys[pygame.K_UP]:
            
            self.direccion="arriba"
            self.dy= -velocidadJugador

        elif keys[pygame.K_DOWN]:
            
            self.direccion="abajo"
            self.dy=velocidadJugador

        else:
            if "izquierda" in self.direccion:
                self.direccion = "paradoIzquierda"
            elif "derecha" in self.direccion:
                self.direccion = "paradoDerecha"
            elif "arriba" in self.direccion:
                self.direccion = "paradoArriba"
            elif "abajo" in self.direccion:
                self.direccion = "paradoAbajo"



   
    def checkColisiones(self,paredes, dx=0, dy=0):

        futRectangulo= self.rectangulo.copy()
        futRectangulo.x+=dx
        futRectangulo.y+=dy

        for pared in paredes:
            if futRectangulo.colliderect(pared.rectangulo):
                return True
        return False



            
    def actualizar_animacion(self):
        if self.direccion == "izquierda":
            self.imagen = pygame.transform.scale(self.clip(self.izquierda_frames), (tamanoJugador, tamanoJugador))
        elif self.direccion == "derecha":
            self.imagen = pygame.transform.scale(self.clip(self.derecha_frames), (tamanoJugador, tamanoJugador))
        elif self.direccion == "arriba":
            self.imagen = pygame.transform.scale(self.clip(self.arriba_frames), (tamanoJugador, tamanoJugador))
        elif self.direccion == "abajo":
            self.imagen = pygame.transform.scale(self.clip(self.abajo_frames), (tamanoJugador, tamanoJugador))
        elif self.direccion == "paradoIzquierda":
            self.imagen = pygame.transform.scale(self.clip(self.izquierda_frames[0]), (tamanoJugador, tamanoJugador))
        elif self.direccion == "paradoDerecha":
            self.imagen = pygame.transform.scale(self.clip(self.derecha_frames[0]), (tamanoJugador, tamanoJugador))
        elif self.direccion == "paradoArriba":
            self.imagen = pygame.transform.scale(self.clip(self.arriba_frames[0]), (tamanoJugador, tamanoJugador))
        elif self.direccion == "paradoAbajo":
            self.imagen = pygame.transform.scale(self.clip(self.abajo_frames[0]), (tamanoJugador, tamanoJugador))

        


    def dibujar(self,pantalla):
        pantalla.blit(self.imagen,self.rectangulo)

    def actualizar(self, paredes):
        self.manejarEntradas()
        self.actualizar_animacion()
        self.desplazar(paredes)

class Zombie:
    def __init__(self,x,y,tipo):
        self.x= x* tamanoCelda+tamanoCelda//2
        self.y=y* tamanoCelda+tamanoCelda//2

        self.tipo=tipo
        self.tiempoDireccion= timpoDireccionZombies[tipo]
        self.sprite= cargar_imagen("zombies.png")

        self.frame=0

        self.sprite.set_clip(pygame.Rect(10, 12, 32, 62))
        self.imagen = self.sprite.subsurface(self.sprite.get_clip())
        self.imagen= pygame.transform.scale(self. imagen, (tamanoZombie,tamanoZombie))
        
        self.rectangulo=self.imagen.get_rect(center=(self.x,self.y))
        self.direccion=random.randint(0,3)



        self.izquierda_frames = {0: (12 , 90 , 28, 62 ), 1: (60 , 91 , 42  , 60 ), 2: (162 , 92 , 44 , 60)}
        self.derecha_frames = {0: (12 , 166  , 28  , 62 ), 1: (54 , 168 , 42, 60), 2: (158 , 168 , 44, 60)}
        self.arriba_frames = {0: (10 , 242 , 32 , 60 ), 1: (64 , 244 , 32 , 58 ), 2: (164 , 244 , 32, 58)}
        self.abajo_frames = {0: (10 , 12  , 32 , 62 ), 1: (62 , 14 , 32, 60 ), 2: (166 , 14 , 32 , 60)}

    def get_frame(self, frame_set):  
        self.frame += 1
        if self.frame > len(frame_set) - 1:
            self.frame = 0
        return frame_set[self.frame]
    
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:  
            rect = self.get_frame(clipped_rect)
        else:
            rect = clipped_rect
        self.sprite.set_clip(pygame.Rect(rect))
        return self.sprite.subsurface(self.sprite.get_clip())


    
    def obtenerSigDireccion(self):
        if self.tipo == 2:
            return random.randint(0,3)
        elif self.tipo == 3:
            if self.direccion in [0,1]:
                return random.randint(2,3)
            else:
                return random.randint(0,1)
        elif self.tipo== 4:
            return (self.direccion +1 )%4
        else:
            return (self.direccion -1) % 4

    
    def cambiarDireccion(self,paredes):
        nuevaDireccion=self.obtenerSigDireccion()
        if self.puedeDesplazar(nuevaDireccion,paredes):
                self.direccion=nuevaDireccion
        else:
                self.direccion= random.randint(0,3)

        self.tiempoDireccion= pygame.time.get_ticks()

    def puedeDesplazar(self,direccion,paredes):
        dx=0
        dy=0

        if self.direccion == 0:
            dx=velocidadZombie
        elif self.direccion==1:
            dx=-velocidadZombie
        elif self.direccion == 2:
            dy=-velocidadZombie
        elif self.direccion == 3:
            dy= velocidadZombie

        nuevoRectangulo=self.rectangulo.copy()
        nuevoRectangulo.x+=dx
        nuevoRectangulo.y+=dy

        for pared in paredes:
            if nuevoRectangulo.colliderect(pared.rectangulo):
                return False
        return True
        



    

    def desplazar(self,paredes):
        tiempoActual= pygame.time.get_ticks()
        if tiempoActual - self.tiempoDireccion > self.tiempoDireccion:
            self.cambiarDireccion(paredes)

        dx=0
        dy=0

        if self.direccion == 0:
            dx=velocidadZombie
        elif self.direccion==1:
            dx=-velocidadZombie
        elif self.direccion == 2:
            dy=-velocidadZombie
        elif self.direccion == 3:
            dy= velocidadZombie

        nuevoRectangulo=self.rectangulo.copy()
        nuevoRectangulo.x+=dx
        nuevoRectangulo.y+=dy

        mover= True

        for pared in paredes:
            if nuevoRectangulo.colliderect(pared.rectangulo):
                mover=False
                self.cambiarDireccion(paredes)
                break
        if mover:
            self.x+=dx
            self.y+=dy
            self.rectangulo.center=(self.x,self.y)
        
        
        nueva_x=self.x
        nueva_y=self.y
    
        if nueva_x > anchoPantalla - tamanoJugador:
            self.x = anchoPantalla - tamanoJugador 
            self.cambiarDireccion(paredes)
        elif nueva_x < tamanoJugador:
            self.x = tamanoJugador
            self.cambiarDireccion(paredes)
        else:
            self.x = nueva_x    


        if nueva_y > altoPantalla - tamanoJugador:
            self.y = altoPantalla - tamanoJugador
            self.cambiarDireccion(paredes)
        elif nueva_y < tamanoJugador//2:
            self.y = tamanoJugador//2
            self.cambiarDireccion(paredes)
        else:
            self.y = nueva_y 

        self.rectangulo.center=(self.x,self.y)

    def actualizar_animacion(self):
            if self.direccion == 1:
                self.imagen = pygame.transform.scale(self.clip(self.izquierda_frames), (tamanoZombie, tamanoZombie))
            elif self.direccion == 0:
                self.imagen = pygame.transform.scale(self.clip(self.derecha_frames), (tamanoZombie, tamanoZombie))
            elif self.direccion ==2:
                self.imagen = pygame.transform.scale(self.clip(self.arriba_frames), (tamanoZombie, tamanoZombie))
            elif self.direccion == 3:
                self.imagen = pygame.transform.scale(self.clip(self.abajo_frames), (tamanoZombie, tamanoZombie))
            # elif self.direccion == "paradoIzquierda":
            #     self.imagen = pygame.transform.scale(self.clip(self.izquierda_frames[0]), (tamanoJugador, tamanoJugador))
            # elif self.direccion == "paradoDerecha":
            #     self.imagen = pygame.transform.scale(self.clip(self.derecha_frames[0]), (tamanoJugador, tamanoJugador))
            # elif self.direccion == "paradoArriba":
            #     self.imagen = pygame.transform.scale(self.clip(self.arriba_frames[0]), (tamanoJugador, tamanoJugador))
            # elif self.direccion == "paradoAbajo":
            #     self.imagen = pygame.transform.scale(self.clip(self.abajo_frames[0]), (tamanoJugador, tamanoJugador))


    def dibujar(self,pantalla):
         pantalla.blit(self.imagen,self.rectangulo)

    def actualizar(self, paredes):
        # self.manejarEntradas()
        self.actualizar_animacion()
        self.desplazar(paredes)















    
