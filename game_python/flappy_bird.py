"""
Developed by Pragati Sahu
Youtube Channel link
https://www.youtube.com/channel/codeatrandom/
"""
from ursina import *
import random as r
app = Ursina()
Sky()
bird = Animation('assests\img',
                collider='box',
                scale=(2,2,2),
                y=5)
camera.orthographic = True
camera.fov =20
def update():
    # Update bird's position
    bird.y = bird.y - 4*time.dt

    # Update pipes' positions
    for p in pipes:
        p.x = p.x - 2*time.dt

    # Check for collision
    touch = bird.intersects()

    # If collision or bird out of screen, quit game
    if touch.hit or bird.y < -10:
        quit()

def input(key):
    # Check if the key is space
    if key == 'space':
        # Increment the bird's y position by 3
        bird.y += 3

#Pipe specification
pipes = []
pipe = Entity(model="quad", 
             color =color.green, 
            texture ='white_cube', 
            position=(20,10), 
            scale=(3,15,1), 
            collider = 'box')

def newPipe():
    # Randomly generate the height of the pipe
    y = r.randint(4, 12)
    
    # Duplicate the pipe and set its height
    new1 = duplicate(pipe, y=y)
    
    # Duplicate the pipe again and set its height to be 
    # 22 less than the first pipe
    new2 = duplicate(pipe, y=y-22)
    
    # Add the new pipes to the list of pipes
    pipes.extend((new1, new2))
    
    # Call the newPipe function again after a delay of 5 seconds
    invoke(newPipe, delay=5)
newPipe()
app.run()