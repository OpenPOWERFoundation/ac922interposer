#!/usr/bin/python

# Create CSV file for KiPart

rows = 12
cols = 20

print('molex_impact_85ohm_left_and_right_guided_240pin_0.39mm')

print('pin,unit,name,type,side')

row_to_name = (
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'J',
    'K',
    'L',
    'M'
)

for col in range(cols):
    for row in range(rows):
        pin_nr = row+(col)*rows+1
        pin_name = '%c%d' % (row_to_name[row], col+1)
        side = 'right'
        print('%s,%s,%s,%s,%s' % (pin_nr, col+1, pin_name, 'bidirectional', side))
