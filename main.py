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
TRANS = KC.TRANSPARENT
___ = KC.NO
XXX = KC.NO

# Layers 
BASE = KC.TO(0)	
L1 = KC.TT(1)
L2 = KC.TT(2)

# Settings
keyboard.tap_time = 250
keyboard.debug_enabled = False

# make keymap
keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E,  KC.R,  KC.T,                   XXX,        KC.Y, KC.U, KC.I,    KC.O,   KC.P,     
        KC.A, KC.S, KC.D,  KC.F,  KC.G,                   XXX,        KC.H, KC.J, KC.K,    KC.L,   KC.SCLN,  
        KC.Z, KC.X, KC.C,  KC.V,  KC.B,                   ALT,       KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
        ESC,  TAB,  SHIFT, SUPER, SPACE,                  CTRL,        BACK, RALT, L1, L2,  ENTER,  
    ],
    [
        KC.N7, KC.N8, KC.N9, KC.N0, ___,                  XXX,       KC.F7, KC.F8, KC.F9, KC.F10,   DEL,     
        KC.N4, KC.N5, KC.N6, KC.LBRACKET, KC.RBRACKET,    XXX,       KC.F4, KC.F5, KC.F6, KC.F11,   TRANS,  
        KC.N1, KC.N2, KC.N3, KC.MINUS,  KC.EQUAL,         TRANS,      KC.F1, KC.F2, KC.F3, KC.F12,  TRANS,
        TRANS, TRANS, TRANS, TRANS, TRANS,                TRANS,      TRANS, TRANS, BASE, ___, TRANS, 
        
    ],
    [
        ___, KC.UP, ___, ___,  ___,                       XXX,       ___,  KC.PGUP,  KC.PGDOWN, ___,  ___,
        KC.LEFT, KC.DOWN, KC.RIGHT, ___,  ___,            XXX,       ___,  KC.HOME,  KC.END, ___,  ___,
        ___,  ___,  ___, ___,  ___,                       TRANS,      ___,  ___,  ___, ___,  ___,
        TRANS, TRANS, TRANS, TRANS, TRANS,                TRANS,      TRANS, TRANS, ___, BASE, TRANS, 
    ],
   ]

if __name__ == '__main__':
    keyboard.go()
