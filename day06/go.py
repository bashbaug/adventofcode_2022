import sys

def findStartOfPacket(line):
    pos = 4
    while True:
        chars = []
        chars[:0] = line[pos-4:pos]
        if len(set(chars)) == len(chars):
            return pos
        pos += 1

def findStartOfMessage(line):
    pos = 14
    while True:
        chars = []
        chars[:0] = line[pos-14:pos]
        if len(set(chars)) == len(chars):
            return pos
        pos += 1

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    for line in lines:
        ps = findStartOfPacket(line)
        ms = findStartOfMessage(line)
        print('Start of packet is %d, start of message is %d'%(ps, ms))
