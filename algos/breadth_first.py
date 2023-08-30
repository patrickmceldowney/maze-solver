from collections import deque


def solve(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    total = maze.width * maze.height
    queue = deque([start])
    shape = (maze.height, maze.width)
    prev = [None] * total
    visited = [False] * total
    count = 0
    completed = False

    visited[start.Position[0] * width + start.Position[1]] = True

    while queue:
        count += 1
        current = queue.pop()

        if current == end:
            completed = True
            break

        for n in current.Neighbors:
            if n != None:
                n_pos = n.Position[0] * width + n.Position[1]
                if visited[n_pos] == False:
                    queue.appendleft(n)
                    visited[n_pos] = True
                    prev[n_pos] = current

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
