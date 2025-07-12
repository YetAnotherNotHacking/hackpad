# Simple numberpad example, will make more detailed ones once I order my pcbs and manufacture the case
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.GP29, board.GP6, board.GP7, board.GP0, board.GP3, board.GP4, board.GP2, board.GP1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8]
]

if __name__ == '__main__':
    keyboard.go()
