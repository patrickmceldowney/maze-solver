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
        topnodes = [None] * width
        count = 0

        for x in range (1, width - 1):
          if data[x] > 0:
            self.start = Maze.Node((0, x))
            topnodes[x] = self.start
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

          for x in range (1, width - 1):
            # Read the image once per pixel (marginal optimization)
            prv = cur
            cur = nxt
            nxt = data[row_offset + x + 1] > 0



            
