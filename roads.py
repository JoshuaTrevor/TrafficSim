# System of roads as graph of nodes.
# Each node is mapped to a location, a set of other nodes and whether there is a traffic light at that node. (or other give way rules)
# Traffic light can be for each incoming edge a circle with a colour. So four way intersection has four traffic lights
# representing the colour faced by people at that road into the intersection.

#Load these from a file later so I can do things like have a road editor or at least not look as hacky
import time


import random

maxNodes = 112

class node:
    def __init__(self, position, connections, trafficLights):
        self.position = position
        self.connections = connections
        self.trafficLights = trafficLights

nodes = {
    0 : node((100, 100), [1, 2], False),
    1 : node((200, 100), [0], False),
    2 : node((100, 200), [0], False),
}

def generateConnectedNode(maxX, maxY, minLength, maxLength):
    maxTries = 100
    tries = 0
    newIndex = max(nodes.keys()) + 1
    length = minLength

    while(tries < maxTries):
        tries = tries + 1

        # Select random node
        foundNode = random.randrange(0, len(nodes.keys()))
        if len(nodes[foundNode].connections) > 3:
            continue
        #print("choosing node " + str(foundNode))

        # Select random direction
        directionAxis = random.randint(0, 1) # 0 or 1
        direction = (random.randint(0, 1) * 2) - 1 # -1 or 1

        # Create test coordinates for new node in this direction
        newX = nodes[foundNode].position[0] + (direction * length) if directionAxis == 0 else nodes[foundNode].position[0] 
        newY = nodes[foundNode].position[1] + (direction * length) if directionAxis == 1 else nodes[foundNode].position[1] 

        if newX > maxX or newY > maxY or newX < 0 or newY < 0:
            continue

        # Check if this node already exists
        exists = False
        
        #start = time.time()
        for ndKey in nodes.keys():
            if nodes[ndKey].position[0] == newX and nodes[ndKey].position[1] == newY:
                #print("This node already exists!")
                exists = True
        #print(time.time() - start)

        if exists:
            continue

        break


    if tries == maxTries:
        return
    
    nodes[newIndex] = node( (newX, newY), [foundNode], False )
    nodes[foundNode].connections.append(newIndex)
    # Work out which nodes this should be connected to and update their connected node values

