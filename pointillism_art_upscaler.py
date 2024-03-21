#Jessie Sellars

import sys, pygame, random

#Defining the variable var_img an image that the user inputs from a command line argument
var_img = pygame.image.load(sys.argv[1])

#Sets the variable (width, heigh) as the resolution of the image
(width, height) = var_img.get_size()

#Defining the variable var_scr1 as a pigame surface the size of (width, heigh), that is NOT the display
var_scr1 = pygame.Surface((width, height))

#Uses the blit function to draw the image var_img on the midle surface var_scr1
var_scr1.blit(var_img, (0, 0))

#Defines a second pigame window that WILL be displayed and that is 4 times biger than the first window
var_scr2 = pygame.display.set_mode((width*4, height*4))

#Using a nested for loop to visit each pixel of the image
for y in range(height):
    for x in range(width):

#Defining the variable (r, g, b, _) as the rgb values of the pixel x, y
        (r, g, b, _) = var_scr1.get_at((x, y))

#Dividing each number by 64 (255/4) because we are upscaling by a factor of 4, this will be the number of squares in that section
        r = r // 64
        g = g // 64
        b = b // 64

#Defining a for i in range loop that will repeat r times (i is not used)
        for i in range(r):
            #Draw a red square at a random x and y repective to the initial pixel
            pygame.draw.rect(var_scr2, (255, 0, 0), ((random.randint(((x-1)*4), ((x*4)-1))), (random.randint(((y-1)*4), ((y*4)-1))), 1, 1))

#Defining a for i in range loop that will repeat g times (i is not used)
        for i in range(g):
            #Draw a green square at a random x and y repective to the initial pixel
            pygame.draw.rect(var_scr2, (0, 255, 0), ((random.randint(((x-1)*4), ((x*4)-1))), (random.randint(((y-1)*4), ((y*4)-1))), 1, 1))

#Defining a for i in range loop that will repeat b times (i is not used)
        for i in range(b):
            #Draw a blue square at a random x and y repective to the initial pixel
            pygame.draw.rect(var_scr2, (0, 0, 255), ((random.randint(((x-1)*4), ((x*4)-1))), (random.randint(((y-1)*4), ((y*4)-1))), 1, 1))

#Updating the pygame window
pygame.display.update()

#Keeps the pygame window open until the user exits it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
