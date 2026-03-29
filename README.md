# Juego de Supervivencia: Zombies 

Este es un juego de supervivencia en 2D desarrollado en **Python** utilizando la librería **Pygame**. El jugador debe navegar a través de un laberinto, recolectando medicinas y evitando el contacto con zombies para ganar.

## Características del Proyecto

- **Mecánicas de Juego**: Movimiento en 4 direcciones, sistema de colisiones con paredes y enemigos.
- **Sistema de Salud**: El jugador cuenta con 100 puntos de energía representados por 4 corazones.
- **Items Interactivos**:
  - **Medicinas**: Debes recolectarlas todas para ganar el juego. Cada una otorga puntos.
  - **Botiquines (SalvaVidas)**: Restauran la salud del jugador cuando ha recibido daño.
- **Enemigos**: Zombies con diferentes patrones de movimiento que restan vida al contacto.
- **Estados de Juego**: Pantallas de inicio, juego en curso, derrota (Game Over) y victoria.
- **Arquitectura**: Código organizado en módulos para configuración, sprites y lógica principal.

## Instalación y Ejecución

### Requisitos Previos
- Python 3.x instalado.
- Librería Pygame.

### Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/SofiaRV03/JuegoZombiesPygame.git
   ```
2. Instala la dependencia necesaria:
   ```bash
   pip install pygame
   ```

### Cómo Jugar
Para iniciar el juego, ejecuta el archivo principal:
```bash
python main.py
```

## Controles

- **Flechas de dirección**: Mover al personaje (arriba, abajo, izquierda, derecha).
- **Barra Espaciadora**: Iniciar el juego desde la pantalla de bienvenida o reiniciar después de ganar/perder.

## Estructura del Código

- [main.py]: Punto de entrada que inicializa y arranca el ciclo principal.
- [juego.py]: Contiene la clase `Juego`, encargada de la lógica global, renderizado y gestión de estados.
- [sprites.py]: Define las clases para los objetos del juego (`Jugador`, `Zombie`, `Pared`, `Medicina`, `salvaVidas`).
- [configuracion.py]: Almacena constantes, colores y la definición del mapa por cuadrícula.

## Autor
- **Sofia Restrepo Villegas**



