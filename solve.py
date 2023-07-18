from PIL import Image
import time
from mazes import Maze

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
