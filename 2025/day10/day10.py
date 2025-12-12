from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


def read_input():
    machines = []
    with open("input.txt", "r") as file:
        for line in file:
            machines.append(parse_line(line.strip()))
    return machines


def parse_line(line):
    start = line.index('[') + 1
    end = line.index(']')
    diagram = line[start:end]
    
    target = 0
    for i, c in enumerate(diagram):
        if c == '#':
            target |= (1 << i)
    
    buttons = []
    button_indices = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            j = line.index(')', i)
            content = line[i+1:j]
            indices = []
            for x in content.split(','):
                indices.append(int(x))
            button_indices.append(indices)
            mask = 0
            for idx in indices:
                mask |= (1 << idx)
            buttons.append(mask)
            i = j + 1
        else:
            i += 1
    
    jstart = line.index('{') + 1
    jend = line.index('}')
    joltage_str = line[jstart:jend]
    joltage = []
    for x in joltage_str.split(','):
        joltage.append(int(x))
    
    return target, buttons, button_indices, joltage


def min_presses(target, buttons):
    n = len(buttons)
    for k in range(n + 1):
        for combo in combinations(range(n), k):
            state = 0
            for i in combo:
                state ^= buttons[i]
            if state == target:
                return k
    return -1


def min_joltage_presses(button_indices, joltage):
    n_buttons = len(button_indices)
    n_counters = len(joltage)
    
    A = np.zeros((n_counters, n_buttons))
    for i, indices in enumerate(button_indices):
        for j in indices:
            if j < n_counters:
                A[j][i] = 1
    
    c = np.ones(n_buttons)
    b = np.array(joltage, dtype=float)

    constraints = LinearConstraint(A, b, b)    
    max_val = max(joltage) if joltage else 100
    bounds = Bounds(lb=0, ub=max_val * 10)
    integrality = np.ones(n_buttons)
    
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        return int(round(result.fun))
    return -1


def day10_easy():
    machines = read_input()
    total = 0
    for target, buttons, button_indices, joltage in machines:
        total += min_presses(target, buttons)
    print(total)


def day10_diff():
    machines = read_input()
    total = 0
    for target, buttons, button_indices, joltage in machines:
        total += min_joltage_presses(button_indices, joltage)
    print(total)


if __name__ == "__main__":
    day10_easy()
    day10_diff()