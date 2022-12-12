import sys

def nextPosition(hx, hy, tx, ty):
    dx = hx - tx
    dy = hy - ty
    if abs(dx) <= 1 and abs(dy) <= 1:
        return (tx, ty)
    if dx == 0:
        ty += 1 if dy > 0 else -1
    elif dy == 0:
        tx += 1 if dx > 0 else -1
    else:
        tx += 1 if dx > 0 else -1
        ty += 1 if dy > 0 else -1
    return (tx, ty)

xmoves = {'R': 1, 'L': -1, 'U': 0, 'D':  0}
ymoves = {'R': 0, 'L':  0, 'U': 1, 'D': -1}

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # H -> T
    sropex = [0, 0]
    sropey = [0, 0]

    lropex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lropey = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    shortseen = set()
    shortseen.add((sropex[-1], sropey[-1]))

    longseen = set()
    longseen.add((lropex[-1], lropey[-1]))

    for line in lines:
        (dir, cstr) = line.strip().split()
        count = int(cstr)
        dx = xmoves[dir]
        dy = ymoves[dir]

        #print('Moving %d steps in the direction [%d, %d]'%(count, dx, dy))
        for step in range(count):
            sropex[0] += dx
            sropey[0] += dy
            lropex[0] += dx
            lropey[0] += dy
            for knot in range(len(sropex)-1):
                (sropex[knot+1], sropey[knot+1]) = nextPosition(sropex[knot], sropey[knot], sropex[knot+1], sropey[knot+1])
            for knot in range(len(lropex)-1):
                (lropex[knot+1], lropey[knot+1]) = nextPosition(lropex[knot], lropey[knot], lropex[knot+1], lropey[knot+1])
            #print('    step %d: head is [%d, %d], tail is [%d, %d]'%(step, sropex[0], sropey[0], sropex[-1], sropey[-1]))
            shortseen.add((sropex[-1], sropey[-1]))
            longseen.add((lropex[-1], lropey[-1]))

    print('Found %d unique short rope positions'%len(shortseen))
    print('Found %d unique long rope positions'%len(longseen))
