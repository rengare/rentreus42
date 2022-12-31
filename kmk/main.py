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
L0 = KC.TO(0)	
L1 = KC.TT(1)
L2 = KC.TT(2)

# Settings
keyboard.tap_time = 250
keyboard.debug_enabled = False

# make keymap
keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E,  KC.R,  KC.T,                      XXX,        KC.Y, KC.U, KC.I,    KC.O,   KC.P,     
        KC.A, KC.S, KC.D,  KC.F,  KC.G,                      XXX,        KC.H, KC.J, KC.K,    KC.L,   KC.SCLN,  
        KC.Z, KC.X, KC.C,  KC.V,  KC.B,                      ALT,        KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
        ESC,  TAB,  SUPER, SHIFT, SPACE,                     CTRL,       BACK, RALT,   L1,    KC.QUOTE,  ENTER,  
    ],
    [
        KC.EXCLAIM, KC.AT, KC.LPRN, KC.RPRN, KC.PIPE,        XXX,        KC.PGUP,  KC.N7, KC.N8,   KC.N9,   KC.ASTERISK,     
        KC.HASH, KC.DLR, KC.LBRC, KC.RBRC   ,KC.ZKHK,        XXX,        KC.PGDN,  KC.N4, KC.N5,   KC.N6,   KC.MINUS,     
        KC.PERC, KC.AMPR, 	KC.ASTR, KC.PIPE, ___,                     TRANS,      ___,      KC.N1, KC.N2,   KC.N3,   KC.BSLS,     
        TRANS, L2, TRANS, TRANS, TRANS,                      TRANS,      TRANS,    L2,    KC.DOT,  KC.N0,   KC.EQUAL, 
    ],
    [
        KC.PSCR, KC.HOME, KC.UP, KC.END, KC.PGUP,           XXX,        KC.PGUP,   KC.F7, KC.F8,   KC.F9,  KC.F10,       
        DEL, KC.LEFT, KC.DOWN, KC.RIGHT,KC.PGDN,            XXX,        KC.PGDN,   KC.F4, KC.F5,   KC.F6,  KC.F11,    
       KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.MEDIA_PLAY_PAUSE,                            TRANS,      KC.AMPR,   KC.F1, KC.F2,   KC.F3,  KC.F12,   
        TRANS, L0, TRANS, TRANS, TRANS,                     TRANS,      TRANS,      L0,     ___ ,   ___,   ENTER,  
    ],
]

if __name__ == '__main__':
    keyboard.go()
