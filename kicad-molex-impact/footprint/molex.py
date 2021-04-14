#!/usr/bin/python

import sys
import os
from KicadModTree import *

# Dimensions in mm

cols = 20
rows = 12

horizontal_pitch = 1.90
vertical_pitch = 1.35

through_hole_size = 0.39
top_pad = 0.80
# Kicad doesn't seem to support pad stacks yet
#bottom_pad = 0.71

horizontal_edge_keepout = 8.5
vertical_edge_keepout = (20.8 - 14.85) / 2

horizontal_keepout = 2*horizontal_edge_keepout + horizontal_pitch*(cols-1)
vertical_keepout = 2*vertical_edge_keepout + vertical_pitch*(rows-1)

npth_x = 8.5 - 4.75
npth_y = 20.8 - vertical_edge_keepout - 11.42
npth_drill = 3.56

footprint_name = "molex_impact_85ohm_left_and_right_guided_240pin_0.39mm"

# init kicad footprint
kicad_mod = Footprint(footprint_name)
kicad_mod.setDescription("Impact 85 Ohm Plus 4 Pair Vertical Header, Right Guided, Left Endwall, 10 Columns, 120 Circuits, Pin Length 4.90mm, Plated Through Hole Dimension 0.39mm, Lead Free")
#kicad_mod.setTags("example")

# set general values
kicad_mod.append(Text(type='reference', text='REF**', at=[horizontal_keepout/2.0, -(vertical_keepout+1)], layer='F.SilkS'))
kicad_mod.append(Text(type='value', text=footprint_name, at=[horizontal_keepout/2.0, -1.2], layer='F.Fab'))

# create silkscreen
kicad_mod.append(RectLine(start=[0, 0], end=[horizontal_keepout, -vertical_keepout], layer='F.SilkS'))

# create courtyard
kicad_mod.append(RectLine(start=[0, 0], end=[horizontal_keepout, -vertical_keepout], layer='F.CrtYd'))

for col in range(cols):
    for row in range(rows):
        x = horizontal_edge_keepout + col * horizontal_pitch
        #y = vertical_edge_keepout + row * vertical_pitch
        y = vertical_keepout - (vertical_edge_keepout + row * vertical_pitch)
        shape = Pad.SHAPE_CIRCLE
        if row == 0 and col == 0:
            shape = Pad.SHAPE_RECT
        pad_nr = 1 + col*rows + row
        kicad_mod.append(Pad(number=pad_nr, type=Pad.TYPE_THT, shape=shape,
                    # Is this the right size?
                    # How to get different bottom and top pad sizes
                     at=[x, -y], size=[top_pad, top_pad], drill=through_hole_size, layers=Pad.LAYERS_THT))

# non plated through holes
kicad_mod.append(Pad(number="", type=Pad.TYPE_NPTH, shape=Pad.SHAPE_CIRCLE,
                 at=[npth_x, -npth_y], size=npth_drill, drill=npth_drill, layers=Pad.LAYERS_NPTH))

kicad_mod.append(Pad(number="", type=Pad.TYPE_NPTH, shape=Pad.SHAPE_CIRCLE,
                 at=[horizontal_keepout-npth_x, -npth_y], size=npth_drill, drill=npth_drill, layers=Pad.LAYERS_NPTH))

# add model
#kicad_mod.append(Model(filename="example.3dshapes/example_footprint.wrl",
                       #at=[0, 0, 0], scale=[1, 1, 1], rotate=[0, 0, 0]))

# output kicad model
file_handler = KicadFileHandler(kicad_mod)
file_handler.writeFile('molex.kicad_mod')
