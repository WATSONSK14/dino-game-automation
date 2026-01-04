from PIL import ImageGrab
import time
import pyautogui

time.sleep(3)

#585 640

print(pyautogui.position())
while True:
    cactus = ImageGrab.grab(bbox=(223, 725, 240, 735))
    bird = ImageGrab.grab(bbox=(223 , 585, 240, 633 ))
    obstacle = False
    fly = False


    for x in range(bird.width):
        for y in range(bird.height):
            r, g, b = bird.getpixel((x, y))
            if r == 83 and g == 83 and b == 83:
                fly = True
                break
            elif r == 172 and g == 172 and b == 172:
                fly = True
                break


    for x in range(cactus.width):
        for y in range(cactus.height):
            r, g, b = cactus.getpixel((x, y))
            if r == 83 and g == 83 and b == 83:
                obstacle = True
                break
            elif r == 172 and g == 172 and b == 172:
                obstacle = True
                break

        if obstacle:
            pyautogui.press('space')
            time.sleep(0.1)
            break

        if fly and not obstacle:
            pyautogui.keyDown('down')
            time.sleep(0.2)
            pyautogui.keyUp('down')
            break