import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "core"))

from src.core.grid_generator import GridGenerator
from gui.ascii_gui import render_grid


grid = GridGenerator.generate_empty(10, 10)
grid.set_cell_type(5, 5, 5)
render_grid(grid.tolist2d())
