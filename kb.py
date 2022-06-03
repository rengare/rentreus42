import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

row1 = board.GP14
row2 = board.GP15
row3 = board.GP17
row4 = board.GP16

col1 = board.GP19
col2 = board.GP20
col3 = board.GP21
col4 = board.GP22
col5 = board.GP26
middle = board.GP18
col6 = board.GP4
col7 = board.GP3
col8 = board.GP2
col9 = board.GP1
col10 = board.GP0


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        col1,
        col2,
        col3,
        col4,
        col5,
        middle,
        col6,
        col7,
        col8,
        col9,
        col10, 
    )
    row_pins = (row1, row2, row3, row4)
    diode_orientation = DiodeOrientation.COL2ROW
