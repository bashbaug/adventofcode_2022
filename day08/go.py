import sys

def checkBlockedU(lines, row, col, height):
    for u in range(row-1, -1, -1):
        check = int(lines[u][col])
        if check >= height:
            return True
    return False

def checkBlockedD(lines, row, col, height):
    for d in range(row+1, len(lines), 1):
        check = int(lines[d][col])
        if check >= height:
            return True
    return False

def checkBlockedL(lines, row, col, height):
    for l in range(col-1, -1, -1):
        check = int(lines[row][l])
        if check >= height:
            return True
    return False

def checkBlockedR(lines, row, col, height):
    for r in range(col+1, len(lines[row].strip()), 1):
        check = int(lines[row][r])
        if check >= height:
            return True
    return False

def checkVisibility(lines, row, col):
    height = int(lines[row][col])
    bu = checkBlockedU(lines, row, col, height)
    bd = checkBlockedD(lines, row, col, height)
    bl = checkBlockedL(lines, row, col, height)
    br = checkBlockedR(lines, row, col, height)
    return 0 if bu and bd and bl and br else 1

def countTreesU(lines, row, col, height):
    count = 0
    for u in range(row-1, -1, -1):
        count += 1
        check = int(lines[u][col])
        if check >= height:
            return count
    return count

def countTreesD(lines, row, col, height):
    count = 0
    for d in range(row+1, len(lines), 1):
        count += 1
        check = int(lines[d][col])
        if check >= height:
            return count
    return count

def countTreesL(lines, row, col, height):
    count = 0
    for l in range(col-1, -1, -1):
        count += 1
        check = int(lines[row][l])
        if check >= height:
            return count
    return count

def countTreesR(lines, row, col, height):
    count = 0
    for r in range(col+1, len(lines[row].strip()), 1):
        count += 1
        check = int(lines[row][r])
        if check >= height:
            return count
    return count

def getScenicScore(lines, row, col):
    height = int(lines[row][col])
    su = countTreesU(lines, row, col, height)
    sd = countTreesD(lines, row, col, height)
    sl = countTreesL(lines, row, col, height)
    sr = countTreesR(lines, row, col, height)
    return su * sd * sl * sr

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    visible = sum([checkVisibility(lines, row, col) for row, line in enumerate(lines) for col in range(len(line.strip()))])
    print('there are %d visible trees'%visible)

    score = max([getScenicScore(lines, row, col) for row, line in enumerate(lines) for col in range(len(line.strip()))])
    print('best scenic score is %d'%score)
