import pygame
import sys
import random
from sympy.logic.boolalg import Or, Not, And
from sympy import symbols
from base_conocimientos2 import crear_base_conocimientos

def check_all(knowledge, query, symbols, model):
    if not symbols:
        if knowledge.subs(model):
            return query.subs(model)
        return True
    else:
        remaining = symbols.copy()
        p = remaining.pop()

        model_true = model.copy()
        model_true[p] = True

        model_false = model.copy()
        model_false[p] = False

        return (
            check_all(knowledge, query, remaining, model_true) and
            check_all(knowledge, query, remaining, model_false)
        )

def deducir(kb, asesinos, lugares, armas):
    model = {}
    symbols = asesinos + lugares + armas

    for asesino in asesinos:
        for lugar in lugares:
            for arma in armas:
                test_model = {
                    asesino: True,
                    lugar: True,
                    arma: True
                }

                for other_asesino in asesinos:
                    if other_asesino != asesino:
                        test_model[other_asesino] = False
                for other_lugar in lugares:
                    if other_lugar != lugar:
                        test_model[other_lugar] = False
                for other_arma in armas:
                    if other_arma != arma:
                        test_model[other_arma] = False

                print(f"probando combinacion: {asesino}, {lugar}, {arma}")

                if check_all(And(*kb), And(asesino, lugar, arma), symbols, test_model):
                    return asesino, lugar, arma

    return None, None, None

def ejecutar_grafico(asesino, lugar, arma):
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("clue game")
    map_image = pygame.image.load('clue.png')
    aspect_ratio = map_image.get_width() / map_image.get_height()
    new_width = int(height * aspect_ratio)
    map_image = pygame.transform.scale(map_image, (new_width, height))

    juan_image = pygame.image.load('juan.png')
    maria_image = pygame.image.load('maria.png')
    pedro_image = pygame.image.load('pedro.png')

    character_height = 50
    juan_image = pygame.transform.scale(juan_image, (int(juan_image.get_width() * (character_height / juan_image.get_height())), character_height))
    maria_image = pygame.transform.scale(maria_image, (int(maria_image.get_width() * (character_height / maria_image.get_height())), character_height))
    pedro_image = pygame.transform.scale(pedro_image, (int(pedro_image.get_width() * (character_height / pedro_image.get_height())), character_height))

    cuchillo_image = pygame.image.load('cuchillo.png')
    veneno_image = pygame.image.load('veneno.png')
    soga_image = pygame.image.load('soga.png')

    object_height = 40
    cuchillo_image = pygame.transform.scale(cuchillo_image, (int(cuchillo_image.get_width() * (object_height / cuchillo_image.get_height())), object_height))
    veneno_image = pygame.transform.scale(veneno_image, (int(veneno_image.get_width() * (object_height / veneno_image.get_height())), object_height))
    soga_image = pygame.transform.scale(soga_image, (int(soga_image.get_width() * (object_height / soga_image.get_height())), object_height))

    rooms = {
        "conservatory": (50, 50),
        "ballroom": (250, 50),
        "kitchen": (450, 50),
        "billiard room": (50, 250),
        "library": (250, 250),
        "dining room": (450, 250),
        "study": (50, 500),
        "hall": (250, 450),
        "lounge": (450, 500)
    }

    characters = {
        "juan": juan_image,
        "maria": maria_image,
        "pedro": pedro_image
    }
    character_positions = {}

    for character in characters.keys():
        room_name, position = random.choice(list(rooms.items()))
        character_positions[character] = position
        del rooms[room_name]

    objects = {
        "cuchillo": cuchillo_image,
        "veneno": veneno_image,
        "soga": soga_image
    }
    object_positions = {}

    for obj in objects.keys():
        room_name, position = random.choice(list(rooms.items()))
        object_positions[obj] = position
        del rooms[room_name]

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(map_image, (0, 0))

        for character, position in character_positions.items():
            pygame.draw.rect(screen, (255, 255, 0), (*position, character_height, character_height), 3)
            screen.blit(characters[character], position)

        for obj, position in object_positions.items():
            pygame.draw.rect(screen, (255, 0, 0), (*position, object_height, object_height), 3)
            screen.blit(objects[obj], position)

        result_text = f"asesino: {asesino}, lugar: {lugar}, arma: {arma}"
        text_surface = font.render(result_text, True, (255, 255, 255))
        screen.blit(text_surface, (20, 550))

        pygame.display.flip()

def main():
    kb, asesinos, lugares, armas = crear_base_conocimientos()
    asesino, lugar, arma = deducir(kb, asesinos, lugares, armas)

    if asesino and lugar and arma:
        print(f"solucion encontrada: asesino: {asesino}, lugar: {lugar}, arma: {arma}")
    else:
        print("no se pudo determinar el asesino, lugar y arma con la informacion actual")

    ejecutar_grafico(asesino, lugar, arma)

if __name__ == "__main__":
    main()
