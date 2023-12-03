from math import prod

def parse_game(li):
    #return list of dicts like [{'red':2, 'blue':3}, {'red':5, 'green':7}]
    li = li.split(':')[-1]
    game = list()
    for r in li.split(';'):
        r_dict = dict()
        for s in r.split(','):
            s1, s2 = s.strip().split(' ')
            r_dict[s2] = int(s1)
        game.append(r_dict)
    return game

def is_possible(game, limits):
    for r_dict in game:
        for k, v in r_dict.items():
            if limits[k] < v:
                return False
    return True

def get_min_set_power(game):
    max_dict = dict()
    for r_dict in game:
        for k,v in r_dict.items():
            if max_dict.get(k, 0) < v:
                max_dict[k] = v
    return prod(max_dict.values())

def solve(fn, limits):
    with open(fn, 'r') as f:
        lines = f.readlines()
    possible_total = 0
    power_total = 0
    for i, li in enumerate(lines):
        game = parse_game(li)
        if is_possible(game, limits):
            possible_total += (i+1)
        power_total += get_min_set_power(game)
    return possible_total, power_total

def main():
    limits = {'red':12, 'green':13, 'blue':14}
    assert solve('test.txt', limits) == (8, 2286)
    part1, part2 = solve('input.txt', limits)
    print(part1)
    print(part2)

if __name__ == '__main__':
    main()
