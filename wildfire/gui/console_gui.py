from rich import print
from rich.table import Table
from rich.text import Text
from rich import box
from rich.live import Live


class ConsoleRenderer:

    mapping = {
        1: (" ", "default", "on black"),
        2: ("O", "bold white", "on bright_black"),     # e.g., Ocean / Water
        3: ("T", "bold white", "on brown"), # e.g., Tree / Forest
        4: ("F", "bold white", "on red"), # e.g., Fire / Hazard
        5: ("C", "bold white", "on dark_grey"),  # e.g., Coin / Treasure
        6: ("A", "bold white", "on light_grey"),    # e.g., Agent / Player
    }

    def __init__(self):
        self.live = None

    def _create_console_grid(self, list2d: list[list[int]]):
        grid = Table.grid(expand=False)
        grid.box = box.SQUARE
        grid.show_lines = True
        grid.show_edge = True

        for _ in range(len(list2d[0])):
            grid.add_column(min_width=3, justify="center")

        for row_data in list2d:
            row = []
            for val in row_data:
                char, fg, bg = ConsoleRenderer.mapping.get(val, ("-", "dim white", "on black"))
                cell_text = Text(char, style=f"{fg} {bg}")
                row.append(cell_text)
            grid.add_row(*row)

        return grid

    def render_grid(self, list2d: list[list[int]]):
        self.live = Live(self._create_console_grid(list2d), auto_refresh=True)
        self.live.start()
        
    def refresh_grid(self, list2d: list[list[int]]):
        self.live.update(self._create_console_grid(list2d))

    def finalize_rendering(self):
        self.live.stop()

