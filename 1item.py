import keyboard
import time


def press_and_release_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)


def main():
    print("Pronto")
    while True:
        keyboard.wait('F10')
        time.sleep(0.1)
        press_and_release_key('r', 0.1)
        keyboard.press('tab')
        time.sleep(0.1)
        press_and_release_key('enter', 0.1)
        time.sleep(0.1)
        press_and_release_key('enter', 0.1)
        time.sleep(0.1)
        keyboard.release('tab')


if __name__ == "__main__":
    main()