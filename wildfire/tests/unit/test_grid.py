import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src", "core"))

from src.core.grid_generator import GridGenerator


class TestGrid:

    def test_empty_grid(self):
        grid = GridGenerator.generate_empty(100, 100)
        assert grid.num_rows == 100
        assert grid.num_cols == 100