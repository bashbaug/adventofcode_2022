import sys
import functools
import json

def comparePackets(packet0, packet1):
    for i in range(len(packet0)):
        if i >= len(packet1):
            #print('Right side ran out of items --> out of order.')
            return 1
        if isinstance(packet0[i], int) and isinstance(packet1[i], int):
            if packet0[i] < packet1[i]:
                #print('Left side is smaller --> in order.')
                return -1
            if packet0[i] > packet1[i]:
                #print('Right side is smaller --> out of order.')
                return 1
        elif isinstance(packet0[i], int):
            #print('Mixed types... converting left and comparing.')
            c = comparePackets([packet0[i]], packet1[i])
            if c != 0: return c
        elif isinstance(packet1[i], int):
            #print('Mixed types... converting right and comparing.')
            c = comparePackets(packet0[i], [packet1[i]])
            if c != 0: return c
        else:
            c = comparePackets(packet0[i], packet1[i])
            if c != 0: return c
    if len(packet0) == len(packet1):
        #print('Right side equals left side.')
        return 0
    #print('Ran out of left items to compare --> in order.')
    return -1

if __name__ == "__main__":
    allpackets = []
    packetpair = 1
    sum = 0
    with open(sys.argv[1]) as f:
        while True:
            line0 = f.readline()
            if line0 == "": break

            packet0 = json.loads(line0)
            packet1 = json.loads(f.readline())
            blank = f.readline()

            #print('Evaluating packet pair %d...'%packetpair)
            #print('Packet 0: %s'%packet0)
            #print('Packet 1: %s'%packet1)
            allpackets.append(packet0)
            allpackets.append(packet1)
            ordered = comparePackets(packet0, packet1)
            if ordered <= 0: sum += packetpair
            #print('Current sum is: %d'%sum)
            #print('')
            packetpair += 1

    print('sum of ordered packets is %d'%sum)

    allpackets.append([[2]])
    allpackets.append([[6]])
    sortedpackets = sorted(allpackets, key=functools.cmp_to_key(comparePackets))

    first = sortedpackets.index([[2]]) + 1
    second = sortedpackets.index([[6]]) + 1
    print('first = %d, second = %d, product = %d'%(first, second, first * second))
