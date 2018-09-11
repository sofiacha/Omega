from Tkinter import *
from math import cos, sin, sqrt, radians
# import sys
import ctypes  # An included library with Python install.
from ctypes.wintypes import HWND, LPWSTR, UINT

_user32 = ctypes.WinDLL('user32', use_last_error=True)

_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT  # default return type is c_int, this is not required
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

MB_OK = 0
MB_OKCANCEL = 1
MB_YESNOCANCEL = 3
MB_YESNO = 4

IDOK =  1
IDCANCEL = 2
IDABORT = 3
IDYES = 6
IDNO = 7

# ------------------------------------------------------------------------------
class Frame:
    def __init__(self, parent, x, y, kind, size):
        self.parent = parent
        self.x = x
        self.y = y
        self.kind = kind
        self.selected = False
    def draw(self):
        FillHexagon(self.parent, self.x, self.y, self.size, self.color)
 # ------------------------------------------------------------------------------
class FillHexagon:
    def __init__(self, parent, x, y, length, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.length = length  # length of a side
        self.color = color  # fill color
        self.selected = False
        self.tags = tags
        self.draw()
    def draw(self):
        start_x = self.x
        start_y = self.y
        angle = 60
        coords = []
        for i in range(6):
            end_x = start_x + self.length * cos(radians(angle * i))
            end_y = start_y + self.length * sin(radians(angle * i))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y
        self.parent.create_polygon(coords[0][1],
                                   coords[0][0],
                                   coords[1][1],
                                   coords[1][0],
                                   coords[2][1],
                                   coords[2][0],
                                   coords[3][1],
                                   coords[3][0],
                                   coords[4][1],
                                   coords[4][0],
                                   coords[5][1],
                                   coords[5][0],
                                   fill=self.color,
                                   outline="#ffffff",
                                   tags=self.tags)
#--------------------------------------------------------------------------------------------------------#
class MyDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.top.geometry("%dx%d%+d%+d" % (400, 150, -50, 25))
        Label(top, text="Please insert the number of players and the size of the game").pack()
        self.variable = StringVar(top)
        self.variable.set("2 players") # default value
        w = OptionMenu(top, self.variable, "2 players", "3 players", "4 players")#, command=self.ok)
        w.pack(padx=15)

        self.variable2 = StringVar(top)
        self.variable2.set("5x5")  # default value
        w2 = OptionMenu(top, self.variable2, "6x6", "7x7", "8x8", "9x9", "10x10")  # , command=self.ok)
        w2.pack(padx=15)

        button = Button(top, text="OK", command=self.ok)
        button.pack(pady=15)

    def ok(self):
        #print "value is", self.variable.get()
        self.top.destroy()


#-------------------------------------------------------------------------------
class BlackCircle:
    score = 0
    def __init__(self, parent, x, y, r, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.r = r  # top left y
        self.color = color  # fill color
        self.selected = True
        self.tags = tags
        self.draw()
        self.neighbors = []
        self.black_neighbors = []
        self.white_neighbors = []

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        self.parent.create_oval(x - r, y - r, x + r, y + r, fill=self.color,
                                outline="#000000",
                                tags=self.tags)
#-------------------------------------------------------------------------------
class WhiteCircle:
    score = 0
    def __init__(self, parent, x, y, r, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.r = r  # top left y
        self.color = color  # fill color
        self.selected = True
        self.tags = tags
        self.draw()
        self.neighbors = []
        self.black_neighbors = []
        self.white_neighbors = []

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        self.parent.create_oval(x - r, y - r, x + r, y + r, fill=self.color,
                                outline="#ffffff",
                                tags=self.tags)
