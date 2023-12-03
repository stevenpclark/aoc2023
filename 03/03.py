from math import prod
import numpy as np
from scipy import ndimage

def solve(fn):
    with open(fn, 'r') as f:
        lines = [list(li) for li in f.read().splitlines()]

    m = np.array(lines, dtype=np.chararray)
    #pad matrix by one to simplify edge conditions
    m = np.pad(m, 1, constant_values='.')
    m_valid = np.zeros(shape=m.shape, dtype=bool)
    m_nums = np.zeros(shape=m.shape, dtype=int)
    nr, nc = m.shape

    for r, c in np.ndindex(nr, nc):
        ch = m[r,c]
        if ch != '.' and not ch.isnumeric():
            m_valid[r,c] = True

    kern = np.ones((3, 3), bool)
    m_valid = ndimage.binary_dilation(m_valid, kern)

    total = 0
    curr = 0
    curr_valid = False
    for r, c in np.ndindex(nr, nc):
        ch = m[r,c]
        if ch.isnumeric():
            if not curr:
                left = c
            curr = curr*10 + int(ch)
            curr_valid |= m_valid[r,c]
        else:
            if curr:
                m_nums[r,left:c] = curr
            total += curr_valid*curr
            curr = 0
            curr_valid = False

    gear_sum = 0
    for r in range(1, nr-1):
        for c in range(1, nc-1):
            if m[r,c] == '*':
                gear_sum += get_gear_ratio(m_nums, r, c)

    return total, gear_sum


def get_gear_ratio(m_nums, r, c):
    parts = list()
    nr, nc = m_nums.shape
    parts.append(m_nums[r,c-1])
    parts.append(m_nums[r,c+1])
    if m_nums[r-1,c]:
        parts.append(m_nums[r-1,c])
    else:
        parts.append(m_nums[r-1,c-1])
        parts.append(m_nums[r-1,c+1])
    if m_nums[r+1,c]:
        parts.append(m_nums[r+1,c])
    else:
        parts.append(m_nums[r+1,c-1])
        parts.append(m_nums[r+1,c+1])
    parts = list(filter(lambda n: n, parts))
    if len(parts) == 2:
        return prod(parts)
    else:
        return 0


def main():
    assert solve('test.txt') == (4361, 467835)
    print(solve('input.txt'))

if __name__ == '__main__':
    main()
