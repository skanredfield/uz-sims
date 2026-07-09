import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "core"))

import time
from src.core.appstate import AppState
from src.core.engine import init_grid, logic_loop
from gui.ascii_gui import ConsoleRenderer

appstate = AppState()
grid = init_grid()
renderer = ConsoleRenderer()

try:
    renderer.render_grid(grid.tolist2d(), appstate)
    time.sleep(1)
    while(True):
        logic_loop(grid, appstate)
        renderer.refresh_grid(grid.tolist2d(), appstate)
finally:
    renderer.finalize_rendering()
