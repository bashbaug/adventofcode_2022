import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    contained = 0
    overlapped = 0
    for line in lines:
        line = line.strip()
        (f, s) = line.split(',')
        (fs, fe) = f.split('-')
        (ss, se) = s.split('-')
        #print('first = %d to %d, second = %d to %d'%(int(fs), int(fe), int(ss), int(se)))
        if int(fs) >= int(ss) and int(fe) <= int(se):
            contained += 1
        elif int(ss) >= int(fs) and int(se) <= int(fe):
            contained += 1
        if int(fs) >= int(ss) and int(fs) <= int(se):
            overlapped += 1
        elif int(ss) >= int(fs) and int(ss) <= int(fe):
            overlapped += 1

    print('number of contained assignments: %d'%contained)
    print('number of overlapping assignments: %d'%overlapped)