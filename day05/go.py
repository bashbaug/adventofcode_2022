import sys
import re

def parseState(initial):
    state = {}
    for line in initial[:-1]:
        stack = 1
        pos = 1
        while pos < len(line):
            state.setdefault(stack, [])
            if line[pos] != ' ':
                state[stack].insert(0, line[pos])
            stack += 1
            pos += 4
    return state

def getCode(state):
    code = ''
    for stack in state:
        code = code + state[stack][-1]
    return code

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    empty = lines.index('\n')
    initial = lines[:empty]

    state = parseState(initial)

    commands = lines[empty + 1:]
    for command in commands:
        t = re.search('^move (\d+) from (\d+) to (\d+)', command)
        count = int(t.group(1))
        src = int(t.group(2))
        dst = int(t.group(3))
        for i in range(count):
            v = state[src][-1]
            state[src] = state[src][:-1]
            state[dst].append(v)

    print('original code is %s'%getCode(state))

    state = parseState(initial)

    commands = lines[empty + 1:]
    for command in commands:
        t = re.search('^move (\d+) from (\d+) to (\d+)', command)
        count = int(t.group(1))
        src = int(t.group(2))
        dst = int(t.group(3))
        moved = []
        for i in range(count):
            v = state[src][-1]
            moved.insert(0, v)
            state[src] = state[src][:-1]
        for v in moved:
            state[dst].append(v)

    print('new code is %s'%getCode(state))
