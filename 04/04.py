def get_match_counts(fn):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    match_counts = list()
    for li in lines:
        li = li.split(':')[-1]
        targets, hand = li.split('|')
        targets = set(int(s) for s in targets.split())
        hand = set(int(s) for s in hand.split())
        matches = hand.intersection(targets)
        match_counts.append(len(matches))
    return match_counts

def solve(fn):
    match_counts = get_match_counts(fn)
    part1 = 0
    part2 = 0
    copies = [1,]*len(match_counts)
    for mc in match_counts:
        if mc:
            part1 += 2**(mc-1)
        num_copies = copies.pop(0)
        for i in range(mc):
            copies[i] += num_copies
        part2 += num_copies
    return part1, part2

def main():
    assert solve('test.txt') == (13, 30)
    print(solve('input.txt'))

if __name__ == '__main__':
    main()
