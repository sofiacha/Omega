from classes import *
from math import *
def init_grid(canvas,cols, rows, size, debug):
    hexagons = []
    # 1h sthlh
    for col in range(3):
        if col % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(1):
            h = FillHexagon(canvas,
                            col * (size * 1.5) + 8.05 * (size * sqrt(3) / 2) + 145,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
            hexagons.append(h)
            if debug:
                coords = "{}".format(len(hexagons) - 1)
                canvas.create_text((ro * (size * sqrt(3))) + 120 + offset,
                                     col * (size * 1.5) + 8.05 * (size * sqrt(3) / 2) + 145 + 10,
                                     text=coords)
    # 2h sthlh
    for col in range(7):
        if col % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(1, 2, 1):
            h = FillHexagon(canvas,
                            col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 146,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 146 + 10,
                                 text=coords)
    # 3h grammh
    for col in range(11):
        if col % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(2, 3, 1):
            h = FillHexagon(canvas,
                            col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 81,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 81 + 10,
                                 text=coords)

    # 4h sthlh
    for col in range(15):
        if col % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(3, 4, 1):
            h = FillHexagon(canvas,
                            col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 14,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 15 + 10,
                                 text=coords)
    # 5h sthlh
    for col in range(19):
        if col % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(4, 5, 1):
            h = FillHexagon(canvas,
                            col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) - 52,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) - 50 + 10,
                                 text=coords)

    # 6h sthlh
    for col in range(19):
        if col % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(5, 6, 1):
            h = FillHexagon(canvas,
                            col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) - 52,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) - 50 + 10,
                                 text=coords)

    # 7 ews 15 sthles
    for c in range(19):
        if c % 2 == 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for r in range(6, rows, 1):
            h = FillHexagon(canvas,
                            c * (size * 1.5) + 35,
                            (r * (size * sqrt(3))) + offset + 100,
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
            hexagons.append(h)
            if debug:
                coords = "{}".format(len(hexagons) - 1)
                canvas.create_text((r * (size * sqrt(3))) + offset + 120,
                                     c * (size * 1.5) + 35 + 10,
                                     text=coords)

    # 16h sthlh
    for c in range(17):
        if c % 2 != 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for r in range(rows, rows + 1, 1):
            h = FillHexagon(canvas,
                            c * (size * 1.5) + 68,
                            (r * (size * sqrt(3))) + offset + 100,
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
            hexagons.append(h)
            if debug:
                coords = "{}".format(len(hexagons) - 1)
                canvas.create_text((r * (size * sqrt(3))) + offset + 120,
                                     c * (size * 1.5) + 68 + 10,
                                     text=coords)

    # 17h sthlh
    for ciol in range(13):
        if ciol % 2 != 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(rows + 1, rows + 2, 1):
            h = FillHexagon(canvas,
                            ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2) + 81,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2) + 81 + 10,
                                 text=coords)
    # 18h sthlh
    for ciol in range(9):
        if ciol % 2 != 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(rows + 2, rows + 3, 1):
            h = FillHexagon(canvas,
                            ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2) + 146,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2) + 146 + 10,
                                 text=coords)
    # 19h sthlh
    for cil in range(5):
        if cil % 2 != 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(rows + 3, rows + 4, 1):
            h = FillHexagon(canvas,
                            cil * (size * 1.5) + 6.3 * (size * sqrt(3) / 2) + 146,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 cil * (size * 1.5) + 6.3 * (size * sqrt(3) / 2) + 146 + 10,
                                 text=coords)
    # 20h sthlh
    for ci in range(1):
        if ci % 2 != 0:
            offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
        else:
            offset = 0
        for ro in range(rows + 4, rows + 5, 1):
            h = FillHexagon(canvas,
                            ci * (size * 1.5) + 9.75 * (size * sqrt(3) / 2) + 146,
                            (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                            size,
                            "#5FFF2D",
                            "{}.{}".format("S", len(hexagons)))
        hexagons.append(h)
        if debug:
            coords = "{}".format(len(hexagons) - 1)
            canvas.create_text((ro * (size * sqrt(3))) + offset + 120,
                                 ci * (size * 1.5) + 9.75 * (size * sqrt(3) / 2) + 146 + 10,
                                 text=coords)

    return hexagons


def choose_grid(canvas, size_of_game, hexagons):
    openP = []
    if (size_of_game == "5x5"):
        cL = 115
        cR = 119
        cRM = 153
        cLM = 64
        cLB = 179
        cRB = 183
        for i in hexagons:
            if i.tags != "S.0" and i.tags != "S.1" and i.tags != "S.2" and i.tags != "S.8" and i.tags != "S.9" and i.tags != "S.19" and i.tags != "S.20" and i.tags != "S.34" and i.tags != "S.35" and i.tags != "S.53" and i.tags != "S.54" and i.tags != "S.73" and i.tags != "S.218" and i.tags != "S.219" and i.tags != "S.220" and i.tags != "S.221" and i.tags != "S.222" and i.tags != "S.223" and i.tags != "S.224" and i.tags != "S.225" and i.tags != "S.242" and i.tags != "S.241" and i.tags != "S.255" and i.tags != "S.254" and i.tags != "S.264" and i.tags != "S.263" and i.tags != "S.269" and i.tags != "S.268" and i.tags != "S.270" and i.tags != "S.266" and i.tags != "S.265" and i.tags != "S.257" and i.tags != "S.256" and i.tags != "S.244" and i.tags != "S.243" and i.tags != "S.227" and i.tags != "S.226" and i.tags != "S.81" and i.tags != "S.80" and i.tags != "S.79" and i.tags != "S.78" and i.tags != "S.77" and i.tags != "S.76" and i.tags != "S.75" and i.tags != "S.74" and i.tags != "S.55" and i.tags != "S.36" and i.tags != "S.37" and i.tags != "S.21" and i.tags != "S.22" and i.tags != "S.10" and i.tags != "S.11" and i.tags != "S.3" and i.tags != "S.4" and i.tags != "S.5" and i.tags != "S.6" and i.tags != "S.7" and i.tags != "S.17" and i.tags != "S.18" and i.tags != "S.32" and i.tags != "S.33" and i.tags != "S.51" and i.tags != "S.52" and i.tags != "S.72" and i.tags != "S.210" and i.tags != "S.211" and i.tags != "S.212" and i.tags != "S.213" and i.tags != "S.214" and i.tags != "S.215" and i.tags != "S.216" and i.tags != "S.217" and i.tags != "S.209" and i.tags != "S.240" and i.tags != "S.239" and i.tags != "S.253" and i.tags != "S.252" and i.tags != "S.262" and i.tags != "S.261" and i.tags != "S.267" and i.tags != "S.259" and i.tags != "S.258" and i.tags != "S.246" and i.tags != "S.245" and i.tags != "S.229" and i.tags != "S.228" and i.tags != "S.97" and i.tags != "S.89" and i.tags != "S.88" and i.tags != "S.87" and i.tags != "S.86" and i.tags != "S.85" and i.tags != "S.84" and i.tags != "S.83" and i.tags != "S.82" and i.tags != "S.56" and i.tags != "S.38" and i.tags != "S.39" and i.tags != "S.23" and i.tags != "S.24" and i.tags != "S.12" and i.tags != "S.13" and i.tags != "S.14" and i.tags != "S.15" and i.tags != "S.16" and i.tags != "S.30" and i.tags != "S.31" and i.tags != "S.49" and i.tags != "S.50" and i.tags != "S.70" and i.tags != "S.71" and i.tags != "S.202" and i.tags != "S.203" and i.tags != "S.204" and i.tags != "S.205" and i.tags != "S.206" and i.tags != "S.207" and i.tags != "S.208" and i.tags != "S.201" and i.tags != "S.193" and i.tags != "S.238" and i.tags != "S.237" and i.tags != "S.251" and i.tags != "S.250" and i.tags != "S.260" and i.tags != "S.248" and i.tags != "S.247" and i.tags != "S.231" and i.tags != "S.230" and i.tags != "S.113" and i.tags != "S.105" and i.tags != "S.96" and i.tags != "S.95" and i.tags != "S.94" and i.tags != "S.93" and i.tags != "S.92" and i.tags != "S.91" and i.tags != "S.90" and i.tags != "S.57" and i.tags != "S.58" and i.tags != "S.40" and i.tags != "S.41" and i.tags != "S.25" and i.tags != "S.26" and i.tags != "S.27" and i.tags != "S.28" and i.tags != "S.29" and i.tags != "S.47" and i.tags != "S.48" and i.tags != "S.68" and i.tags != "S.69" and i.tags != "S.194" and i.tags != "S.195" and i.tags != "S.196" and i.tags != "S.197" and i.tags != "S.198" and i.tags != "S.199" and i.tags != "S.200" and i.tags != "S.192" and i.tags != "S.185" and i.tags != "S.177" and i.tags != "S.236" and i.tags != "S.235" and i.tags != "S.249" and i.tags != "S.233" and i.tags != "S.232" and i.tags != "S.129" and i.tags != "S.121" and i.tags != "S.112" and i.tags != "S.104" and i.tags != "S.103" and i.tags != "S.102" and i.tags != "S.101" and i.tags != "S.100" and i.tags != "S.99" and i.tags != "S.98" and i.tags != "S.59" and i.tags != "S.60" and i.tags != "S.42" and i.tags != "S.43" and i.tags != "S.44" and i.tags != "S.45" and i.tags != "S.46" and i.tags != "S.66" and i.tags != "S.67" and i.tags != "S.178" and i.tags != "S.186" and i.tags != "S.187" and i.tags != "S.188" and i.tags != "S.189" and i.tags != "S.190" and i.tags != "S.191" and i.tags != "S.184" and i.tags != "S.176" and i.tags != "S.169" and i.tags != "S.161" and i.tags != "S.234" and i.tags != "S.145" and i.tags != "S.137" and i.tags != "S.128" and i.tags != "S.120" and i.tags != "S.111" and i.tags != "S.110" and i.tags != "S.109" and i.tags != "S.108" and i.tags != "S.107" and i.tags != "S.106" and i.tags != "S.114" and i.tags != "S.61" and i.tags != "S.62":
                openP.append(i)
    if (size_of_game == "6x6"):
        cL = 106
        cR = 111
        cRM = 234
        cLM = 45
        cLB = 186
        cRB = 191
        for i in hexagons:
            if i.tags != "S.0" and i.tags != "S.1" and i.tags != "S.2" and i.tags != "S.8" and i.tags != "S.9" and i.tags != "S.19" and i.tags != "S.20" and i.tags != "S.34" and i.tags != "S.35" and i.tags != "S.53" and i.tags != "S.54" and i.tags != "S.73" and i.tags != "S.218" and i.tags != "S.219" and i.tags != "S.220" and i.tags != "S.221" and i.tags != "S.222" and i.tags != "S.223" and i.tags != "S.224" and i.tags != "S.225" and i.tags != "S.242" and i.tags != "S.241" and i.tags != "S.255" and i.tags != "S.254" and i.tags != "S.264" and i.tags != "S.263" and i.tags != "S.269" and i.tags != "S.268" and i.tags != "S.270" and i.tags != "S.266" and i.tags != "S.265" and i.tags != "S.257" and i.tags != "S.256" and i.tags != "S.244" and i.tags != "S.243" and i.tags != "S.227" and i.tags != "S.226" and i.tags != "S.81" and i.tags != "S.80" and i.tags != "S.79" and i.tags != "S.78" and i.tags != "S.77" and i.tags != "S.76" and i.tags != "S.75" and i.tags != "S.74" and i.tags != "S.55" and i.tags != "S.36" and i.tags != "S.37" and i.tags != "S.21" and i.tags != "S.22" and i.tags != "S.10" and i.tags != "S.11" and i.tags != "S.3" and i.tags != "S.4" and i.tags != "S.5" and i.tags != "S.6" and i.tags != "S.7" and i.tags != "S.17" and i.tags != "S.18" and i.tags != "S.32" and i.tags != "S.33" and i.tags != "S.51" and i.tags != "S.52" and i.tags != "S.72" and i.tags != "S.210" and i.tags != "S.211" and i.tags != "S.212" and i.tags != "S.213" and i.tags != "S.214" and i.tags != "S.215" and i.tags != "S.216" and i.tags != "S.217" and i.tags != "S.209" and i.tags != "S.240" and i.tags != "S.239" and i.tags != "S.253" and i.tags != "S.252" and i.tags != "S.262" and i.tags != "S.261" and i.tags != "S.267" and i.tags != "S.259" and i.tags != "S.258" and i.tags != "S.246" and i.tags != "S.245" and i.tags != "S.229" and i.tags != "S.228" and i.tags != "S.97" and i.tags != "S.89" and i.tags != "S.88" and i.tags != "S.87" and i.tags != "S.86" and i.tags != "S.85" and i.tags != "S.84" and i.tags != "S.83" and i.tags != "S.82" and i.tags != "S.56" and i.tags != "S.38" and i.tags != "S.39" and i.tags != "S.23" and i.tags != "S.24" and i.tags != "S.12" and i.tags != "S.13" and i.tags != "S.14" and i.tags != "S.15" and i.tags != "S.16" and i.tags != "S.30" and i.tags != "S.31" and i.tags != "S.49" and i.tags != "S.50" and i.tags != "S.70" and i.tags != "S.71" and i.tags != "S.202" and i.tags != "S.203" and i.tags != "S.204" and i.tags != "S.205" and i.tags != "S.206" and i.tags != "S.207" and i.tags != "S.208" and i.tags != "S.201" and i.tags != "S.193" and i.tags != "S.238" and i.tags != "S.237" and i.tags != "S.251" and i.tags != "S.250" and i.tags != "S.260" and i.tags != "S.248" and i.tags != "S.247" and i.tags != "S.231" and i.tags != "S.230" and i.tags != "S.113" and i.tags != "S.105" and i.tags != "S.96" and i.tags != "S.95" and i.tags != "S.94" and i.tags != "S.93" and i.tags != "S.92" and i.tags != "S.91" and i.tags != "S.90" and i.tags != "S.57" and i.tags != "S.58" and i.tags != "S.40" and i.tags != "S.41" and i.tags != "S.25" and i.tags != "S.26" and i.tags != "S.27" and i.tags != "S.28" and i.tags != "S.29" and i.tags != "S.47" and i.tags != "S.48" and i.tags != "S.68" and i.tags != "S.69" and i.tags != "S.194" and i.tags != "S.195" and i.tags != "S.196" and i.tags != "S.197" and i.tags != "S.198" and i.tags != "S.199" and i.tags != "S.200" and i.tags != "S.192" and i.tags != "S.185" and i.tags != "S.177" and i.tags != "S.236" and i.tags != "S.235" and i.tags != "S.249" and i.tags != "S.233" and i.tags != "S.232" and i.tags != "S.129" and i.tags != "S.121" and i.tags != "S.112" and i.tags != "S.104" and i.tags != "S.103" and i.tags != "S.102" and i.tags != "S.101" and i.tags != "S.100" and i.tags != "S.99" and i.tags != "S.98" and i.tags != "S.59" and i.tags != "S.60" and i.tags != "S.42" and i.tags != "S.43":
                openP.append(i)
    if (size_of_game == "7x7"):
        cL = 98
        cR = 104
        cRM = 249
        cLM = 28
        cLB = 194
        cRB = 200
        for i in hexagons:
            if i.tags != "S.0" and i.tags != "S.1" and i.tags != "S.2" and i.tags != "S.8" and i.tags != "S.9" and i.tags != "S.19" and i.tags != "S.20" and i.tags != "S.34" and i.tags != "S.35" and i.tags != "S.53" and i.tags != "S.54" and i.tags != "S.73" and i.tags != "S.218" and i.tags != "S.219" and i.tags != "S.220" and i.tags != "S.221" and i.tags != "S.222" and i.tags != "S.223" and i.tags != "S.224" and i.tags != "S.225" and i.tags != "S.242" and i.tags != "S.241" and i.tags != "S.255" and i.tags != "S.254" and i.tags != "S.264" and i.tags != "S.263" and i.tags != "S.269" and i.tags != "S.268" and i.tags != "S.270" and i.tags != "S.266" and i.tags != "S.265" and i.tags != "S.257" and i.tags != "S.256" and i.tags != "S.244" and i.tags != "S.243" and i.tags != "S.227" and i.tags != "S.226" and i.tags != "S.81" and i.tags != "S.80" and i.tags != "S.79" and i.tags != "S.78" and i.tags != "S.77" and i.tags != "S.76" and i.tags != "S.75" and i.tags != "S.74" and i.tags != "S.55" and i.tags != "S.36" and i.tags != "S.37" and i.tags != "S.21" and i.tags != "S.22" and i.tags != "S.10" and i.tags != "S.11" and i.tags != "S.3" and i.tags != "S.4" and i.tags != "S.5" and i.tags != "S.6" and i.tags != "S.7" and i.tags != "S.17" and i.tags != "S.18" and i.tags != "S.32" and i.tags != "S.33" and i.tags != "S.51" and i.tags != "S.52" and i.tags != "S.72" and i.tags != "S.210" and i.tags != "S.211" and i.tags != "S.212" and i.tags != "S.213" and i.tags != "S.214" and i.tags != "S.215" and i.tags != "S.216" and i.tags != "S.217" and i.tags != "S.209" and i.tags != "S.240" and i.tags != "S.239" and i.tags != "S.253" and i.tags != "S.252" and i.tags != "S.262" and i.tags != "S.261" and i.tags != "S.267" and i.tags != "S.259" and i.tags != "S.258" and i.tags != "S.246" and i.tags != "S.245" and i.tags != "S.229" and i.tags != "S.228" and i.tags != "S.97" and i.tags != "S.89" and i.tags != "S.88" and i.tags != "S.87" and i.tags != "S.86" and i.tags != "S.85" and i.tags != "S.84" and i.tags != "S.83" and i.tags != "S.82" and i.tags != "S.56" and i.tags != "S.38" and i.tags != "S.39" and i.tags != "S.23" and i.tags != "S.24" and i.tags != "S.12" and i.tags != "S.13" and i.tags != "S.14" and i.tags != "S.15" and i.tags != "S.16" and i.tags != "S.30" and i.tags != "S.31" and i.tags != "S.49" and i.tags != "S.50" and i.tags != "S.70" and i.tags != "S.71" and i.tags != "S.202" and i.tags != "S.203" and i.tags != "S.204" and i.tags != "S.205" and i.tags != "S.206" and i.tags != "S.207" and i.tags != "S.208" and i.tags != "S.201" and i.tags != "S.193" and i.tags != "S.238" and i.tags != "S.237" and i.tags != "S.251" and i.tags != "S.250" and i.tags != "S.260" and i.tags != "S.248" and i.tags != "S.247" and i.tags != "S.231" and i.tags != "S.230" and i.tags != "S.113" and i.tags != "S.105" and i.tags != "S.96" and i.tags != "S.95" and i.tags != "S.94" and i.tags != "S.93" and i.tags != "S.92" and i.tags != "S.91" and i.tags != "S.90" and i.tags != "S.57" and i.tags != "S.58" and i.tags != "S.40" and i.tags != "S.41" and i.tags != "S.25" and i.tags != "S.26":
                openP.append(i)
    if (size_of_game == "8x8"):
        cL = 57
        cR = 96
        cRM = 260
        cLM = 15
        cLB = 71
        cRB = 208
        for i in hexagons:
            if i.tags != "S.0" and i.tags != "S.1" and i.tags != "S.2" and i.tags != "S.8" and i.tags != "S.9" and i.tags != "S.19" and i.tags != "S.20" and i.tags != "S.34" and i.tags != "S.35" and i.tags != "S.53" and i.tags != "S.54" and i.tags != "S.73" and i.tags != "S.218" and i.tags != "S.219" and i.tags != "S.220" and i.tags != "S.221" and i.tags != "S.222" and i.tags != "S.223" and i.tags != "S.224" and i.tags != "S.225" and i.tags != "S.242" and i.tags != "S.241" and i.tags != "S.255" and i.tags != "S.254" and i.tags != "S.264" and i.tags != "S.263" and i.tags != "S.269" and i.tags != "S.268" and i.tags != "S.270" and i.tags != "S.266" and i.tags != "S.265" and i.tags != "S.257" and i.tags != "S.256" and i.tags != "S.244" and i.tags != "S.243" and i.tags != "S.227" and i.tags != "S.226" and i.tags != "S.81" and i.tags != "S.80" and i.tags != "S.79" and i.tags != "S.78" and i.tags != "S.77" and i.tags != "S.76" and i.tags != "S.75" and i.tags != "S.74" and i.tags != "S.55" and i.tags != "S.36" and i.tags != "S.37" and i.tags != "S.21" and i.tags != "S.22" and i.tags != "S.10" and i.tags != "S.11" and i.tags != "S.3" and i.tags != "S.4" and i.tags != "S.5" and i.tags != "S.6" and i.tags != "S.7" and i.tags != "S.17" and i.tags != "S.18" and i.tags != "S.32" and i.tags != "S.33" and i.tags != "S.51" and i.tags != "S.52" and i.tags != "S.72" and i.tags != "S.210" and i.tags != "S.211" and i.tags != "S.212" and i.tags != "S.213" and i.tags != "S.214" and i.tags != "S.215" and i.tags != "S.216" and i.tags != "S.217" and i.tags != "S.209" and i.tags != "S.240" and i.tags != "S.239" and i.tags != "S.253" and i.tags != "S.252" and i.tags != "S.262" and i.tags != "S.261" and i.tags != "S.267" and i.tags != "S.259" and i.tags != "S.258" and i.tags != "S.246" and i.tags != "S.245" and i.tags != "S.229" and i.tags != "S.228" and i.tags != "S.97" and i.tags != "S.89" and i.tags != "S.88" and i.tags != "S.87" and i.tags != "S.86" and i.tags != "S.85" and i.tags != "S.84" and i.tags != "S.83" and i.tags != "S.82" and i.tags != "S.56" and i.tags != "S.38" and i.tags != "S.39" and i.tags != "S.23" and i.tags != "S.24" and i.tags != "S.12" and i.tags != "S.13":
                openP.append(i)
    if (size_of_game == "9x9"):
        cL = 56
        cR = 89
        cRM = 267
        cLM = 6
        cLB = 72
        cRB = 217
        for i in hexagons:
            if i.tags != "S.0" and i.tags != "S.1" and i.tags != "S.2" and i.tags != "S.8" and i.tags != "S.9" and i.tags != "S.19" and i.tags != "S.20" and i.tags != "S.34" and i.tags != "S.35" and i.tags != "S.53" and i.tags != "S.54" and i.tags != "S.73" and i.tags != "S.218" and i.tags != "S.219" and i.tags != "S.220" and i.tags != "S.221" and i.tags != "S.222" and i.tags != "S.223" and i.tags != "S.224" and i.tags != "S.225" and i.tags != "S.242" and i.tags != "S.241" and i.tags != "S.255" and i.tags != "S.254" and i.tags != "S.264" and i.tags != "S.263" and i.tags != "S.269" and i.tags != "S.268" and i.tags != "S.270" and i.tags != "S.266" and i.tags != "S.265" and i.tags != "S.257" and i.tags != "S.256" and i.tags != "S.244" and i.tags != "S.243" and i.tags != "S.227" and i.tags != "S.226" and i.tags != "S.81" and i.tags != "S.80" and i.tags != "S.79" and i.tags != "S.78" and i.tags != "S.77" and i.tags != "S.76" and i.tags != "S.75" and i.tags != "S.74" and i.tags != "S.55" and i.tags != "S.36" and i.tags != "S.37" and i.tags != "S.21" and i.tags != "S.22" and i.tags != "S.10" and i.tags != "S.11" and i.tags != "S.3" and i.tags != "S.4":
                openP.append(i)
    if (size_of_game == "10x10"):
        cL = 36
        cR = 81
        cRM = 270
        cLM = 1
        cLB = 54
        cRB = 225
        openP = hexagons
    CornerLeft(canvas, hexagons[cL].y + 7, hexagons[cL].x - 22,"A-55")  # 5x5 : 115,   6x6: 106, 7x7: 98,  8x8:57,   9x9:  56, 10x10: 36
    CornerRight(canvas, hexagons[cR].y - 19, hexagons[cR].x - 22,"A-55")  # 5x5 : 119,   6x6: 111, 7x7: 104  8x8:96,   9x9:  89, 10x10: 81
    CornerRightMiddle(canvas, hexagons[cRM].y + 20, hexagons[cRM].x - 33, "A-55")  # 5x5 : 153,  6x6: 234, 7x7: 249, 8x8:260,  9x9:  267,10x10: 270
    CornerLeftMiddle(canvas, hexagons[cLM].y + 20, hexagons[cLM].x - 33, "A-55")  # 5x5 : 64,   6x6: 45,  7x7: 28,  8x8:15,   9x9:  6,  10x10: 1
    CornerLeftBottom(canvas, hexagons[cLB].y - 19, hexagons[cLB].x - 10, "A-55")  # 5x5 : 179,  6x6: 186, 7x7: 194, 8x8:71,   9x9:  72, 10x10: 54
    CornerRightBottom(canvas, hexagons[cRB].y + 57, hexagons[cRB].x - 10, "A-55")  # 5x5 : 183,  6x6: 191, 7x7: 200, 8x8:208,  9x9:  217,10x10: 225
