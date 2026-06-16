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
    CELL_HEIGHT = 2

    TOP_LEFT = "┏"
    TOP_RIGHT = "┓"
    BOTTOM_LEFT = "┗"
    BOTTOM_RIGHT = "┛"

    VERTICAL = "┃"
    HORIZONTAL = "━"

    LEFT_T = "┣"
    RIGHT_T = "┫"

    TOP_T = "┳"
    BOTTOM_T = "┻"

    CROSS = "╋"


    def _draw_top(self, cols: int) -> None:

        print(self.TOP_LEFT, end="")

        for col in range(cols):

            print(
                self.HORIZONTAL * self.CELL_WIDTH,
                end=""
            )

            if col == cols - 1:
                print(self.TOP_RIGHT)
            else:
                print(self.TOP_T, end="")

    def _draw_middle(self, cols: int) -> None:

        for _ in range(self.CELL_HEIGHT):

            print(self.VERTICAL, end="")

            for col in range(cols):

                print(
                    " " * self.CELL_WIDTH,
                    end=""
                )

                print(self.VERTICAL, end="")

            print()

    def _draw_separator(self, cols: int) -> None:

        print(self.LEFT_T, end="")

        for col in range(cols):

            print(
                self.HORIZONTAL * self.CELL_WIDTH,
                end=""
            )

            if col == cols - 1:
                print(self.RIGHT_T)
            else:
                print(self.CROSS, end="")

    def _draw_bottom(self, cols: int) -> None:

        print(self.BOTTOM_LEFT, end="")

        for col in range(cols):

            print(
                self.HORIZONTAL * self.CELL_WIDTH,
                end=""
            )

            if col == cols - 1:
                print(self.BOTTOM_RIGHT)
            else:
                print(self.BOTTOM_T, end="")

    def render(self, maze: Maze) -> None:

        for row_index in range(maze.rows):

            if row_index == 0:
                self._draw_top(maze.cols)

            self._draw_middle(maze.cols)

            if row_index == maze.rows - 1:
                self._draw_bottom(maze.cols)
            else:
                self._draw_separator(maze.cols)

        print()
        print("==================Hex Value =================")
        for row in maze.grid:
            line = "".join(cell.hex_value for cell in row)
            print(line)


    

    