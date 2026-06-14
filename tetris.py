import pygame
import random


def addBlocks(newBlocks):
    print(newBlocks)
    for i in newBlocks:
        cells[i[0]][i[1]] = 1


def manipulateBlocksHoriz(blocks, factor):
    returnBlocks = []
    returnOriginal = False
    for i in range(0, len(blocks)):
        returnBlocks.append([blocks[i][0], blocks[i][1] + factor])
        if((blocks[i][1] + factor) < 0 or (blocks[i][1] + factor) > 9):
            returnOriginal = True
            break

    return returnBlocks if not returnOriginal else blocks

def generateNewO():
    returnBlocks = []
    x = random.randrange(0,9)
    for i in range(0,2):
        returnBlocks.append([i, x])
        returnBlocks.append([i, x+1])
    return returnBlocks

pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True
rect_pos = [screen.get_width()/2, screen.get_height()/2]
rect_size = 20
dt = 0
timer = 0

cells = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


newblocks = [
    [0,4],
    [0,5],
    [1,4],
    [1,5]
]

while running:
    screen.fill("purple")
    for row_index, row in enumerate(cells):
        y = row_index*40
        for col_index, col in enumerate(row):
            x = col_index*40
            if(col == 1):
                pygame.draw.rect(screen, "red", (x, y, 40, 40))
    

    
    bottom = 0
    for i in newblocks:
        y=i[0]*40
        x=i[1]*40
        pygame.draw.rect(screen, "red", (x, y, 40, 40))


    timer += dt

    if timer > 0.5:

        should_lock = False

        for block in newblocks:
            if block[0] + 1 > 19:
                should_lock = True
                break

        if should_lock:
            addBlocks(newblocks)
            newblocks = generateNewO()
        else:
            for block in newblocks:
                block[0] += 1

        timer = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key==pygame.K_LEFT:
                newblocks = manipulateBlocksHoriz(newblocks, -1)
            elif event.key == pygame.K_d or event.key==pygame.K_RIGHT:
                newblocks = manipulateBlocksHoriz(newblocks, 1)


    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
