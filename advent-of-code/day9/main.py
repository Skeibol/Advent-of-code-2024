class File:
    def __init__(self, ID):
        self.ID = ID
        self.locations = []

    def setDiskLocations(self, start, end):
        for i in range(start, end):
            self.locations.append(i)


class Disk:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size
        self.files = []

    def addFileToMemory(self, file):
        self.files.append(file)
        for i in file.locations:
            self.memory[i] = file.ID

    def writeToAvailableMemory(self, file):
        newLocations = []
        
        for i, fileLocation in enumerate(file.locations[::-1]):
            for j, memoryLocation in enumerate(self.memory):
                if j > fileLocation:
                    newLocations.append(fileLocation)
                    break
                if memoryLocation is None:
                    if(file.ID == 6):
                        print(f"Setting file 6 - {file.locations[i]} to {j}")
                    self.memory[j] = file.ID
                    self.memory[fileLocation] = None
                    newLocations.append(j)
                    break
        file.locations = newLocations

    def getDiskSpace(self):
        space = 0
        for i in self.memory:
            if i is None:
                space += 1
        return space

    def getFileChecksum(self):
        checksum = 0
        for file in self.files:
            print(file.ID, end="")
            print(f" {file.locations}", end="")
            for loc in file.locations:
                checksum += loc * int(file.ID)
            print()
        return checksum
    
    def printDiskSpace(self):
        for memoryLocation in self.memory:
            if memoryLocation is None:
                print(".", end="")
            else:
                print(memoryLocation, end="")


f = open("./advent-of-code/day9/input.txt", "r")
fileID = 0
diskIdx = 0
diskSegments = []
diskSize = 0

while 1:

    # read by character
    char = f.read(1)
    if not char:
        break
    diskSegments.append(char)
    diskSize += int(char)


disk = Disk(diskSize)


for idx, seg in enumerate(diskSegments):
    if idx % 2 == 0:
        diskIdxEnd = diskIdx + int(seg)
        currentFile = File(fileID)
        currentFile.setDiskLocations(diskIdx, diskIdxEnd)
        disk.addFileToMemory(currentFile)
        diskIdx = diskIdxEnd
        fileID += 1
    else:
        diskIdx += int(seg)

spaceToWrite = disk.getDiskSpace()
initSpace = disk.getDiskSpace()
for file in disk.files[::-1]:
    disk.writeToAvailableMemory(file)
    spaceToWrite -= len(file.locations)
    print(f"{spaceToWrite} / {initSpace} complete")
    if spaceToWrite <= 0:
        break
    

print(disk.getFileChecksum())
f.close()
