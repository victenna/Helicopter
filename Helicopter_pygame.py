import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 1300, 800
ground_level = screen_height - 150  # Ground level for divers and helicopter
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Helicopter and Divers Animation")

# Load images
background_image = pygame.image.load('road.gif')
helicopter_images = [pygame.image.load('helicopter11.gif'), pygame.image.load('helicopter12.gif')]
helicopter_images_alt = [pygame.image.load('helicopter21.gif'), pygame.image.load('helicopter22.gif')]
diver_images = [
    pygame.image.load('boy.gif'),
    pygame.image.load('boy1.gif'),
    pygame.image.load('boy2.gif'),
    pygame.image.load('boy3.gif'),
    pygame.image.load('girl.gif')
]

# Initialize helicopter and divers
helicopter = {"pos": [screen_width // 2, 200], "dir": [1, 0], "frame": 0, "state": "flying", "rounds": 0}
divers = [{"pos": [0, 280], "visible": False, "image_index": i} for i in range(len(diver_images))]
all_divers_landed = False

# Helper functions
def update_helicopter_position(heli):
    if heli["state"] == "flying":
        heli["pos"][0] += 5 * heli["dir"][0]
        if heli["pos"][0] >= 480:
            heli["dir"][0] = -1
            heli["rounds"] += 0.5
        elif heli["pos"][0] <= -480:
            heli["dir"][0] = 1
            heli["rounds"] += 0.5

        if heli["rounds"] >= 2 and all_divers_landed:
            heli["state"] = "landing"
    elif heli["state"] == "landing":
        if heli["pos"][1] < ground_level:
            heli["pos"][1] += 5

def draw_helicopter(heli):
    frame = heli["frame"] % 2
    image = helicopter_images[frame] if heli["dir"][0] > 0 else helicopter_images_alt[frame]
    heli["frame"] += 1
    screen.blit(image, (heli["pos"][0] + screen_width // 2 - image.get_width() // 2, heli["pos"][1]))

def update_divers():
    global all_divers_landed
    all_divers_landed = True
    for diver in divers:
        if diver["visible"] and diver["pos"][1] < ground_level:
            diver["pos"][1] += 5
        if diver["pos"][1] < ground_level:
            all_divers_landed = False

def draw_divers():
    for diver in divers:
        if diver["visible"]:
            image = diver_images[diver["image_index"]]
            screen.blit(image, (diver["pos"][0] + screen_width // 2 - image.get_width() // 2, diver["pos"][1]))

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for diver in divers:
                if not diver["visible"]:
                    diver["visible"] = True
                    diver["pos"] = [helicopter["pos"][0], helicopter["pos"][1]]
                    break

    # Update logic
    update_helicopter_position(helicopter)
    update_divers()

    # Clear screen and draw
    screen.fill((139, 69, 19))  # Brown background
    screen.blit(background_image, (0, 0))
    draw_helicopter(helicopter)
    draw_divers()

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
