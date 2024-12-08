class AntennaCluster:
    def __init__(self, ID):
        self.id = ID
        self.antennae = []
        self.rangeX = 0
        self.rangeY = 0
        self.antinodes = []

    def addAntennae(self, antennaeObject):
        self.antennae.append(antennaeObject)

    def pingAntennaes(self, rangeX, rangeY):
        self.rangeX = rangeX
        self.rangeY = rangeY
        for idxCurrent, currentAntennae in enumerate(self.antennae[0:-1]):
            for idxOther, otherAntennae in enumerate(self.antennae[idxCurrent + 1 :]):
                firstLoc = currentAntennae.ping()
                secondLoc = otherAntennae.ping()

                firstAntinode = Antinode(
                    firstLoc[0],
                    firstLoc[1],
                    currentAntennae.X - otherAntennae.X,
                    currentAntennae.Y - otherAntennae.Y,
                )
                while firstAntinode.propagate(rangeX, rangeY):
                    pass

                self.antinodes.append(firstAntinode)

                secondAntinode = Antinode(
                    secondLoc[0],
                    secondLoc[1],
                    otherAntennae.X - currentAntennae.X,
                    otherAntennae.Y - currentAntennae.Y,
                )
                while secondAntinode.propagate(rangeX, rangeY):
                    pass
                self.antinodes.append(secondAntinode)


class Antinode:
    def __init__(self, X, Y, distanceX, distanceY):
        self.X = X
        self.Y = Y
        self.distanceX = distanceX
        self.distanceY = distanceY
        self.locations = [[self.X, self.Y]]
        self.propagated = False
        pass

    def propagate(self, rangeX, rangeY):
        self.X += self.distanceX
        self.Y += self.distanceY
        if self.X < 0 or self.X > rangeX or self.Y < 0 or self.Y > rangeY:
            return False


        if(not self.propagated):
            self.propagated = True
        self.locations.append([self.X, self.Y])
        return True


class Antennae:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        pass

    def ping(self):
        return [self.X, self.Y]


f = open("./advent-of-code/day8/input.txt", "r")

clusters = []
height = 0
for idxY, line in enumerate(f.readlines()):
    for idxX, character in enumerate(line):
        if character == "." or character == "\n":
            continue
        else:
            newAntennae = Antennae(idxX, idxY)

            clusterFound = False
            for cluster in clusters:
                if cluster.id == character:
                    currentCluster = cluster
                    clusterFound = True
                    break

            if clusterFound:
                cluster.addAntennae(newAntennae)
            else:
                currentCluster = AntennaCluster(character)
                currentCluster.addAntennae(newAntennae)
                clusters.append(currentCluster)
    height += 1
width = len(line) - 1
height = height - 1

allLocations = []
singleLocations = []

cnt = 0
for cluster in clusters:
    cluster.pingAntennaes(width, height)

    for antinode in cluster.antinodes:
        for loc in antinode.locations:
            allLocations.append(loc)
            
        if(antinode.propagated):
            singleLocations.append(antinode.locations[1])


print(len(list(set(map(tuple,singleLocations)))))
print(len(list(set(map(tuple,allLocations)))))
