from maze import Maze
class Renderer:
    # def render(self, maze: Maze) -> None:
        # for row in maze.grid:
        #     for _ in row:
        #         print("[ ]", end=" ")
        #     print()
        
        
        # print()
        # print("==================Hex Value =================")
        # for row in maze.grid:
        #     line = "".join(cell.hex_value for cell in row)
        #     print(line)

        
    CELL_WIDTH = 5
    CELL_HEIGHT = 3

    def _draw_top(self, cols: int) -> None:
        print("┌", end="")

        for col in range(cols):
            print("─" * self.CELL_WIDTH, end="")

            if col == cols - 1:
                print("┐")
            else:
                print("┬", end="")

    def _draw_middle(self, cols: int) -> None:

        for _ in range(self.CELL_HEIGHT):

            print("│", end="")

            for col in range(cols):
                print(" " * self.CELL_WIDTH, end="")

                if col == cols - 1:
                    print("│", end="")
                else:
                    print("│", end="")

            print()

    def _draw_separator(self, cols: int) -> None:
        print("├", end="")

        for col in range(cols):
            print("─" * self.CELL_WIDTH, end="")

            if col == cols - 1:
                print("┤")
            else:
                print("┼", end="")

    def _draw_bottom(self, cols: int) -> None:
        print("└", end="")

        for col in range(cols):
            print("─" * self.CELL_WIDTH, end="")

            if col == cols - 1:
                print("┘")
            else:
                print("┴", end="")

    def render(self, maze: Maze) -> None:

        for row_index in range(maze.rows):

            # First row
            if row_index == 0:
                self._draw_top(maze.cols)

            # Cell contents
            self._draw_middle(maze.cols)

            # Separator or bottom
            if row_index == maze.rows - 1:
                self._draw_bottom(maze.cols)
            else:
                self._draw_separator(maze.cols)


        print()
        print("==================Hex Value =================")
        for row in maze.grid:
            line = "".join(cell.hex_value for cell in row)
            print(line)

    