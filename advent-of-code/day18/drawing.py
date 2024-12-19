import cv2
import numpy as np

class Color:
    NLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

def drawField(line):
    
    pr = ''
    for char in line:

        if char == '':
            pr += f"{Color.GREEN}{char}{Color.ENDC}"
            #print(char, end="")
        elif char == '3':
            pr += f"{Color.GREEN}O{Color.ENDC}"
            #print(pr, end="")
        elif char == '1':
            pr += f"{Color.CYAN}#{Color.ENDC}"
            #print(pr, end="")
        elif char == '2':
            pr += f"{Color.RED}X{Color.ENDC}"
            #print(pr, end="")
        else:
            pr += f"{Color.CYAN}.{Color.ENDC}"
            #print(pr, end="")
    
    print(pr)
def drawField(line):
    
    pr = ''
    for char in line:

        if char == '':
            pr += f"{Color.GREEN}{char}{Color.ENDC}"
            #print(char, end="")
        elif char == '3':
            pr += f"{Color.GREEN}O{Color.ENDC}"
            #print(pr, end="")
        elif char == '1':
            pr += f"{Color.CYAN}#{Color.ENDC}"
            #print(pr, end="")
        elif char == '2':
            pr += f"{Color.RED}X{Color.ENDC}"
            #print(pr, end="")
        else:
            pr += f"{Color.CYAN}.{Color.ENDC}"
            #print(pr, end="")
    
    print(pr)
    


def putTextOnImage(image,text,alignLeft = True):
    image_width = image.shape[1]
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    fontpath = "./advent-of-code/day18/terminal2.otf"     
    font = ImageFont.truetype(fontpath, 32)

    # Calculate the position: center horizontally and vertically within the 50px
    if alignLeft:
        text_x = 20
    else: 
        text_x = image_width // 2 + 70
        
    text_y = 20  # Align vertically in the 50px space

      
    draw.text((text_x, text_y),text,(200),font=font)
    
    return np.array(image)
  
FIELD_SIZE = 71
SCALE = 14
PADDING = 80
from PIL import Image, ImageFont, ImageDraw




images = []
with open("./advent-of-code/day18/visual.txt", "r") as file:

    fieldImage = []
 
    for line in file:
        line = line.strip()
        if line[0] =='-':
            index, pathLength, addedObstacle = [el for el in line.split('.') if el != '-']
      
    
            index = int(index)
            pathLength = int(pathLength)
            
            finalImage = np.array(fieldImage,dtype=np.uint8)
            finalImage = cv2.resize(finalImage, (FIELD_SIZE * SCALE, FIELD_SIZE * SCALE),interpolation=cv2.INTER_NEAREST) 
            finalImage = finalImage * (255//3)
            finalImage = np.pad(finalImage, [(PADDING, 0), (0, 0)], mode='constant', constant_values=0)
           
            finalImage = putTextOnImage(finalImage,f"Length: {pathLength}",False)
            finalImage = putTextOnImage(finalImage,f"Obstacle: {index}")
            
            images.append(finalImage)
            fieldImage = []
            continue
        
        lineArray = []
        for char in line:
            lineArray.append(int(char))
        fieldImage.append(lineArray)
      



fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out= cv2.VideoWriter("./advent-of-code/day18/visual.avi",fourcc,24,(FIELD_SIZE*SCALE,FIELD_SIZE*SCALE+PADDING),isColor=True) 
print(images[0].shape)
for idx,image in enumerate(images):
    #print("enum")
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
    B = image[:,:,0]
    G = image[:,:,1]
    R = image[:,:,2]
    if idx == len(images) - 1:
    
        B[B == 255] = 20
        G[G == 255] = 20
        R[R == 255] = 175
    else:
        B[B == 255] = 20
        G[G == 255] = 175
        R[R == 255] = 20

    #print(f"{(FIELD_SIZE*SCALE+PADDING,FIELD_SIZE*SCALE)} , img : {image.shape}")
    out.write(image)

for i in range(0,50):
    out.write(image)

out.release()