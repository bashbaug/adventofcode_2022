import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    
    elves = []
    count = 0
    for line in lines:
        line = line.strip()
        if line == '':
            elves.append(count)
            count = 0
        else:
            count += int(line)

    #print('elves is %s'%elves)

    elves.sort()

    print('max is %d'%elves[-1])
    print('top three is %d'%(elves[-1]+elves[-2]+elves[-3]))
