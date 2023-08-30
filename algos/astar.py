from fibonacci_heap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This is nearly identical to Dijkstra's


def solve(maze):
    width = maze.width
    total = maze.width * maze.height
    start = maze.start
    start_pos = start.Position
    end = maze.end
    end_pos = end.Position
    visited = [False] * total
    prev = [None] * total
    infinity = float("inf")
    distances = [infinity] * total

    # The priority queue. There are multiple implementations in priority queue
    unvisited = FibPQ()

    node_index = [None] * total
    distances[start.Position[0] * width + start.Position[1]] = 0
    start_node = FibHeap.Node(0, start)
    node_index[start.Position[0] * width + start.Position[1]] = start_node
    unvisited.insert(start_node)

    count = 0
    completed = False

    while len(unvisited) > 0:
        count += 1
        n = unvisited.remove_minimum()
        u = n.value
        u_pos = u.Position
        u_pos_index = u_pos[0] * width + u_pos[1]

        if distances[u_pos_index] == infinity:
            break

        if u_pos == end_pos:
            completed = True
            break

        for v in u.Neighbors:
            if v != None:
                v_pos = v.Position
                v_pos_index = v_pos[0] * width + v_pos[1]

                if visited[v_pos_index] == False:
                    d = abs(v_pos[0] - u_pos[0]) + abs(v_pos[1] - u_pos[1])

                    # New path to V is distance to U + extra (g cost).
                    # New distance is the distances of the path from the start, though U, to V
                    new_distance = distances[u_pos_index] + d

                    # Remaining cost (f cost). Use manhattan distance to calculate the distance from
                    # V to the end.
                    remaining = abs(v_pos[0] - end_pos[0]) + abs(v_pos[1] - end_pos[1])

                    # We don't inlcude f cost in this first check. We want to know that the path "to" our node V is shortest
                    if new_distance < distances[v_pos_index]:
                        v_node = node_index[v_pos_index]

                        if v_node == None:
                            # V goes into the priority queue with a cost of g + f. So if it's moving closer to the end, it'll get higher
                            # priority than some other nodes. The order we visit nodes is a trade-off between a short path, and moving
                            # closer to the goal.
                            v_node = FibHeap.Node(new_distance + remaining, v)
                            unvisited.insert(v_node)
                            node_index[v_pos_index] = v_node
                            # The distance to the node remains just g
                            distances[v_pos_index] = new_distance
                            prev[v_pos_index] = u
                    else:
                        # As above, we decrease the node since we've found a new path. But include the distance remaining (f cost)
                        unvisited.decrease_key(v_node, new_distance + remaining)
                        distances[v_pos_index] = new_distance
                        prev[v_pos_index] = u

        visited[u_pos_index] = True

    from collections import deque

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
