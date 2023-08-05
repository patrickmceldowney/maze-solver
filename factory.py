# Simple factory class that imports and returns a relveant solver when provided a string


class SolverFactory:
    def __init__(self) -> None:
        self.Default = "breadth_first"
        self.Choices = [
            "breadth_first",
            "depth_first",
            "dijkstra",
            "astar",
            "left_turn",
        ]

    def create_solver(self, type):
        if type == "left_turn":
            from algos.left_turn import solve

            return ["Left turn only", solve]
        elif type == "depth_first":
            # import depth_first
            print("Depth first search")
        elif type == "dijkstra":
            # import dijkstra
            print("Dijkstra's Algorithm")
        elif type == "astar":
            # import astar
            print("A-star search")
        elif type == "breadth_first":
            # import breadth_first
            print("Breadth first search")
