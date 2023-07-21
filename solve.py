from PIL import Image
import time
from mazes import Maze
from factory import SolverFactory

Image.MAX_IMAGE_PIXELS = None

# read cmd line arguments
import argparse


def solve(factory, method, input_file, output_file):
    # load image
    print("Loading Image")
    im = Image.open(input_file)

    # Creat the maze and time it.
    print("Creating maze")
    t0 = time.time()
    maze = Maze(im)
    t1 = time.time()
    print("Node Count:", maze.count)
    total = t1 - t0
    print("Time Elapsed", total, "\n")

    # Create and run solver
    [title, solver] = factory.creates_solver(method)
    print("Starting solve:", title)

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    print("Node explored", stats[0])
    if stats[2]:
        print("Path found, length", stats[1])
    else:
        print("No path found")
    print("Time elapsed: ", total, "\n")

    """
    Create and save the output image.
    This is a simple drawing code that travels between each node in turn, drawing either
    a horiztontal or vertical line. Line color is roughly interpolated between between 
    blue and red depending on how far down the path this section is.
    """

    print("Saving image")
    im = im.convert("RGB")
    impixels = im.load()

    result_path = [n.Position for n in result]
    length = len(result_path)

    for i in range(0, length - 1):
        a = result_path[i]
        b = result_path[i + 1]

        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # horizontal line -- y is equal
            impixels[x, a[0]] = px
        elif a[1] == b[1]:
            # vertical line -- x is equal
            for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                impixels[a[1], y] = px

    im.save(output_file)


def main():
    sf = SolverFactory()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--method",
        nargs="?",
        const=sf.Default,
        default=sf.Default,
        choices=sf.Choices,
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    solve(sf, args.method, args.input_file, args.output_file)


if __name__ == "__main__":
    main()
