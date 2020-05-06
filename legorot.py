import math

def RadiusSquared(a, b):
    return a**2 + b**2

def GCD(a, b): 
   while(b): 
      a, b = b, a % b 
   return a

WIDTH = 2
HEIGHT = 2
MIN_CONNECTIONS = 3

inter_width = 2 * WIDTH
inter_height = 2 * HEIGHT
max_radius = int(math.ceil(
    math.sqrt(RadiusSquared(inter_width, inter_height))))

radius_map = {}
for i in xrange(max_radius + 1):
    for j in xrange(max_radius + 1):
        radius = RadiusSquared(i, j)
        if radius > 0 and radius <= max_radius**2:
            if radius in radius_map.keys():
                radius_map[radius].add((i, j))
            else:
                radius_map[radius] = {(i, j)}

angle_map = {}
for radius, positions in radius_map.items():
    for pos_fix in positions:
        for pos_rot in positions:
            if (pos_rot[0] <= inter_width and
                    pos_rot[1] <= inter_height):
                pos_wrp = pos_fix
                if pos_wrp[0] > pos_rot[0]:
                    pos_wrp = (-pos_wrp[1], pos_wrp[0])
                angle = (RadiusSquared(
                    pos_rot[0] - pos_wrp[0],
                    pos_rot[1] - pos_wrp[1]), 4 * radius)
                gcd = GCD(angle[0], angle[1])
                if gcd:
                    angle = (angle[0] / gcd, angle[1] / gcd)
                if angle in angle_map.keys():
                    angle_map[angle].add(pos_rot)
                else:
                    angle_map[angle] = {pos_rot}

for angle, connections in angle_map.items():
    connections.add((0, 0))
    if angle == (1, 2) or len(connections) < MIN_CONNECTIONS:
        del angle_map[angle]
        
for k, v in angle_map.items():
    print('{}: {}'.format(k, len(v)))
