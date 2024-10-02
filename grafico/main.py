import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

# Define dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clue Game")

# Carga la imagen del mapa
map_image = pygame.image.load('clue.png')  # Ruta corregida

# Escala la imagen a la altura de la ventana, manteniendo la relación de aspecto
aspect_ratio = map_image.get_width() / map_image.get_height()
new_width = int(height * aspect_ratio)
map_image = pygame.transform.scale(map_image, (new_width, height))

# Carga las imágenes de los personajes
juan_image = pygame.image.load('juan.png')
maria_image = pygame.image.load('maria.png')
pedro_image = pygame.image.load('pedro.png')

# Escala las imágenes de los personajes a un tamaño más pequeño
character_height = 50  # Nuevo tamaño más pequeño para los personajes
juan_image = pygame.transform.scale(juan_image, (int(juan_image.get_width() * (character_height / juan_image.get_height())), character_height))
maria_image = pygame.transform.scale(maria_image, (int(maria_image.get_width() * (character_height / maria_image.get_height())), character_height))
pedro_image = pygame.transform.scale(pedro_image, (int(pedro_image.get_width() * (character_height / pedro_image.get_height())), character_height))

# Carga las imágenes de los objetos
cuchillo_image = pygame.image.load('cuchillo.png')
veneno_image = pygame.image.load('veneno.png')
soga_image = pygame.image.load('soga.png')

# Escala las imágenes de los objetos
object_height = 40  # Tamaño más pequeño para los objetos
cuchillo_image = pygame.transform.scale(cuchillo_image, (int(cuchillo_image.get_width() * (object_height / cuchillo_image.get_height())), object_height))
veneno_image = pygame.transform.scale(veneno_image, (int(veneno_image.get_width() * (object_height / veneno_image.get_height())), object_height))
soga_image = pygame.transform.scale(soga_image, (int(soga_image.get_width() * (object_height / soga_image.get_height())), object_height))

# Definir las habitaciones con sus posiciones aproximadas en el mapa (x, y)
rooms = {
    "Conservatory": (50, 50),
    "Ballroom": (250, 50),
    "Kitchen": (450, 50),
    "Billiard Room": (50, 250),
    "Library": (250, 250),
    "Dining Room": (450, 250),
    "Study": (50, 500),
    "Hall": (250, 450),
    "Lounge": (450, 500)
}

# Asignar personajes a habitaciones aleatorias
characters = {
    "Juan": juan_image,
    "Maria": maria_image,
    "Pedro": pedro_image
}
character_positions = {}

# Asigna una posición aleatoria de las habitaciones a cada personaje
for character in characters.keys():
    room_name, position = random.choice(list(rooms.items()))
    character_positions[character] = position
    del rooms[room_name]  # Evita que dos personajes estén en la misma habitación

# Asignar objetos a habitaciones aleatorias (sin repetir)
objects = {
    "Cuchillo": cuchillo_image,
    "Veneno": veneno_image,
    "Soga": soga_image
}
object_positions = {}

for obj in objects.keys():
    room_name, position = random.choice(list(rooms.items()))
    object_positions[obj] = position
    del rooms[room_name]  # Evita que dos objetos estén en la misma habitación

# Función principal del juego
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibuja el mapa en la pantalla
        screen.blit(map_image, (0, 0))

        # Dibuja los personajes con borde amarillo en las posiciones asignadas
        for character, position in character_positions.items():
            # Dibuja el borde amarillo alrededor del personaje
            pygame.draw.rect(screen, (255, 255, 0), (*position, character_height, character_height), 3)
            # Dibuja el personaje
            screen.blit(characters[character], position)

        # Dibuja los objetos con borde rojo en las posiciones asignadas
        for obj, position in object_positions.items():
            # Dibuja el borde rojo alrededor del objeto
            pygame.draw.rect(screen, (255, 0, 0), (*position, object_height, object_height), 3)
            # Dibuja el objeto
            screen.blit(objects[obj], position)

        # Actualiza la pantalla
        pygame.display.flip()

# Ejecuta el juego
main()
