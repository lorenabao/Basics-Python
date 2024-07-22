from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
starttime = time.monotonic()

keyboard.type("Hello World, ")

while True:
    keyboard.press('A')
    keyboard.release('A')
    print("OK")
    time.sleep(120)
    # time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))



