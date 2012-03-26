import math
r1 = None
r2 = None
sw = None
pos = 0
while pos <= 60:
    if pos % 5 == 0:
        sw = 20
        r1 = 260
        r2 = 320
    else:
        sw = 10
        r1 = 280
        r2 = 320
    deg = pos * 6;
    rad = math.radians(deg)
    x1 = math.cos(rad) * r1
    y1 = math.sin(rad) * r1
    x2 = math.cos(rad) * r2
    y2 = math.sin(rad) * r2
    # print '<line x1="' + str(int(x1)) + '" y1="' + str(int(-y1)) + '" x2="' + str(int(x2)) +  '" y2="' + str(int(-y2)) + '" stroke="#202020" stroke-width="' + str(sw) + '" />'
    print '<line x1="' + str(x1) + '" y1="' + str(-y1) + '" x2="' + str(x2) +  '" y2="' + str(-y2) + '" stroke="#202020" stroke-width="' + str(sw) + '" />'
    pos = pos + 1
