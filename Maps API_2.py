import os
import sys
import pygame
import requests

pygame.init()
screen = pygame.display.set_mode((650, 450))
pygame.display.set_caption('Maps API')

ll = [47.9, 46.2]
params = {"ll": ",".join([str(el) for el in ll]),
          "z": 16,
          "l": "map",
          "size": ",".join(["650", "450"])
          }



def terminate():
    pygame.quit()
    sys.exit()


def map():
    global params, ll
    params["ll"] = ",".join([str(el) for el in ll])
    api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(api_server, params=params)
    try:
        with open("map.png", "wb") as file:
            file.write(response.content)
    except IOError:
        print("Ошибка")
        sys.exit(2)
    return "map.png"


def main():
    global params, ll
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove(map_file)
                terminate()
            if pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
                if params["z"] > 2:
                    params["z"] -= 1
            if pygame.key.get_pressed()[pygame.K_PAGEUP]:
                if params["z"] < 19:
                    params["z"] += 1
        screen.fill("Black")
        map_file = map()
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
