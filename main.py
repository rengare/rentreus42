print("Starting")
import board

from kb import KMKKeyboard

from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules = [
    Layers(),
]

# Keys mapping 
SUPER = KC.LWIN
SHIFT = KC.LSHIFT
CTRL = KC.LCTRL
ALT = KC.LALT
RALT = KC.RALT
TAB = KC.TAB
ESC = KC.ESCAPE
ENTER = KC.ENTER
SPACE = KC.SPACE
BACK = KC.BACKSPACE
DEL = KC.DELETE

XXXXXXX = KC.NO

# Layers 
BASE = KC.TO(0)	
L1 = KC.TT(1)
L2 = KC.TT(2)

# Settings
keyboard.tap_time = 250
keyboard.debug_enabled = False

# make keymap
keyboard.keymap = [
    [  # base                                                #middle
        KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,    XXXXXXX,     KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,     
        KC.A,      KC.S,      KC.D,      KC.F,      KC.G,    XXXXXXX,     KC.H,      KC.J,      KC.K,      KC.L,      KC.SCLN,  
        KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,      CTRL,      KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,
        ESC,       TAB,       SUPER,     SHIFT,     SPACE,     ALT,       BACK,      RALT,      L1,        L2,        ENTER,  
    ],
    [  # func                                                #middle
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     DEL,      XXXXXXX,  BASE,  XXXXXXX,  XXXXXXX,
    ],
    [  # xxxx                                                #middle
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,      XXXXXXX,     XXXXXXX,  XXXXXXX,  BASE,  XXXXXXX,  XXXXXXX,
    ]
   ]

if __name__ == '__main__':
    # keyboard.go(hid_type=HIDModes.BLE, ble_name='Rentreus42')
    keyboard.go()
