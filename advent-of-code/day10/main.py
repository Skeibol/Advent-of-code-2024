import numpy as np
class Node():
    def __init__(self,X,Y,parent=None):
        self.X = X
        self.Y = Y
        self.parent = parent
        self.locations = []
        
    def signalEndPosition(self):
        currentNode = self
        while currentNode.parent is not None:
            currentNode = currentNode.parent
        
        #if [self.X,self.Y] not in currentNode.locations:
        currentNode.locations.append([self.X,self.Y])


def lookAdjacentPositions(terrain,node,depth):

    height , width = terrain.shape
    currentLocation = terrain[node.Y,node.X]
    if(currentLocation == depth):
        if depth == 9:
            node.signalEndPosition()  
        if(node.X - 1 >= 0):
            leftNode = Node(node.X - 1, node.Y,node)
            lookAdjacentPositions(terrain,leftNode,depth + 1)
        if(node.X + 1 < width):
            rightNode = Node(node.X + 1, node.Y,node)
            lookAdjacentPositions(terrain,rightNode,depth + 1)
        if(node.Y - 1 >= 0):
            upNode = Node(node.X, node.Y - 1,node)
            lookAdjacentPositions(terrain,upNode,depth + 1)
        if(node.Y + 1 < height):
            downNode = Node(node.X, node.Y + 1,node)
            lookAdjacentPositions(terrain,downNode,depth + 1)

    
f = open("./advent-of-code/day10/input.txt", "r")
# Open the file in read mode
row = []
terrain = []
with open("./advent-of-code/day10/input.txt", "r") as file:
    # Read each line in the file
    for line in file:
        for char in line:
            if(char == '\n'):
                continue
            if(char == '.'):
                row.append(-1)
                continue
            row.append(int(char))
        terrain.append(row)
        row = []

cnt = 0
terrainArray = np.array(terrain)
for idxCol,col in enumerate(terrainArray):
    for idxLocation,location in enumerate(col):

        if(location == 0):
            currentLocationNode = Node(idxLocation,idxCol)
            lookAdjacentPositions(terrainArray,currentLocationNode,0)
            cnt += len(currentLocationNode.locations)

print(cnt)