
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules = [layers]

'''
'''

keyboard.col_pins = [board.GP5,board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
                     board.GP12,board.GP13,board.GP14, board.GP15, board.GP18, board.GP19, board.GP20, board.GP21]#[::-1] # gp 16 & 17 have resin in them lamo
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

BLANK = KC.KP_DOT
         
keyboard.keymap = [[
  KC.ESC,  KC.N1,    KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,    KC.N9,    KC.N0,    KC.MINS, KC.EQL,  KC.BSPC, KC.DEL, 
  KC.TAB,  KC.Q,    KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,          KC.PGUP,
  KC.CLCK, KC.A,    KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN, KC.QUOT,     BLANK,     KC.ENT,           KC.PGDN,
  KC.LSFT, BLANK,   KC.Z,    KC.X,   KC.C,  KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,  KC.UP,   KC.END,
  KC.LCTL, KC.LGUI, KC.LALT, BLANK, BLANK, BLANK,   KC.SPC, BLANK,  BLANK,  BLANK,  KC.RALT, KC.RCTL,  KC.LEFT, KC.DOWN, KC.RGHT]]

if __name__ == '__main__':
    keyboard.go()
