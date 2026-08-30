import sys
from typing import ClassVar

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget


class _ColorBlock(QWidget):
    def __init__(self, color_name_or_hex):
        super().__init__()
        
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color_name_or_hex))
        self.setPalette(palette)

class _MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Grid App")
        self.resize(400, 400)

        layout = QGridLayout()

        for x in range(10):
            for y in range(10):
                layout.addWidget(_ColorBlock("grey"), x, y)

        palette = layout.itemAtPosition(5, 5).widget().palette()
        palette.setColor(QPalette.Window, QColor("tomato"))
        layout.itemAtPosition(5, 5).widget().setPalette(palette)

        # grid.set_cell_type(4, 4, CellType.FOREST)
        # grid.set_cell_type(4, 5, CellType.FOREST)
        # grid.set_cell_type(4, 6, CellType.FOREST)
        # grid.set_cell_type(5, 4, CellType.FOREST)
        # grid.set_cell_type(5, 6, CellType.FOREST)
        # grid.set_cell_type(6, 4, CellType.FOREST)
        # grid.set_cell_type(6, 5, CellType.FOREST)
        # grid.set_cell_type(6, 6, CellType.FOREST)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class QTRenderer:

    mapping: ClassVar[dict[int, tuple[str, str, str]]] = {
        1: (" ", "default", "on black"),
        2: ("O", "bold white", "on bright_white"),
        3: ("T", "bold white", "on green"),
        4: ("F", "bold white", "on red"),
        5: ("C", "bold white", "on bright_black"),
        6: ("A", "bold white", "on white"),
    }


    def render_grid(self, list2d: list[list[int]]):
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)

        window = _MainWindow()
        window.show()
        sys.exit(app.exec())
        
    def refresh_grid(self, list2d: list[list[int]]):
        pass

    def finalize_rendering(self):
        pass



