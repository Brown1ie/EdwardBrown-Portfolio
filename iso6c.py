import pyjsdl as pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()

def load_images():
    try:
        cross = pygame.image.load('assets/crosshair3.png')
        cross = pygame.transform.scale(cross, (16,16))
        icon_img = pygame.image.load('assets/bluetriangle.png')
        icon_img.set_colorkey((0, 0, 0))
        water = pygame.image.load('assets/water.png')
        water.set_colorkey((0, 0, 0))
        return True
    except Exception as e:
        print(f"Error loading images: {e}")
        return False

def Main(display, clock):
    global LCscore, RCscore, GrassActive, StoneActive, SandActive
    global GREENGO, GREYGO, YELLOWGO
    
    world = pygame.Surface((2000,2000))
    world.fill(colors["BLACK"])
    
    if not load_images():
        print("Failed to load images")
        return

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.blit(world, camera_pos)
        textbox.draw(display)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    display = pygame.display.set_mode((500,500))
    pygame.display.set_caption("WorldSpawner")
    
    colors = {
        "WHITE": (255,255,255),
        "RED": (255,0,0),
        "GREEN": (0,255,0),
        "BLUE": (0,0,255),
        "GREY": (128,128,128),
        "YELLOW": (255,255,0),
        "BLACK": (0,0,0),
        "LIGHTBLUE": (44,87,93),
        "DARKBLUE": (87,166,178)
    }
    
    Main(display, clock)