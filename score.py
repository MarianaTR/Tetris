

def line_completed_score(line, level):
    if line == 1:
        return 100 * level
    elif line == 2:
        return 300 * level
    elif line == 3:
        return 500 * level
    elif line == 4:
        return 800 * level

def perfect_clear(grid, level, line):
    if grid.is_perfect_clean():
        if line == 1:
            return 800 * level
        elif line == 2:
            return 1200 * level
        elif line == 3:
            return 1800 * level
        elif line == 4:
            return 2000 * level
    return 0

def combo(level, combo_count):
    return 50 * combo_count * level

def hard_drop():
    pass