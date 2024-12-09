class BlockFile:
    def __init__(self, start, size, ID=-1):
        self.ID = ID
        self.start = start
        self.size = size

    def getPrint(self):
        if self.ID == -1:
            return "."
        else:
            return str(self.ID)
     

    def getChecksum(self):
        if self.ID == -1:
            return 0
        res = 0
        for i in range(self.start, self.start + self.size):
            res += self.ID * i
        return res


class Disk:
    def __init__(self):
        self.files = []

    def addFileToMemory(self, file):
        self.files.append(file)

    def pushFilesBack(self):
        for file in self.files[::-1]:
            if file.ID == -1:
                continue
            else:
                for emptySpace in self.files:
                    if emptySpace.ID != -1 or emptySpace.start > file.start:
                        continue
                    if file.size <= emptySpace.size:
                        newEmptySpace = BlockFile(file.start,file.size)
                        file.start = emptySpace.start
                        emptySpace.start = emptySpace.start + file.size
                        emptySpace.size = emptySpace.size - file.size
                        self.addFileToMemory(newEmptySpace)
                        break
                            

    def getFileChecksum(self):
        checksum = 0
        for file in self.files:
            print(file.ID, end="")
            print(f" {file.locations}", end="")
            for loc in file.locations:
                checksum += loc * int(file.ID)
            print()
        return checksum
    
    def printMemoryAllocation(self):
        diskSize = 1
        for file in self.files:
            print(f"File {file.ID} - size {file.size} - start {file.start}")
            diskSize+= file.size
        memory = ["."] * diskSize
        for file in self.files:
            if(file.size == 0):
                continue
            for i in range(file.start,file.start+file.size):
                
                memory[i] = file.getPrint()
        
        print("".join(memory))
        
    def getFileChecksum(self):
        res = 0
        for file in self.files:
            res+= file.getChecksum()
            
        return res


f = open("./advent-of-code/day9/input.txt", "r")


freeSpace = False
fileID = 0
fileStartIndex = 0
disk = Disk()
while 1:

    # read by character
    char = f.read(1)
    if not char:
        break
    if int(char) == 0:
        freeSpace = not freeSpace
        continue
    if not freeSpace:

        currentFile = BlockFile(fileStartIndex, int(char), fileID)
        fileID += 1
    else:
        currentFile = BlockFile(fileStartIndex, int(char))

    disk.addFileToMemory(currentFile)

    freeSpace = not freeSpace

    fileStartIndex += int(char)

disk.pushFilesBack()

print(disk.getFileChecksum())
#6467290489134
#6467290489134
#6467290923294