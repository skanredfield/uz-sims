import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src", "core"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "gui"))


from gui.qt_gui import QTRenderer
from src.core.engine import init_grid


class TestGridQt:

    def test_grid(self):
        grid = init_grid()
        renderer = QTRenderer()
        renderer.render_grid(grid.tolist2d())