import numpy
from scipy.spatial.transform.rotation import Rotation as r

orientations = [
    [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ],
    [
        [1,0,0],
        [0,0,-1],
        [0,1,0]
    ],
    [
        [1,0,0],
        [0,-1,0],
        [0,0,-1]
    ],
    [
        [1,0,0],
        [0,0,1],
        [0,-1,0]
    ],
    [
        [0,-1,0],
        [1,0,0],
        [0,0,1]
    ],
    [
        [0,0,1],
        [1,0,0],
        [0,1,0]
    ],
    [
        [0,1,0],
        [1,0,0],
        [0,0,-1]
    ],
    [
        [0,0,-1],
        [1,0,0],
        [0,-1,0]
    ],
    [
        [-1,0,0],
        [0,-1,0],
        [0,0,1]
    ],
    [
        [-1,0,0],
        [0,0,-1],
        [0,-1,0]
    ],
    [
        [-1,0,0],
        [0,1,0],
        [0,0,-1]
    ],
    [
        [-1,0,0],
        [0,0,1],
        [0,1,0]
    ],
    [
        [0,1,0],
        [-1,0,0],
        [0,0,1]
    ],
    [
        [0,0,1],
        [-1,0,0],
        [0,-1,0]
    ],
    [
        [0,-1,0],
        [-1,0,0],
        [0,0,-1]
    ],
    [
        [0,0,-1],
        [-1,0,0],
        [0,1,0]
    ],
    [
        [0,0,-1],
        [0,1,0],
        [1,0,0]
    ],
    [
        [0,1,0],
        [0,0,1],
        [1,0,0]
    ],
    [
        [0,0,1],
        [0,-1,0],
        [1,0,0]
    ],
    [
        [0,-1,0],
        [0,0,-1],
        [1,0,0]
    ],
    [
        [0,0,-1],
        [0,-1,0],
        [-1,0,0]
    ],
    [
        [0,-1,0],
        [0,0,1],
        [-1,0,0]
    ],
    [
        [0,0,1],
        [0,1,0],
        [-1,0,0]
    ],
    [
        [0,1,0],
        [0,0,-1],
        [-1,0,0]
    ]
]

class Scanner:
    def __init__(self):
        self.beacons = []
        self.orientation = orientations[0]
    def rotations(self):
        rots = []
        for o in orientations:
            rot = r.from_matrix(o)
            rots.append(r.apply(rot, self.beacons))
        return rots
    def distances(self):
        d = set()
        for b in self.beacons:
            for c in self.beacons:
                x,y,z = b[0]-c[0],b[1]-c[1],b[2]-c[2]
                d.add(int((x*x+y*y+z*z)**0.5))
        return d
    def match(self, other):
        pass

scanners = []
with open('testinput.in') as f:
    for line in f.readlines():
        line = line.strip()
        if line.count('scan'):
            scan = Scanner()
        elif line == '':
            scanners.append(scan)
        else:
            line = line.split(',')
            x,y,z = map(int, line)
            scan.beacons.append([x,y,z])

for s in scanners:
    for t in scanners:
        if s == t: continue
        d = s.distances().intersection(t.distances())
        if len(d) >= 66:
            print('hello')