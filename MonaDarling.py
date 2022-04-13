
import pygame
import random
import numpy as np

img = pygame.image.load("monalisa.jpg")

pygame.init()
screen = pygame.display.set_mode((600,600))

for i,x in enumerate(range(0,600,200)):
    for j,y in enumerate(range(0,600,200)):
        Rect = (x, y, 200, 200)
        img1 = img.subsurface(Rect)
        pygame.image.save(img1,str(i*3+j)+'.jpg')

list1 = [i for i in range(-1, 8 , 1)]

# random.shuffle(list1)

arr = np.reshape(list1, (3, 3))

imagesDict = {}

for i in range(9):
       imagesDict[i] = pygame.image.load(str(i)+'.jpg')

def isEndGame():
    endArray = np.reshape(arr, (9,))
    

def show():
    for i,x in enumerate(range(0,600,200)):
        for j,y in enumerate(range(0,600,200)):
            if (arr[i,j] == -1):
                continue
            screen.blit(imagesDict[arr[i,j]], (x, y))

def isValid(i: int, j: int) -> bool:
    rows, cols = arr.shape
    return i in range(rows) and j in range(cols)
    

running = True
while(running):
    screen.fill((0, 0, 0))
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                a,b = np.where(arr == -1)
                if(isValid(a,b+1)):
                    temp = arr[a,b]
                    arr[a,b] = arr[a,b+1]
                    arr[a,b+1] = temp
                          
            elif keys[pygame.K_DOWN]:
                a,b = np.where(arr == -1)
                if(isValid(a,b-1)):
                    temp = arr[a,b]
                    arr[a,b] = arr[a,b-1]
                    arr[a,b-1] = temp
                
            elif keys[pygame.K_LEFT]:
                a,b= np.where(arr == -1)
                if(isValid(a+1,b)):
                    temp = arr[a,b]
                    arr[a,b] = arr[a+1,b]
                    arr[a+1,b] = temp
                
            elif keys[pygame.K_RIGHT]:
                a,b = np.where(arr == -1)
                if(isValid(a-1,b)):
                    temp = arr[a,b]
                    arr[a,b] = arr[a-1,b]
                    arr[a-1,b] = temp
                
    show()      
    pygame.display.update()