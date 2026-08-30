import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "core"))

from src.core.grid_generator import GridGenerator
from gui.console_gui import ConsoleRenderer
from src.core.engine import init_grid


renderer = ConsoleRenderer()
# grid = GridGenerator.generate_empty(10, 10)
# grid.set_cell_type(5, 5, 5)
grid = init_grid()

current_grid = grid.tolist2d()
renderer.render_grid(current_grid)
renderer.refresh_grid(current_grid)
