import time
import keyboard
from PIL import ImageGrab

def screen_shot():
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    image = ImageGrab.grab()
    image.save("image{}.png".format(cur_time))

keyboard.add_hotkey("F9", screen_shot)

keyboard.wait("esc")