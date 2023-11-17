import pyautogui as gui
import time
from PIL import ImageGrab
import keyboard

time.sleep(2)
foundShiny = False
resets = 0
starterCoordinate = x, y = 520, 560
enemyCoordinate = x, y = 1300, 320
starterColor = (255, 107, 57)
enemyColor = (74, 82, 99)
px = ImageGrab.grab()

with gui.hold('space'):
    while(not foundShiny):
        gui.hotkey('enter', 'backspace', 'z', 'x', interval = 0.05)
        for x in range(0, 10):
            gui.keyDown('z')
            gui.keyUp('z')
        
        px = ImageGrab.grab()
        shinyStarter = (px.getpixel(starterCoordinate) != starterColor)
        shinyEnemy = (px.getpixel(enemyCoordinate) != enemyColor)
        foundShiny = (shinyStarter or shinyEnemy)
        resets += 1
        print(resets)
        if(foundShiny):
            if(shinyStarter):
                print("Shiny Torchic!")
                print(px.getpixel(starterCoordinate))
            if(shinyEnemy):
                print("Shiny Poochyena!")
                print(px.getpixel(enemyCoordinate))
        if keyboard.is_pressed('esc'):
            print("Exiting program.")
            foundShiny = True
px.show()

##        gui.keyDown('left')
##        time.sleep(0.2)
##        gui.keyUp('left')
##        time.sleep(0.2)
