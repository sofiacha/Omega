from Tkinter import *
from math import *
# ----------------------------------------------------------------------------------------------
# those are used to create the dialog box for the user to tell what grid size wants for the game
import ctypes
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
        Hexagon(self.parent, self.x, self.y, self.size, self.color)
 # ------------------------------------------------------------------------------
class Hexagon:
    def __init__(self, parent, x, y, length, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.length = length  # length of a side
        self.color = color  # fill color
        self.selected = False
        self.tags = tags
        self.neighbors = []
        self.occupied = []
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
class GridSizeDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.top.geometry("%dx%d%+d%+d" % (400, 155, -50, 25))
        Label(top, text="Please choose the size of the game and the colour you are going to be: \n").pack()

        self.variable = StringVar(top)
        self.variable.set("5x5")  # default value
        w = OptionMenu(top, self.variable, "6x6", "7x7", "8x8", "9x9", "10x10")  # , command=self.ok)
        w.pack(padx=15)

        self.variable2 = StringVar(top)
        self.variable2.set("White")  # default value
        w2 = OptionMenu(top, self.variable2, "White", "Black")  # , command=self.ok)
        w2.pack(padx=15)

        button = Button(top, text="OK", command=self.ok)
        button.pack(pady=15)

    def ok(self):
        #print "value is", self.variable.get()
        self.top.destroy()
#--------------------------------------------------------------------------------------------------------#
class GameOver:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.top.geometry("%dx%d%+d%+d" % (200, 85, -850, 250))
        Label(top, text="GAME OVER!").pack()
        button = Button(top, text="OK", command=self.ok)
        button.pack(pady=15)

    def ok(self):
        #print "value is", self.variable.get()
        self.top.destroy()

#-------------------------------------------------------------------------------
class BlackStone:
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
        self.occupied = []
        self.white_neighbors = []
        self.black_neighbors = []

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        self.parent.create_oval(x - r, y - r, x + r, y + r, fill=self.color,
                                outline="#000000",
                                tags=self.tags)
#-------------------------------------------------------------------------------
class WhiteStone:
    score = 0
    def __init__(self, parent, x, y, r, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.r = r
        self.color = color  # fill color
        self.selected = True
        self.tags = tags
        self.draw()
        self.occupied = []
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

# -----------------------------------------------------------------------------------------------------------------------------------
# Corners classes
class CornerLeft:
    def __init__(self, parent, x, y ,tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.tags = tags
        self.initUI()

    def initUI(self):
        x = self.x
        y = self.y
        cos_tr = cos(30 * pi / 180) * 22
        sin_tr = sin(30 * pi / 180) * 22
        xy = [(x, y), (x+50, y), (x+50, y + 11), (x+50 - cos_tr, y+11 + sin_tr), #x0 , x1 , x2, x3,
              (x+50 - cos_tr- cos_tr, y+11 + sin_tr- sin_tr), ( x+50 - cos_tr- cos_tr- cos_tr, y+11 + sin_tr - sin_tr+ sin_tr),  #x4  , x5
              (x+50 - cos_tr- cos_tr- cos_tr, y+11 + sin_tr- sin_tr + sin_tr+ 22),  #x5,
              ( x+50 - cos_tr- cos_tr- cos_tr -cos_tr, y + 11 + sin_tr - sin_tr + sin_tr + 22 + sin_tr), #x6
              (x + 50 - cos_tr - cos_tr - cos_tr - cos_tr- cos_tr/2, y + 11 + sin_tr - sin_tr + sin_tr + 22 + sin_tr - sin_tr/2), #x7
              (x + 50 - cos_tr - cos_tr - cos_tr - cos_tr- cos_tr/2 + sin(30 * pi / 180) * 55, y + 11 + sin_tr - sin_tr + sin_tr + 22 + sin_tr - sin_tr / 2- cos(30 * pi / 180) * 55)] #x8
        self.parent.create_polygon(xy,  fill="#fff", outline="#ffffff", tags = self.tags)

class CornerRight:
    def __init__(self, parent, x, y ,tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.tags = tags
        self.y = y  # top left y
        self.initUI()

    def initUI(self):
        x = self.x
        y = self.y
        cos_tr = cos(30 * pi / 180) * 22
        sin_tr = sin(30 * pi / 180) * 22
        xy = [(x+50, y), (x, y), (x, y + 11), (x + cos_tr, y+11 + sin_tr), #x0 , x1 , x2, x3,
              (x + cos_tr+ cos_tr, y+11 + sin_tr- sin_tr), ( x + cos_tr+ cos_tr+ cos_tr, y+11 + sin_tr - sin_tr+ sin_tr),  #x4  , x5
              (x + cos_tr+ cos_tr+ cos_tr, y+11 + sin_tr- sin_tr + sin_tr+ 22),  #x6,
              (x + cos_tr+ cos_tr+ cos_tr +cos_tr, y + 11 + sin_tr - sin_tr + sin_tr + 22 + sin_tr), #x7
              (x + cos_tr + cos_tr + cos_tr + cos_tr+ cos_tr/2, y + 11 + sin_tr - sin_tr + sin_tr + 22 + sin_tr - sin_tr/2), #x8
              (x + cos_tr + cos_tr + cos_tr + cos_tr+ cos_tr/2 -sin(30 * pi / 180) * 55, y + 11 + sin_tr - sin_tr + sin_tr + 22 + sin_tr - sin_tr / 2- cos(30 * pi / 180) * 55)] #x9
        self.parent.create_polygon(xy,  fill="#fff", outline="#ffffff", tags = self.tags)

class CornerRightMiddle:
    def __init__(self, parent, x, y ,tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.tags = tags
        self.y = y  # top left y
        self.initUI()

    def initUI(self):
        x = self.x
        y = self.y
        cos_tr = cos(30 * pi / 180) * 22
        sin_tr = sin(30 * pi / 180) * 22
        xy = [(x +cos_tr/2, y-sin_tr/2), (x, y), (x, y + 22), (x + cos_tr, y+22 + sin_tr), #x0 , x1 , x2, x3,
              (x + cos_tr, y+22 + sin_tr+ 22), ( x + cos_tr- cos_tr, y+22 + sin_tr +22+ sin_tr),  #x4  , x5
              (x + cos_tr- cos_tr, y+22 + sin_tr+22+ sin_tr+ 22),  #x6,
              (x + cos_tr- cos_tr +cos_tr/2, y + 22 + sin_tr +22 + sin_tr + 22 + sin_tr/2), #x7
              (x + cos_tr- cos_tr +cos_tr + sin(20 * pi / 180) * 55, y + 22 + sin_tr +22 + sin_tr + 22 + sin_tr-cos(20 * pi / 180) * 55)] #x8
        self.parent.create_polygon(xy,  fill="#fff", outline="#ffffff", tags = self.tags)

class CornerLeftMiddle:
    def __init__(self, parent, x, y ,tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.tags =tags
        self.initUI()

    def initUI(self):
        x = self.x
        y = self.y
        cos_tr = cos(30 * pi / 180) * 22
        sin_tr = sin(30 * pi / 180) * 22
        xy = [(x -cos_tr/2, y-sin_tr/2), (x, y), (x, y + 22), (x - cos_tr, y+22 + sin_tr), #x0 , x1 , x2, x3,
              (x - cos_tr, y+22 + sin_tr+ 22), ( x + cos_tr- cos_tr, y+22 + sin_tr +22+ sin_tr),  #x4  , x5
              (x + cos_tr- cos_tr, y+22 + sin_tr+22+ sin_tr+ 22),  #x6,
              (x + cos_tr- cos_tr -cos_tr/2, y + 22 + sin_tr +22 + sin_tr + 22 + sin_tr/2), #x7
              (x + cos_tr- cos_tr -cos_tr - sin(20 * pi / 180) * 55, y + 22 + sin_tr +22 + sin_tr + 22 + sin_tr-cos(20 * pi / 180) * 55)] #x8
        self.parent.create_polygon(xy,  fill="#fff", outline="#ffffff", tags = self.tags)

class CornerLeftBottom:
    def __init__(self, parent, x, y ,tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.tags = tags
        self.initUI()

    def initUI(self):
        x = self.x
        y = self.y
        cos_tr = cos(30 * pi / 180) * 22
        sin_tr = sin(30 * pi / 180) * 22
        xy = [(x -cos_tr/2, y+sin_tr/2), (x, y), (x+cos_tr, y + sin_tr), (x + cos_tr, y+22 + sin_tr), #x0 , x1 , x2, x3,
              (x + 2*cos_tr, y+22 + 2*sin_tr), ( x + 3*cos_tr, y+22 + sin_tr ),  #x4  , x5
              (x + 4*cos_tr, y+22 + 2*sin_tr),  #x6,
              (x + 4*cos_tr, y+33 + 2*sin_tr), #x7
              (x + 4*cos_tr -55, y+33 + 2*sin_tr)] #x8
        self.parent.create_polygon(xy,  fill="#fff", outline="#ffffff", tags = self.tags)

class CornerRightBottom:
    def __init__(self, parent, x, y, tags ):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.tags = tags
        self.initUI()

    def initUI(self):
        x = self.x
        y = self.y
        cos_tr = cos(30 * pi / 180) * 22
        sin_tr = sin(30 * pi / 180) * 22
        xy = [(x +cos_tr/2, y+sin_tr/2), (x, y), (x-cos_tr, y + sin_tr), (x - cos_tr, y+22 + sin_tr), #x0 , x1 , x2, x3,
              (x - 2*cos_tr, y+22 + 2*sin_tr), ( x - 3*cos_tr, y+22 + sin_tr ),  #x4  , x5
              (x - 4*cos_tr, y+22 + 2*sin_tr),  #x6,
              (x - 4*cos_tr, y+33 + 2*sin_tr), #x7
              (x - 4*cos_tr +55, y+33 + 2*sin_tr)] #x8
        self.parent.create_polygon(xy,  fill="#fff", outline="#ffffff", tags = self.tags)