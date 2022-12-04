import sys

def priority(item):
    o = ord(item)
    if o >= ord('a') and o <= ord('z'):
        return o - ord('a') + 1
    if o >= ord('A') and o <= ord('Z'):
        return o - ord('A') + 27
    print('unexpected!')
    return 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        line = line.strip()
        beg = line[:len(line)//2]
        end = line[len(line)//2:]
        #print('Begin: %s    End: %s'%(beg, end))
        for c in beg:
            if c in end:
                #print('found item %s!'%c)
                sum += priority(c)
                break
    print('Sum of item priorities: %d'%sum)

    sum = 0
    for g in range(len(lines)//3):
        rs0 = lines[g * 3 + 0]
        rs1 = lines[g * 3 + 1]
        rs2 = lines[g * 3 + 2]
        for c in rs0:
            if c in rs1 and c in rs2:
                #print('found badge %s!'%c)
                sum += priority(c)
                break
    print('Sum of badge priorities: %d'%sum)
