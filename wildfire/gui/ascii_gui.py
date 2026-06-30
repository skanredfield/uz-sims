from rich import print
from rich.table import Table
from rich.text import Text
from rich import box
from rich.live import Live
import random
import time


# def render_grid(list2d: list[list[int]]):
#     line = "-" * (2 * len(list2d) + 1)
#     print(line)
#     for i in range(len(list2d)):
#         row = "|"
#         for j in range(len(list2d[i])):
#             match list2d[i][j]:
#                 case 1:
#                     row += " "
#                 case 2:
#                     row += "O"
#                 case 3:
#                     row += "T"
#                 case 4:
#                     row += "F"
#                 case 5:
#                     row += "C"
#                 case 6:
#                     row += "A"
#                 case _:
#                     row += "-"
#             row += "|"
#         print(row)
#         print(line)

mapping = {
    1: (" ", "default", "on black"),
    2: ("O", "bold white", "on bright_black"),     # e.g., Ocean / Water
    3: ("T", "bold white", "on brown"), # e.g., Tree / Forest
    4: ("F", "bold white", "on red"), # e.g., Fire / Hazard
    5: ("C", "bold white", "on dark_grey"),  # e.g., Coin / Treasure
    6: ("A", "bold white", "on light_grey"),    # e.g., Agent / Player
}

def _create_console_grid(list2d: list[list[int]]):
    grid = Table.grid(expand=False)
    grid.box = box.SQUARE
    grid.show_lines = True
    grid.show_edge = True

    for _ in range(len(list2d[0])):
        grid.add_column(min_width=3, justify="center")

    for row_data in list2d:
        row = []
        for val in row_data:
            char, fg, bg = mapping.get(val, ("-", "dim white", "on black"))
            # Text object allows styled background padding across the cell width
            cell_text = Text(char, style=f"{fg} {bg}")
            row.append(cell_text)
        grid.add_row(*row)

    # mapping = {1: " ", 2: "O", 3: "T", 4: "F", 5: "C", 6: "A"}

    # for row_data in list2d:
    #     row = [mapping.get(val, "-") for val in row_data]
    #     grid.add_row(*row)

    return grid

def render_grid(list2d: list[list[int]]):
    # rows, cols = 10, 10
    # current_map = [[random.randint(1, 7) for _ in range(cols)] for _ in range(rows)]
    with Live(_create_console_grid(list2d), auto_refresh=True):
        pass
    # with Live(_create_console_grid(list2d), refresh_per_second=4) as live:
    #     for _ in range(20): # Run for 20 frames
    #         time.sleep(0.25)
            
            # Simulate a world change or player movement
            # current_map = [[random.randint(1, 7) for _ in range(cols)] for _ in range(rows)]
            
            # Update the existing live canvas display smoothly
            # live.update(_create_console_grid(list2d))

