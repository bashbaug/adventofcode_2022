import sys

def check(cycle, reg):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        #print('at cycle %d reg has value %d so signal strength is %d'%(cycle, reg, cycle * reg))
        return cycle * reg
    return 0

def draw(cycle, reg, output):
    if (cycle - 1) % 40 == 0:
        print('output is: %s'%output)
        output = ""

    col = (cycle - 1) % 40
    #print('During cycle %2d: CRT draws in position %d'%(cycle, col))
    if abs(reg - col) <= 1:
        output += '#'
    else:
        output += '.'
    #print('Current CRT row: %s'%output)
    return output

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    reg = 1
    cycle = 0
    output = ""
    sum = 0
    for line in lines:
        cycle += 1
        #print('Start cycle   %2d: begin executing %s'%(cycle, line.strip()))
        sum += check(cycle, reg)
        output = draw(cycle, reg, output)
        if line.strip() != 'noop':
            (addx, cstr) = line.split()
            count = int(cstr)
            cycle += 1
            #print('')
            sum += check(cycle, reg)
            output = draw(cycle, reg, output)
            reg += count
        #print('End of cycle %2d: finish executing %s (register X is now %d)'%(cycle, line.strip(), reg))
        #print('')

    print('output is: %s'%output)

    print('sum of signal strengths is %d'%sum)
