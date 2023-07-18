class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbors = [None, None, None, None]

    def __init__(self, im):
        width = im.size[0]
        height = im.size[1]
        data = list(im.getdata(0))

        self.start = None
        self.end = None

        # Top row buffer
        top_nodes = [None] * width
        count = 0

        for x in range(1, width - 1):
            if data[x] > 0:
                self.start = Maze.Node((0, x))
                top_nodes[x] = self.start
                count += 1
                break

        for y in range(1, height - 1):
            row_offset = y * width
            row_above_offset = row_offset - width
            row_below_offset = row_offset + width

            prv = False
            cur = False
            nxt = data[row_offset + 1] > 0

            left_node = None

            for x in range(1, width - 1):
                # Read the image once per pixel (marginal optimization)
                prv = cur
                cur = nxt
                nxt = data[row_offset + x + 1] > 0

                n = None

                if cur == False:
                    # on wall - no action
                    continue

                if prv == True:
                    if next == True:
                        # Path Path Path
                        # Create node only if paths above or below
                        if (
                            data[row_above_offset + x] > 0
                            or data[row_above_offset + x] > 0
                        ):
                            n = Maze.Node((y, x))
                            left_node.Neighboers[1] = n
                            n.Neighbors[3] = left_node
                            left_node = n
                    else:
                        # path path wall
                        # create path at end of corridor
                        n = Maze.Node((y, x))
                        left_node.Neighbors[1] = n
                        n.Neighbors[3] = left_node
                        left_node = None
                else:
                    if nxt == True:
                        # wall wall path
                        # create path at start of corridor
                        n = Maze.Node((y, x))
                        left_node = n
                    else:
                        # wall path path
                        # create node only if in dead end
                        if (data[row_above_offset + x] == 0) or (
                            data[row_below_offset + x] == 0
                        ):
                            n = Maze.Node((y, x))

            # If node isn't none, we can assume we can connect N-S somewhere
            if n != None:
                # clear above, connect to top node
                if data[row_above_offset + x] > 0:
                    t = top_nodes[x]
                    t.Neighbors[2] = n
                    n.Neighbors[0] = t

                # if clear below, put this new node in the top row for next connection
                if data[row_below_offset + x] > 0:
                    top_nodes[x] = n
                else:
                    top_nodes[x] = None

                count += 1

        # end row
        row_offset = (height - 1) * width
        for x in range(1, width - 1):
            if data[row_offset + x] > 0:
                self.end = Maze.Node((height - 1, x))
                t = top_nodes[x]
                t.Neighbors[2] = self.end
                self.end.Neighbors[0] = t
                count += 1
                break

        self.count = count
        self.width = width
        self.height = height
