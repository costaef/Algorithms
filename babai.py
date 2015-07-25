UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

def generate_grid(n, m):
    grid = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            grid.append(((i, j), 0)) # (i, j), visited
    return grid

def step_ahead(position):
    return [(position[0][0] + position[1][0], position[0][1] + position[1][1]), position[1]]

def turn_right(position):
    heading = position[1]
    if heading == UP:
        return [position[0], RIGHT]
    elif heading == RIGHT:
        return [position[0], DOWN]
    elif heading == DOWN:
        return [position[0], LEFT]
    elif heading == LEFT:
        return [position[0], UP]

def pos_string(pos):
    return 'Position: ' + str(pos[0]) + ' | Heading: ' + str(pos[1])

def  totalCellsVisited( n,  m):
    grid = generate_grid(n, m)
    babai_pos = [(1, 1), UP] # position, heading
    print pos_string(babai_pos)
    grid[0] = ((1, 1), 1)
    total = 1
    total_turns = 0
    completed = False
    while completed == False:
        new_pos = step_ahead(babai_pos)
        if (new_pos[0], 0) in grid:
            new_pos = turn_right(new_pos)
            babai_pos = new_pos
            print pos_string(babai_pos)
            i = grid.index((new_pos[0], 0))
            grid[i] = (new_pos[0], 1)
            total += 1
            total_turns = 0
        else:
            babai_pos = turn_right(babai_pos)
            total_turns += 1
            if total_turns > 4:
                completed = True
    return total

print totalCellsVisited(25, 40)
