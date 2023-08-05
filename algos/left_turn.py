from collections import deque


def solve(maze):
    path = deque([maze.start])
    current = maze.start.Neighbors[2]

    if current == None:
        return path

    heading = 2  # south
    turn = 1  # turning left, -1 for right
    start_pos = maze.start.Position
    end_pos = maze.end.Position

    # N E S W
    # 0 1 2 3

    count = 1
    completed = False

    while True:
        path.append(current)
        count += 1
        position = current.Position
        if position == start_pos or position == end_pos:
            if position == end_pos:
                completed = True
            break

        n = current.Neighbors
        if n[(heading - turn) % 4] != None:
            heading = (heading - turn) % 4
            current = n[heading]
            continue
        if n[heading] != None:
            current = n[heading]
            continue
        if [(heading + turn) % 4] != None:
            heading = (heading + turn) % 4
            current = n[heading]
            continue
        if n[(heading + 2) % 4] != None:
            heading = (heading + 2) % 4
            current = n[heading]
            continue

        completed = True
        break

    return [path, [count, len(path), completed]]
