import sys
from typing import ClassVar

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)


class _ColorButton(QPushButton):

    def __init__(self, text: str, fg_color_name_or_hex: str, bg_color_name_or_hex: str):
        super().__init__()

        self.setFlat(True)
        self.setMinimumSize(50, 50)

        self.setText(text)

        # note that "border: none" was required for the style to work correctly
        self.setStyleSheet(_ColorButton.getStyleString(fg_color_name_or_hex, bg_color_name_or_hex))
        self.show()

    @classmethod
    def getStyleString(cls, fg_color_name_or_hex: str, bg_color_name_or_hex: str) -> str:
        return f"""
            QPushButton:!pressed {{
                color: {fg_color_name_or_hex}; 
                background-color: {bg_color_name_or_hex};
                border: none;
            }}
            QPushButton:pressed {{
                color: {fg_color_name_or_hex}; 
                background-color: {bg_color_name_or_hex};
                border: none;
            }}
        """


        
class _MainWindow(QMainWindow):

    def __init__(self, grid: QGridLayout):
        super().__init__()

        self.setWindowTitle("Wildfire")
        self.resize(400, 400)

        layout = QHBoxLayout()
        layout.addLayout(grid)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class QTRenderer:

    mapping: ClassVar[dict[int, tuple[str, str, str]]] = {
        1: (" ", "white", "black"),
        2: ("O", "white", "snow"),
        3: ("T", "white", "green"),
        4: ("F", "white", "red"),
        5: ("C", "white", "darkgray"),
        6: ("A", "white", "gray"),
    }

    def __init__(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        self.initialized = False

    def _create_console_grid(self, list2d: list[list[int]]) -> QGridLayout:
        for row in range(len(list2d)):
            for col in range(len(list2d[row])):
                char, fg, bg = QTRenderer.mapping.get(list2d[row][col], ("-", "white", "black"))
                if not self.initialized:
                    self.grid.addWidget(_ColorButton(char, fg, bg), row, col)
                else:
                    widget = self.grid.itemAtPosition(row, col).widget()
                    widget.setText(char)
                    widget.setStyleSheet(_ColorButton.getStyleString(fg, bg))

        self.initialized = True

        return self.grid

    def render_grid(self, list2d: list[list[int]]):
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)

        grid = self._create_console_grid(list2d)
        window = _MainWindow(grid)
        window.show()
        sys.exit(app.exec())
        
    def refresh_grid(self, list2d: list[list[int]]):
        self._create_console_grid(list2d)

    def finalize_rendering(self):
        pass



