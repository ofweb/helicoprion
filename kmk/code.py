import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.layers import Layers
from kmk.modules.capsword import CapsWord
from kmk.extensions.media_keys import MediaKeys



keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

caps_word=CapsWord()
keyboard.modules.append(caps_word)

# https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/split_keyboards.md
# https://github.com/KMKfw/kmk_firmware/blob/master/boards/kyria/main.py
split = Split(  
    split_side=None,
    split_type=SplitType.UART,
    uart_flip=False,
    data_pin=board.D1,
    data_pin2=board.D0,
    use_pio=False,
    split_target_left=True
)
keyboard.modules.append(split)

keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# +--+--+--+--+--+                    +--+--+--+--+--+
# |00|01|02|03|04|                    |28|27|26|25|24|
# +--+--+--+--+--+                    +--+--+--+--+--+
# |06|07|08|09|10|                    |34|33|32|31|30| 
# +--+--+--+--+--+                    +--+--+--+--+--+
# |12|13|14|15|16|                    |40|39|38|37|36|
# +--+--+--+--+--+--+--+--+  +--+--+--+--+--+--+--+--+
#             +--|22|05|11|  |35|29|46|--+            
#             |20+--+--+--+  +--+--+--+44|            
#             +--|21|23|17|  |41|47|45|--+            
#                +--+--+--+  +--+--+--+               

# [
#     00, 01, 02, 03, 04, 05, 29, 28, 27, 26, 25, 24,
#     06, 07, 08, 09, 10, 11, 35, 34, 33, 32, 31, 30,
#     12, 13, 14, 15, 16, 17, 41, 40, 39, 38, 37, 36,
#     --, --, 20, 21, 22, 23, 47, 46, 45, 44, --, --,
# ]


keyboard.keymap = [
# +--+--+--+--+--+                    +--+--+--+--+--+
# | Q| W| F| P| B|                    | J| L| U| Y| ⌫|
# +--+--+--+--+--+                    +--+--+--+--+--+
# | A| R| S| T| G|                    | M| N| E| I| O| 
# +--+--+--+--+--+                    +--+--+--+--+--+
# | Z| X| C| D| V|                    | K| H| Æ| Ø| Å|
# +--+--+--+--+--+--+--+--+  +--+--+--+--+--+--+--+--+
#             +--| ⇥| ⇧| .|  | ;| ⎈|CW|--+            
#             |L1+--+--+--+  +--+--+--+L2|           
#             +--| ⎵| ⌥| ,|  | :| ⌘| ↵|--+            
#                +--+--+--+  +--+--+--+         
    [
        KC.Q,   KC.W,   KC.F,       KC.P,   KC.B,       KC.LSFT,    KC.RCTRL,  KC.J,    KC.L,       KC.U,               KC.Y,               KC.BSPC,
        KC.A,   KC.R,   KC.S,       KC.T,   KC.G,       KC.DOT,     KC.SCLN,   KC.M,    KC.N,       KC.E,               KC.I,               KC.O,
        KC.Z,   KC.X,   KC.C,       KC.D,   KC.V,       KC.COMM,    KC.COLN,   KC.K,    KC.H,       KC.LALT(KC.QUOT),   KC.LALT(KC.O),      KC.LALT(KC.A),
        KC.NO,  KC.NO,  KC.MO(1),   KC.SPC, KC.TAB,     KC.LALT,    KC.RCMD,   KC.CW,   KC.ENT,     KC.MO(2),           KC.NO,              KC.NO,
    ],
# +--+--+--+--+--+                    +--+--+--+--+---+
# | @| _| \| "| +|                    | >| )| }| ]|DEL|
# +--+--+--+--+--+                    +--+--+--+--+---+
# | #| -| /| '| =|                    | <| (| {| [| ^ | 
# +--+--+--+--+--+                    +--+--+--+--+---+
# | $| ~| || `| ?|                    | !| %|  | &| * |
# +--+--+--+--+--+--+--+--+  +--+--+--+--+--+--+--+---+
#             +--| ⇥| ⇧| .|  | ;| ⎈|CW|--+            
#             |L1+--+--+--+  +--+--+--+L2|           
#             +--| ⎵| ⌥| ,|  | :| ⌘| ↵|--+            
#                +--+--+--+  +--+--+--+      
    [
        KC.AT,      KC.UNDS,    KC.BSLS,     KC.DQUO,     KC.PLUS,      KC.TRNS,    KC.TRNS,   KC.RABK,    KC.RPRN,       KC.RCBR,     KC.RBRC,      KC.DEL,
        KC.HASH,    KC.MINS,    KC.SLSH,     KC.QUOT,     KC.EQL,       KC.TRNS,    KC.TRNS,   KC.LABK,    KC.LPRN,       KC.LCBR,     KC.LBRC,      KC.CIRC,
        KC.DLR,     KC.TILD,    KC.PIPE,     KC.GRV,      KC.QUES,      KC.TRNS,    KC.TRNS,   KC.EXLM,    KC.PERC,       KC.NO,       KC.AMPR,      KC.ASTR,
        KC.NO,      KC.NO,      KC.TRNS,     KC.TRNS,     KC.TRNS,      KC.TRNS,    KC.TRNS,   KC.TRNS,    KC.TRNS,       KC.TRNS,     KC.NO,        KC.NO,
    ],
# +---+--+--+--+--+                    +---+---+---+---+---+
# |del|  | 7| 8| 9|                    |F11|F12| VU|MUT| VD|
# +---+--+--+--+--+                    +---+---+---+---+---+
# | → | ↑| 4| 5| 6|                    | F6| F7| F8| F9|F10| 
# +---+--+--+--+--+                    +---+---+---+---+---+
# | ← | ↓| 1| 2| 3|                    | F1| F2| F3| F4| F5|
# +---+--+--+--+--+--+--+--+  +--+--+--+---+---+---+---+---+
#             +--| ⇥| ⇧| .|  | ;| ⎈|CW|--+            
#             |L1+--+--+--+  +--+--+--+L2|           
#             +--| ⎵| ⌥| ,|  | :| ⌘| ↵|--+            
#                +--+--+--+  +--+--+--+        
    [
        KC.GESC,     KC.NO,    KC.N7,     KC.N8,     KC.N9,      KC.TRNS,    KC.TRNS,   KC.F11,       KC.F12,      KC.VOLU,   KC.MUTE,    KC.VOLD,
        KC.RIGHT,   KC.UP,    KC.N4,     KC.N5,     KC.N6,      KC.TRNS,    KC.TRNS,   KC.F6,        KC.F7,       KC.F8,     KC.F9,      KC.F10,
        KC.LEFT,    KC.DOWN,  KC.N1,     KC.N2,     KC.N3,      KC.TRNS,    KC.TRNS,   KC.F1,        KC.F2,       KC.F3,     KC.F4,      KC.F5,
        KC.NO,      KC.NO,    KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.NO,      KC.NO,
    ]
]


if __name__ == '__main__':
    keyboard.go()

