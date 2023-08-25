from fibonacci_heap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ


def solve(maze):
    width = maze.width
    total = maze.width * maze.height

    start = maze.start
    end = maze.end
    end_pos = end.Position

    # so we don't return to the same node multiple times
    visited = [False] * total

    # link to the pervious node in the path
    previous = [None] * total

    # list of the best paths. better paths replace worse ones as we find them
    infinity = float("inf")
    distances = [infinity] * total

    # not sure which priority queue to use yet
    unvisited = HeapPQ()

    # Holds all priority queue nodes as they are created. We use this to decrease the key of a specific node when a shorter path is found.
    # This isn't hugely memory efficient, but likely to be faster than a dictionary
    node_index = [None] * total

    # Set the distance to the start to zero, and add it into the unvisited queue
    distances[start.Position[0] * width + start.Position[1]] = 0
    start_node = FibHeap.Node(0, start)
    node_index[start.Position[0] * width + start.Position[1]] = start_node
    unvisited.insert(start_node)

    # zero nodes visited, and not completed yet
    count = 0
    completed = False

    # Begin Dijkstra
    while len(unvisited) > 0:
        count += 1

        # Find the current shortest path point to explore
        n = unvisited.remove_minimum()

        # Current node u, all neighbors will be v
        u = n.value
        u_pos = u.Position
        u_pos_index = u_pos[0] * width + u_pos[1]

        if distances[u_pos_index] == infinity:
            break

        if u_pos == end_pos:
            # we're done!
            completed = True
            break

        for v in u.Neighbors:
            if v != None:
                v_pos = v.Position
                v_pos_index = v_pos[0] * width * v_pos[1]

                if visited[v_pos_index] == False:
                    # the extra distance from where we are (u_pos) to the neighbor (v_pos) -- manhattan distance
                    d = abs(v_pos[0] - u_pos[0]) + abs(v_pos[1] - u_pos[1])

                    # new path cost to v is distance to u + extra
                    new_distance = distances[u_pos_index] + d

                    # if this new distance is the new shortest path to v
                    if new_distance < distances[v_pos_index]:
                        v_node = node_index[v_pos_index]

                        # add it to the queue if it isn't already in there
                        if v_node == None:
                            v_node = FibHeap.Node(new_distance, v)
                            unvisited.insert(v_node)
                            node_index[v_pos_index] = v_node
                            distances[v_pos_index] = new_distance
                            previous[v_pos_index] = u
                        else:
                            unvisited.decrease_key(v_node, new_distance)
                            distances[v_pos_index] = new_distance
                            previous[v_pos_index] = u

        visited[u_pos_index] = True

    # Sanity check
    # We want to reconstruct the path. We start at the end, and then go previous[end] and follow all the previous[] links until we are back at the start
    from collections import deque

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = previous[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
