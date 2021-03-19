import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    
    for i in range(199, 250):
        for j in range(355, 417):
            if data[i, j] < 100:
                hit("up")
                return 

    for i in range(180, 200):
        for j in range(280, 353):
            if data[i, j] < 100:
                hit("down")
                return 
            
    return

if __name__ == "__main__":
    print("Hey..Dino game about to start in 3 seconds")
    time.sleep(3)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print (asarray(image))

        # Draw the rectangle for cactus
        # for i in range(199, 250):
        #     for j in range(355, 417):
        #         data[i, j] = 0

        # # Draw the rectangle for birds
        # for i in range(180, 200):
        #     for j in range(280, 353):
        #         data[i, j] = 171

        # image.show()
        # break
