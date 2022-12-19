import sys

if __name__ == "__main__":
    reducer = 1
    monkeys = []
    with open(sys.argv[1]) as f:
        count = 0
        while True:
            monkeystr = f.readline().strip()
            if monkeystr == "": break
            #print('Read input for %s'%monkeystr)

            itemstr = f.readline()
            itemlist = [int(x) for x in itemstr.split(':')[1].split(',')]
            #print('Item list for monkey: %s'%itemlist)

            opstr = f.readline()
            operation = [x for x in opstr.split('=')[1].strip().split(' ')]
            #print('Operation for monkey: %s'%operation)

            teststr = f.readline()
            test = int(teststr.split('by')[1])
            #print('Test for monkey: %d'%test)

            truestr = f.readline()
            truethrow = int(truestr.split('monkey')[1])
            #print('True throw to monkey: %d'%truethrow)

            falsestr = f.readline()
            falsethrow = int(falsestr.split('monkey')[1])
            #print('False throw to monkey: %d'%falsethrow)

            blank = f.readline()
            #print('')

            monkey = {}
            monkey['items'] = itemlist
            monkey['op'] = operation
            monkey['test'] = test
            monkey['true'] = truethrow
            monkey['false'] = falsethrow
            monkey['count'] = 0

            reducer = reducer * test
            monkeys.append(monkey)

    #print('Monkeys: %s'%monkeys)

    #for round in range(20): # part 1
    for round in range(10000): # part 2
        for m, monkey in enumerate(monkeys):
            #print('Monkey %d:'%m)
            count = monkey['count']
            check = monkey['items']
            monkey['items'] = []
            for i, item in enumerate(check):
                count = count + 1
                #print('  Monkey inspects an item with a worry level of %d.'%item)
                new = item
                if monkey['op'][1] == '+':
                    if monkey['op'][2].isnumeric():
                        new = new + int(monkey['op'][2])
                    else:
                        new = new + new
                elif monkey['op'][1] == '*':
                    if monkey['op'][2].isnumeric():
                        new = new * int(monkey['op'][2])
                    else:
                        new = new * new
                else:
                    print('Unexpected op: %s'%monkey['op'][1])
                #print('    New worry level is %d.'%new)
                #new = new // 3 # part 1
                new = new % reducer # part 2
                #print('    Monkey gets bored with item. Worry level is divided by 3 to %d.'%new)
                if new % monkey['test'] == 0:
                    #print('    Current worry level is divisible by %d.'%monkey['test'])
                    #print('    Item with worry level %d is thrown to monkey %d.'%(new, monkey['true']))
                    monkeys[monkey['true']]['items'].append(new)
                else:
                    #print('    Current worry level is not divisible by %d.'%monkey['test'])
                    #print('    Item with worry level %d is thrown to monkey %d.'%(new, monkey['false']))
                    monkeys[monkey['false']]['items'].append(new)
            monkey['count'] = count
        #print('After round %d:'%round)
        #for m, monkey in enumerate(monkeys):
        #    print('Monkey %d: %s'%(m, monkey['items']))

    for m, monkey in enumerate(monkeys):
        print('Monkey %d inspected %d items.'%(m, monkey['count']))
    
    inspected = [monkey['count'] for monkey in monkeys]
    inspected.sort()
    print('two most active monkeys inspected %d and %d items'%(inspected[-1], inspected[-2]))
    print('monkey business is: %d'%(inspected[-1] * inspected[-2]))
