import pgzrun
from pgzhelper import *
WIDTH = 800
HEIGHT = 600

runner = Actor("a0",(100,300))
runnerLeft = Actor("b0")
runner.images = ["a0","a1","a2","a3","a4","a5"]

flagRunner = True

runnerLeft.images = ["b0","b1","b2","b3","b4","b5"]
def update():
    
    global flagRunner
    
    if keyboard.right:
        runner.flip_x = False
        runner.animate()
        runner.x += 1
        flagRunner = True
        runnerLeft.x = runner.x
        runnerLeft.y = runner.y
        
    else:
        runner.image = "a0"
        flagRunner = True

    if keyboard.left:
        flagRunner = False
        runnerLeft.animate()
        runnerLeft.x -= 1
        runner.x = runnerLeft.x 
        runner.y = runnerLeft.y 

def draw():
    global flagRunner
    screen.fill("dim gray")
    if flagRunner:
        runner.draw()
    else:
        runnerLeft.draw()    



pgzrun.go()