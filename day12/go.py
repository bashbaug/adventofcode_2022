import sys

distmax = sys.maxsize

def printBoard(board):
    for r, row in enumerate(board):
        print('Row %2d: %s'%(r, row))
    print('')

def findMinDistance(distances, visited):
    coord = (0, 0, False)
    found = False
    dist = distmax
    for r in range(len(distances)):
        for c in range(len(distances[0])):
            if visited[r][c] == False and distances[r][c] < dist:
                dist = distances[r][c]
                coord = (r, c, True)
                found = True
    return coord

def djikstra(board, start, end):
    distances = [[distmax] * len(board[0]) for i in range(len(board))]
    distances[start[0]][start[1]] = 0

    visited = [[False] * len(board[0]) for i in range(len(board))]

    for count in range(len(board) * len(board[0])):
        (r, c, found) = findMinDistance(distances, visited)
        if found == False:
            break

        visited[r][c] = True

        if (r > 0 and
            ord(board[r-1][c]) <= ord(board[r][c]) + 1 and
            visited[r-1][c] == False and
            distances[r-1][c] > distances[r][c] + 1):
            distances[r-1][c] = distances[r][c] + 1
        if (r < len(board) - 1 and
            ord(board[r+1][c]) <= ord(board[r][c]) + 1 and
            visited[r+1][c] == False and
            distances[r+1][c] > distances[r][c] + 1):
            distances[r+1][c] = distances[r][c] + 1
        if (c > 0 and
            ord(board[r][c-1]) <= ord(board[r][c]) + 1 and
            visited[r][c-1] == False and
            distances[r][c-1] > distances[r][c] + 1):
            distances[r][c-1] = distances[r][c] + 1
        if (c < len(board[0]) - 1 and
            ord(board[r][c+1]) <= ord(board[r][c]) + 1 and
            visited[r][c+1] == False and
            distances[r][c+1] > distances[r][c] + 1):
            distances[r][c+1] = distances[r][c] + 1

    return distances[end[0]][end[1]]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    board = [list(line.strip()) for line in lines]
    #printBoard(board)

    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == 'S':
                start = (r, c)
                board[r][c] = 'a'
            if col == 'E':
                end = (r, c)
                board[r][c] = 'z'

    print('Starting coordinate: row = %d, col = %d'%start)
    print('Ending coordinate: row = %d, col = %d'%end)

    distance = djikstra(board, start, end)
    print('Part 1: Distance from start to end is %d'%distance)

    distmin = distmax
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if board[r][c] == 'a':
                distance = djikstra(board, (r, c), end)
                if distance < distmin:
                    distmin = distance
                    coordmin = (r, c)
        print('Part 2: Done with row %d: Shortest distance is %d from row = %d and col = %d'%(r, distmin, coordmin[0], coordmin[1]))
