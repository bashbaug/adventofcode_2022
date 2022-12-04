import sys

# 1 = Rock, 2 = Paper, 3 = Scissors
values = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

outcomes = {'X': 0, 'Y': 3, 'Z': 6}

def score(line):
    opp, me = line.split()
    vm = values[me]
    vo = values[opp]

    outcome = 0
    if vm == vo: outcome = 3
    if vm == vo + 1: outcome = 6
    if vm == 1 and vo == 3: outcome = 6
    return vm + outcome

def score2(line):
    opp, outcome = line.split()
    vo = values[opp]

    if outcome == 'X': # lose
        if vo == 1:
            vm = 3
        else:
            vm = vo - 1
    if outcome == 'Y': # tie
        vm = vo
    if outcome == 'Z': # win
        if vo == 3:
            vm = 1
        else:
            vm = vo + 1
    return vm + outcomes[outcome]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    score = sum([score(line) for line in lines])
    print('Score is: %d'%score)

    score = sum([score2(line) for line in lines])
    print('Score2 is: %d'%score)

