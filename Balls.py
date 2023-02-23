import pygame
from pygame import Surface, SurfaceType
from random import randrange

FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()

n = 5
background_height = 3 / 4 * n * 180
background_width = n * 180
slots = 18
slot_pos = 0
slot_width = background_width / 19
border_width = n
ball_radius = slot_width - 2 * n
slot_wall = 0
node_ind = 0
node_row1 = 3
node_row2 = 11
node_row3 = 11
node_row4 = 13
node_row5 = 13
node_row6 = 15
node_row7 = 15
node_row8 = 17
node_row9 = 17
node_row10 = 18

background_color = (171, 219, 227)
iron = (245, 245, 245)
bronze = (205, 127, 50)
silver = (192, 192, 192)
gold = (255, 215, 0)
amethyst = (147, 112, 219)
ruby = (224, 17, 95)
ice = (0, 191, 255)
transparent = (0, 0, 0, 0)

# Set up the drawing window
background: Surface | SurfaceType = pygame.display.set_mode([background_width, background_height])
#background2: Surface | SurfaceType = pygame.display.set_mode([background_width, background_height])

# Run until the user asks to quit
running = True

# Fill the background
background.fill(background_color)
#background2.fill(background_color)

# Draw walls for slots
wall = pygame.Surface((border_width, ball_radius))
slot = pygame.Surface((slot_width - n, ball_radius - 2))
while slot_wall <= slots:
    background.blit(wall, (slot_width / 2 + slot_width * slot_wall, background_height - ball_radius))
    slot_wall += 1

temp_slot = []
slot_coord = []
for slot_pos in range(slots):
    if slot_pos < 3:
        slot.fill(iron)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    elif 3 <= slot_pos < 7:
        slot.fill(bronze)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    elif 7 <= slot_pos < 10:
        slot.fill(silver)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    elif 10 <= slot_pos < 13:
        slot.fill(gold)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    elif 13 <= slot_pos < 15:
        slot.fill(amethyst)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    elif 15 <= slot_pos < 17:
        slot.fill(ruby)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    else:
        slot.fill(ice)
        temp_slot.append(background.blit(slot, (slot_width / 2 + n + slot_width * slot_pos, background_height - ball_radius)))
    slot_coord.append(temp_slot)
    temp_slot = []
#print(len(slot_coord))

# Draw a border
border_vertical = pygame.Surface((border_width, background_height))
border_horisontal = pygame.Surface((background_width, border_width))
background.blit(border_vertical, [0, 0])
background.blit(border_vertical, [background_width - n, 0])
background.blit(border_horisontal, [0, 0])
background.blit(border_horisontal, [0, background_height - n])

# Draw a border
border_vertical = pygame.Surface((border_width, background_height))
border_horisontal = pygame.Surface((background_width, border_width))
background.blit(border_vertical, [0, 0])
background.blit(border_vertical, [background_width - n, 0])
background.blit(border_horisontal, [0, 0])
background.blit(border_horisontal, [0, background_height - n])

# Draw nodes
node = pygame.Surface((border_width, border_width))
a = []
node_coord = []
for node_row in range(10):
    if node_row == 9:
        for node_ind in range(node_row1):
            a.append(background.blit(node, (slot_width + slot_width * node_ind,
                                            background_height - ball_radius - n * 2 - node_row * slot_width)))
    elif (node_row % 2) == 0:
        for node_ind in range(node_row10):
            a.append(background.blit(node, (slot_width / 2 + slot_width * node_ind,
                                            background_height - ball_radius - n * 2 - node_row * slot_width)))
        node_row10 -= 1
    else:
        for node_ind in range(node_row9):
            a.append(background.blit(node, (slot_width + slot_width * node_ind,
                                            background_height - ball_radius - n * 2 - node_row * slot_width)))
        node_row9 -= 1
    # print(a)
    node_coord.insert(node_row, a)
    a = []

# print(node_coord)


# Draw portals
pygame.draw.ellipse(background, bronze, (slot_width + slot_width * 3,
                                         background_height - ball_radius - n * 2 - 10 * slot_width,
                                         slot_width, slot_width / 2))
pygame.draw.ellipse(background, silver, (slot_width + slot_width * 6,
                                         background_height - ball_radius - n * 2 - 10 * slot_width,
                                         slot_width, slot_width / 2))
pygame.draw.ellipse(background, gold, (slot_width + slot_width * 9,
                                       background_height - ball_radius - n * 2 - 10 * slot_width,
                                       slot_width, slot_width / 2))
pygame.draw.ellipse(background, amethyst, (slot_width + slot_width * 12,
                                           background_height - ball_radius - n * 2 - 10 * slot_width,
                                           slot_width, slot_width / 2))


def startingPos():
    start_pos = randrange(3)
    if start_pos == 0:
        square_coord[0] = slot_width - n + 1
        square_coord[1] = slot_width
        return square_coord
    elif start_pos == 1:
        square_coord[0] = 2 * slot_width - n + 1
        square_coord[1] = slot_width
        return square_coord
    else:
        square_coord[0] = 3 * slot_width - n + 1
        square_coord[1] = slot_width
        return square_coord


# Ball form
square = pygame.Surface((ball_radius / 2 - n, ball_radius / 2 - n))
square_coord = square.get_rect()
square.fill(ice)
background.blit(square, startingPos())

speed = [0, 1]
gravity = 10


def collisionNode(num1, num2, num3):
    direction = randrange(2)
    if num2 in range(0, 10, 2) and num3 == 0:
        num1[0] += slot_width / 2
        num1 = square_coord
        return num1
    else:
        if direction == 0:
            num1[0] -= slot_width / 2
            num1 = square_coord
            return num1
        else:
            num1[0] += slot_width / 2
            num1 = square_coord
            return num1

def collisionIron(num1):
    direction = randrange(2)
    if direction == 1:
        num1[0] = slot_width / 2 + slot_width * 4 - n + 1
        num1[1] = background_height - ball_radius - n * 2 - 10 * slot_width
        num1 = square_coord
        return num1
    else:
        startingPos()

def collisionBronze(num1):
    direction = randrange(2)
    if direction == 1:
        num1[0] = slot_width / 2 + slot_width * 7 - n + 1
        num1[1] = background_height - ball_radius - n * 2 - 10 * slot_width
        num1 = square_coord
        return num1
    else:
        startingPos()

def collisionSilver(num1):
    direction = randrange(2)
    if direction == 1:
        num1[0] = slot_width / 2 + slot_width * 10 - n + 1
        num1[1] = background_height - ball_radius - n * 2 - 10 * slot_width
        num1 = square_coord
        return num1
    else:
        startingPos()

def collisionGold(num1):
    direction = randrange(2)
    if direction == 1:
        num1[0] = slot_width / 2 + slot_width * 13 - n + 1
        num1[1] = background_height - ball_radius - n * 2 - 10 * slot_width
        num1 = square_coord
        return num1
    else:
        startingPos()


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    speed[1] = gravity
    square_coord = square_coord.move(speed)
    background.blit(square, square_coord)

    if square_coord[1] >= background_height - ball_radius:
        start_pos = randrange(3)
        if start_pos == 0:
            square_coord[0] = slot_width - n + 1
            square_coord[1] = slot_width
        elif start_pos == 1:
            square_coord[0] = 2 * slot_width - n + 1
            square_coord[1] = slot_width
        else:
            square_coord[0] = 3 * slot_width - n + 1
            square_coord[1] = slot_width

    node_row1 = 3
    node_row9 = 17
    node_row10 = 18

    for node_row in range(10):
        if node_row == 9:
            for node_ind in range(node_row1):
                if square_coord.colliderect(node_coord[node_row][node_ind]):
                    # print("aa")
                    collisionNode(square_coord, node_row, node_ind)
        elif (node_row % 2) == 0:
            for node_ind in range(node_row10):
                if square_coord.colliderect(node_coord[node_row][node_ind]):
                    # print("bb")
                    collisionNode(square_coord, node_row, node_ind)
            node_row10 -= 1
        else:
            for node_ind in range(node_row9):
                if square_coord.colliderect(node_coord[node_row][node_ind]):
                    # print("cc")
                    collisionNode(square_coord, node_row, node_ind)
            node_row9 -= 1

    for slot_pos in range(slots):
        if square_coord.colliderect(slot_coord[slot_pos][0]):
            if slot_pos < 3:
                collisionIron(square_coord)
            elif 3 <= slot_pos < 7:
                collisionBronze(square_coord)
            elif 7 <= slot_pos < 10:
                collisionSilver(square_coord)
            elif 10 <= slot_pos < 13:
                collisionGold(square_coord)
            else:
                startingPos()

    # print(square_coord)

    pygame.display.update()
    fpsClock.tick(FPS)

# Done! Time to quit.
pygame.quit()
