import os
import time
import pygame.camera
import pygame.image
import sys

time.sleep(1)
bufferSize = 100;
PATH = "./my_program.fifo";  
pipe = os.open(PATH, os.O_RDONLY);

pygame.camera.init()
cameras = pygame.camera.list_cameras()
facecam = pygame.camera.Camera(cameras[0])
notecam = pygame.camera.Camera(cameras[1])

facecam.start()
notecam.start()
button_status = 2
while True :
    faceimg = facecam.get_image()
    noteimg = notecam.get_image()
    input = os.read(pipe,bufferSize);

    if(input == "1\n" or input == "2\n"):
		button_status = int(input.split("\n")[0])
	
    if(button_status == 1):
    	data = pygame.image.tostring(faceimg, 'RGB')

    elif(button_status == 2):
    	smallfaceimg = pygame.transform.scale(faceimg, (160, 120)) 
    	flippednoteimg = pygame.transform.flip(noteimg, 1, 1)
    	flippednoteimg.blit(smallfaceimg, (480,0))
    	data = pygame.image.tostring(flippednoteimg, 'RGB')
    sys.stdout.write(data)