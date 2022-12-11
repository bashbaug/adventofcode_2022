import sys

filesystem = {}
root = {}

def parse(current, lines, ln):
    while ln < len(lines):
        line = lines[ln].strip()
        #print('line is: %s'%line)
        ln = ln + 1
        if line == '$ cd /':
            #print('Changing directory to root...')
            current = root
        elif line == '$ ls':
            #print('Listing directory contents...')
            while ln < len(lines) and lines[ln][0] != '$':
                (f, s) = lines[ln].strip().split(' ')
                if f == 'dir':
                    #print('Found directory %s'%s)
                    current[s] = {}
                else:
                    #print('Found file %s with size %d'%(s, int(f)))
                    current[s] = int(f)
                ln = ln + 1
        elif line == '$ cd ..':
            #print('Returning up a directory...')
            return ln
        else: # '$ cd <dir>':
            (d0, d1, dir) = line.strip().split(' ')
            #print('Changing to directory %s'%dir)
            ln = parse(current[dir], lines, ln)
    return ln

def checkSizesPartA(sizes, totalsum, current, label):
    localsum = 0
    for check in current:
        #print('Checking %s...'%check)
        if isinstance(current[check], dict):
            #print('Recursing into %s'%check)
            (t, l) = checkSizesPartA(sizes, totalsum, current[check], check)
            totalsum = t
            localsum += l
        else:
            #print('Adding %s size %d to localsum.'%(check, current[check]))
            localsum += current[check]
    if localsum <= 100000:
        totalsum += localsum
    #print('Local sum for %s is %d, total sum is %d'%(label, localsum, totalsum))
    sizes[label] = localsum
    return (totalsum, localsum)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    filesystem['/'] = root

    parse(root, lines, 0)

    #print('Filesystem is: %s'%filesystem)

    sizes = {}
    (totalsum, localsum) = checkSizesPartA(sizes, 0, root, '/')
    print('total sum is %d'%totalsum)

    #print('sizes is %s'%sizes)

    free = 70000000 - sizes['/']
    need = 30000000 - free
    print('free space = %d, need %d'%(free, need))

    name = '/'
    closest = sizes['/']
    for dir in sizes:
        if sizes[dir] >= need and sizes[dir] < closest:
            name = dir
            closest = sizes[dir]
    print('should delete dir %s with size %d'%(name, closest))
