from collections import deque


def solve(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    stack = deque([start])
    shape = (maze.height, maze.width)
    prev = [None] * (maze.width * maze.height)
    visited = [False] * (maze.width * maze.height)
    count = 0
    completed = False

    while stack:
        count += 1
        current = stack.pop()

        if current == end:
            completed = True
            break

        visited[current.Position[0] * width + current.Position[1]] = True

        for n in current.Neighbors:
            if n != None:
                n_pos = n.Position[0] * width + n.Position[1]
                if visited[n_pos] == False:
                    stack.append(n)
                    prev[n_pos] = current

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
