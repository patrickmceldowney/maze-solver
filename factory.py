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
            from algos.depth_first import solve

            return ["Depth First", solve]
        elif type == "dijkstra":
            from algos.dijkstra import solve

            return ["Dijkstra's Algorithm", solve]
        elif type == "astar":
            from algos.astar import solve

            return ["A*", solve]
        elif type == "breadth_first":
            from algos.breadth_first import solve

            return ["Breadth First", solve]
