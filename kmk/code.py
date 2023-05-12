import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType


keyboard = KMKKeyboard()

# https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/split_keyboards.md
# https://github.com/KMKfw/kmk_firmware/blob/master/boards/kyria/main.py
split = Split(  
    split_side=None,
    split_type=SplitType.UART,
    uart_flip=True, #double check
    data_pin=board.D1,
    data_pin2=board.D0,
    use_pio=False,
    split_target_left=True
)
keyboard.modules.append(split)

# vhttps://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.mdx``
# rgb_ext = RGB(
#     pixel_pin=keyboard.rgb_pixel_pin,
#     num_pixels=10,
#     animation_mode=AnimationModes.BREATHING_RAINBOW,
# )
# keyboard.extensions.append(rgb_ext)



keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.A,   KC.B,   KC.C,   KC.D,   KC.E,   KC.I,   KC.N1,          KC.TILD,    KC.L,   KC.M,   KC.N,               KC.O,            KC.P,            KC.Q
        KC.F,   KC.G,   KC.H,   KC.I,   KC.J,   KC.J,   KC.N2,          KC.EXLM,    KC.R    KC.S,   KC.T,               KC.Y,            KC.V,            KC.X
        KC.K,   KC.L,   KC.M,   KC.N,   KC.O,   KC.K,   KC.N3,          KC.AT,      KC.Y,   KC.Z,   KC.LALT(KC.QUOT),   KC.LALT(KC.O),   KC.LALT(KC.A),   KC.X
        KC.N4,  KC.N5,  KC.N6,  KC.N7
    ]
]


if __name__ == '__main__':
    keyboard.go()
