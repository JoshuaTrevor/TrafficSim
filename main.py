import pygame, sys
import roads
import time
from pygame.locals import *

def main():

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    #pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

    
    
    

    # Draw a road between each connected node
    for nd in roads.nodes.keys():
        for connection in roads.nodes[nd].connections:
            drawRoad(nd, connection, 5)

    timePassed = 0
    while True:
        timePassed += clock.tick()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or timePassed > 20:
                #timePassed = 0
                roads.generateConnectedNode(1200, 800, 100, 100)
        
        if len(roads.nodes.keys()) < roads.maxNodes:
            for nd in roads.nodes.keys():
                for connection in roads.nodes[nd].connections:
                    drawRoad(nd, connection, 25)
        
        pygame.display.update()

# Draw connection between two nodes horizontally or vertically
def drawRoad(nodeA, nodeB, roadWidth):
    posNodeA = roads.nodes[nodeA].position
    posNodeB = roads.nodes[nodeB].position

    roadAxis = -1
    # Get road direction (perpendicular to axis of shared dimension)
    if posNodeA[0] == posNodeB[0]:
        roadAxis = 1
    elif posNodeA[1] == posNodeB[1]:
        roadAxis = 0

    else:
        print("Error: Two nodes are not aligned but are connected")
        return
    
    # Draw vertical roads
    if roadAxis == 1:
        left = posNodeA[0] - roadWidth/2
        top = min(posNodeA[1], posNodeB[1]) - roadWidth/2
        width = roadWidth
        height = abs(posNodeA[1] - posNodeB[1]) + roadWidth
        
       
    # Draw horizontal roads
    else:
        left = min(posNodeA[0], posNodeB[0]) - roadWidth/2
        top = posNodeA[1] - roadWidth/2
        width = abs(posNodeA[0] - posNodeB[0]) + roadWidth
        height = roadWidth
        
        
    #print("results: " + str(nodeA) + "," + str(nodeB) + "---" + str((left, top, width, height)))
    #pygame.draw.rect(DISPLAY, (0, 0, 0), (c1,c3,c2,c4))
    pygame.draw.rect(DISPLAY, (0, 0, 0), (left, top, width, height))



pygame.init()
clock = pygame.time.Clock()
DISPLAY=pygame.display.set_mode((1200,800),0,32)
main()