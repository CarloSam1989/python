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
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)


# Definir dimensiones de la pantalla
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Definir dimensiones de la cuadrícula
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Definir tamaño de los bloques
BLOCK_SIZE = 25

# Definir velocidad de caída de los bloques
FALL_FREQUENCY = 2

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
    'L': ORANGE,
    'O': YELLOW,
    'I': LIGHTBLUE,
    'T': PURPLE
    
}

# Crear una cuadrícula vacía
def create_grid():
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    return grid

# Dibujar la cuadrícula
def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

# Dibujar un bloque
def draw_block(block, x, y):
    shape = SHAPES[block['shape']][block['rotation']]
    color = BLOCK_COLORS[block['shape']]
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == '0':
                pygame.draw.rect(screen, color, (x + col * BLOCK_SIZE, y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Comprobar si el bloque está en una posición válida
def is_valid_position(block, x, y):
    shape = SHAPES[block['shape']][block['rotation']]
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == '0':
                if not (0 <= x + col < GRID_WIDTH and 0 <= y + row < GRID_HEIGHT):
                    return False
                if grid[y + row][x + col] != BLACK:
                    return False
    return True

# Agregar el bloque a la cuadrícula
def add_to_grid(block, x, y):
    shape = SHAPES[block['shape']][block['rotation']]
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == '0':
                grid[y + row][x + col] = BLOCK_COLORS[block['shape']]

# Eliminar filas completas
def remove_complete_rows():
    rows_to_remove = []
    for row in range(GRID_HEIGHT):
        if all(color != BLACK for color in grid[row]):
            rows_to_remove.append(row)
    for row in rows_to_remove:
        del grid[row]
        grid.insert(0, [BLACK] * GRID_WIDTH)

# Mostrar el siguiente bloque
def draw_next_block(next_block):
    next_shape = SHAPES[next_block['shape']][next_block['rotation']]
    for row in range(len(next_shape)):
        for col in range(len(next_shape[row])):
            if next_shape[row][col] == '0':
                pygame.draw.rect(screen, BLOCK_COLORS[next_block['shape']],
                                 (SCREEN_WIDTH + 50 + col * BLOCK_SIZE, 100 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Comprobar si el juego ha terminado
def game_over():
    return any(color != BLACK for color in grid[0])

# Crear la ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH + 200, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Crear un reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Variables del juego
grid = create_grid()
current_block = {'shape': random.choice(list(SHAPES.keys())), 'rotation': 0, 'x': GRID_WIDTH // 2 - 1, 'y': 0}
next_block = {'shape': random.choice(list(SHAPES.keys())), 'rotation': 0}
fall_counter = 0
score = 0

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                if is_valid_position(current_block, current_block['x'] - 1, current_block['y']):
                    current_block['x'] -= 1
            elif event.key == K_RIGHT:
                if is_valid_position(current_block, current_block['x'] + 1, current_block['y']):
                    current_block['x'] += 1
            elif event.key == K_DOWN:
                if is_valid_position(current_block, current_block['x'], current_block['y'] + 1):
                    current_block['y'] += 1
            elif event.key == K_UP:
                if is_valid_position(current_block, current_block['x'], current_block['y']):
                    current_block['rotation'] = (current_block['rotation'] + 1) % len(SHAPES[current_block['shape']])
            elif event.key == K_SPACE:
                while is_valid_position(current_block, current_block['x'], current_block['y'] + 1):
                    current_block['y'] += 1


    # Actualizar la posición del bloque
    fall_counter += 1
    if fall_counter >= FALL_FREQUENCY:
        if is_valid_position(current_block, current_block['x'], current_block['y'] + 1):
            current_block['y'] += 1
        else:
            add_to_grid(current_block, current_block['x'], current_block['y'])
            remove_complete_rows()
            if game_over():
                running = False
            else:
                current_block = next_block
                next_block = {'shape': random.choice(list(SHAPES.keys())), 'rotation': 0}
            fall_counter = 0

    # Dibujar el fondo
    screen.fill(BLACK)

    # Dibujar la cuadrícula
    draw_grid()

    # Dibujar los bloques en la cuadrícula
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] != BLACK:
                pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Dibujar el bloque actual
    if current_block is not None and 'x' in current_block and 'y' in current_block and 'shape' in current_block:
     draw_block(current_block, current_block['x'] * BLOCK_SIZE, current_block['y'] * BLOCK_SIZE)


    # Dibujar el siguiente bloque
    draw_next_block(next_block)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad del juego
    clock.tick(10)

# Mostrar la puntuación final
final_score_text = pygame.font.Font(None, 50).render("Final Score: " + str(score), True, WHITE)
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - final_score_text.get_height() // 2))
pygame.display.update()

# Esperar un poco antes de cerrar la ventana
pygame.time.wait(3000)

# Salir del juego
pygame.quit()
