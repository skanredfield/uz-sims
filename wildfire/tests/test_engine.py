import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "core"))

from src.core.engine import init_grid, logic_loop
from gui.ascii_gui import render_grid


grid = init_grid()
logic_loop(grid, render_grid)
render_grid(grid.tolist2d())
