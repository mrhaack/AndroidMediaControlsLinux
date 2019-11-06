from pynput.keyboard import KeyCode, Controller

keyboard = Controller()
VK_MEDIA_PLAY_PAUSE = 0x1008FF14

def toggle_play():
    keyboard.press(KeyCode.from_vk(VK_MEDIA_PLAY_PAUSE))
    keyboard.release(KeyCode.from_vk(VK_MEDIA_PLAY_PAUSE))