import pygame
from pygame.locals import *
import random


# Inicializar Pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load('tetris.mp3')

# Play the music
pygame.mixer.music.play(-1)
# Inicializar Pygame

# Definir colores
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHTRED = (175, 20, 20)
GREEN = (0, 155, 0)
LIGHTGREEN = (20, 175, 20)
BLUE = (0, 0, 155)
LIGHTBLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Definir dimensiones de la cuadrícula
GRID_WIDTH = 28
GRID_HEIGHT = 20

# Definir tamaño de los bloques
BLOCK_SIZE = 20

# Definir velocidad de caída de los bloques
FALL_FREQUENCY = 1

# Definir formas de los bloques
SHAPES = {
    'S': [['.....',
           '.....',
           '..00.',
           '.00..',
           '.....'],
          ['.....',
           '..0..',
           '..00.',
           '...0.',
           '.....']],

    'Z': [['.....',
           '.....',
           '.00..',
           '..00.',
           '.....'],
          ['.....',
           '..0..',
           '.00..',
           '.0...',
           '.....']],

    'J': [['.....',
           '.0...',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..00.',
           '..0..',
           '..0..',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '...0.',
           '.....'],
          ['.....',
           '..0..',
           '..0..',
           '.00..',
           '.....']],

    'L': [['.....',
           '...0.',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..0..',
           '..0..',
           '..00.',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '.0...',
           '.....'],
          ['.....',
           '.00..',
           '..0..',
           '..0..']],
    'O': [['.....',
           '.....',
           '.00..',
           '.00..',
           '.....']],

    'I': [['..0..',
           '..0..',
           '..0..',
           '..0..',
           '.....'],
          ['.....',
           '0000.',
           '.....',
           '.....',
           '.....']],

    'T': [['.....',
           '..0..',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..0..',
           '..00.',
           '..0..',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '..0..',
           '.....'],
          ['.....',
           '..0..',
           '.00..',
           '..0..',
           '.....']]
}

# Definir colores de los bloques
BLOCK_COLORS = {
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': BLUE,
    'I': RED,
    'O': YELLOW,
    'T': YELLOW
}

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Crear la cuadrícula
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Crear el bloque actual y el siguiente
current_block = {
    'shape': random.choice(list(SHAPES.keys())),
    'rotation': 0,
    'x': GRID_WIDTH // 2 - 2,
    'y': 0
}
next_block = {
    'shape': random.choice(list(SHAPES.keys())),
    'rotation': 0,
    'x': GRID_WIDTH // 2 - 2,
    'y': 0
}
# Crear el reloj
clock = pygame.time.Clock()

# Crear la puntuación
score = 0


def draw_grid():
    # Dibujar la cuadrícula
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] is not None:
                pygame.draw.rect(
                    screen, BLOCK_COLORS[grid[y][x]], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE,
                                 y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_block(block):
    # Dibujar el bloque actual
    shape = SHAPES[block['shape']][block['rotation']]
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[y][x] == '0':
                pygame.draw.rect(screen, BLOCK_COLORS[block['shape']], ((
                    block['x'] + x) * BLOCK_SIZE, (block['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, ((
                    block['x'] + x) * BLOCK_SIZE, (block['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_next_block(block):
    # Dibujar el siguiente bloque
    shape = SHAPES[block['shape']][block['rotation']]
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[y][x] == '0':
                pygame.draw.rect(screen, BLOCK_COLORS[block['shape']], ((
                    GRID_WIDTH + 1 + x) * BLOCK_SIZE, (1 + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, ((
                    GRID_WIDTH + 1 + x) * BLOCK_SIZE, (1 + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def can_move(block, dx, dy):
    # Comprobar si el bloque puede moverse
    shape = SHAPES[block['shape']][block['rotation']]
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[y][x] == '0':
                new_x = block['x'] + x + dx
                new_y = block['y'] + y + dy
                if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT or grid[new_y][new_x] is not None:
                    return False
    return True


def can_rotate(block):
    # Comprobar si el bloque puede rotar
    shape = SHAPES[block['shape']][(
        block['rotation'] + 1) % len(SHAPES[block['shape']])]
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[y][x] == '0':
                new_x = block['x'] + x
                new_y = block['y'] + y
                if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT or grid[new_y][new_x] is not None:
                    return False
    return True


def add_to_grid(block):
    # Añadir el bloque a la cuadrícula
    global score
    shape = SHAPES[block['shape']][block['rotation']]
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[y][x] == '0':
                grid[block['y'] + y][block['x'] + x] = block['shape']
    lines = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if all(grid[y][x] is not None for x in range(GRID_WIDTH)):
            lines += 1
            for y2 in range(y, 0, -1):
                for x in range(GRID_WIDTH):
                    grid[y2][x] = grid[y2 - 1][x]
            for x in range(GRID_WIDTH):
                grid[0][x] = None
    if lines == 1:
        score += 40
    elif lines == 2:
        score += 100
    elif lines == 3:
        score += 300
    elif lines == 4:
        score += 1200


def new_block():
    # Crear un nuevo bloque
    global current_block, next_block
    if next_block is None:
        current_block = {
            'shape': random.choice(list(SHAPES.keys())),
            'rotation': 0,
            'x': GRID_WIDTH // 2 - 2,
            'y': 0
        }
        next_block = {
            'shape': random.choice(list(SHAPES.keys())),
            'rotation': 0,
            'x': GRID_WIDTH // 2 - 2,
            'y': 0
        }
    else:
        current_block = next_block
        next_block = {
            'shape': random.choice(list(SHAPES.keys())),
            'rotation': 0,
            'x': GRID_WIDTH // 2 - 2,
            'y': 0
        }


def game_over():
    # Comprobar si el juego ha terminado
    for x in range(GRID_WIDTH):
        if grid[0][x] is not None:
            return True
    return False


# Bucle principal del juego
last_fall_time = pygame.time.get_ticks()
while True:
    # Manejar eventos de entrada
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and can_move(current_block, -1, 0):
                current_block['x'] -= 1
            elif event.key == K_RIGHT and can_move(current_block, 1, 0):
                current_block['x'] += 1
            elif event.key == K_DOWN and can_move(current_block, 0, 1):
                current_block['y'] += 1
                last_fall_time = pygame.time.get_ticks()
            elif event.key == K_UP and can_rotate(current_block):
                current_block['rotation'] = (
                    current_block['rotation'] + 1) % len(SHAPES[current_block['shape']])

    # Mover el bloque actual hacia abajo
    if pygame.time.get_ticks() - last_fall_time > FALL_FREQUENCY * 1000:
        if can_move(current_block, 0, 1):
            current_block['y'] += 1
            last_fall_time = pygame.time.get_ticks()
        else:
            add_to_grid(current_block)
            new_block()
            last_fall_time = pygame.time.get_ticks()

    # Comprobar si el juego ha terminado
    if game_over():
        break

    # Dibujar la pantalla
    screen.fill(BLACK)
    draw_grid()
    draw_block(current_block)
    draw_next_block(next_block)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad del juego
    clock.tick(60)

# Mostrar mensaje de fin de juego
font = pygame.font.Font(None, 36)
text = font.render('Game Over', True, WHITE)
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery
screen.blit(text, text_rect)
pygame.display.update()

# current_block = None
# next_block = None

# Crear el primer bloque
new_block()

# Bucle principal del juego
last_fall_time = pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
