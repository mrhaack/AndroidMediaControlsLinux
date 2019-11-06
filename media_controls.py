from pynput.keyboard import KeyCode, Controller

keyboard = Controller()

def toggle_play():
    keyboard.press(KeyCode.from_vk(0x1008FF14))
    keyboard.release(KeyCode.from_vk(0x1008FF14))