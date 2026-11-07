import sys
from typing import ClassVar

from PySide6.QtCore import Qt, QObject, Signal, Slot
from PySide6.QtGui import QPaintEvent, QMouseEvent, QPainter, QPen, QBrush, QColor
from PySide6.QtWidgets import (
    QSizePolicy,
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QBoxLayout
)


# class _ColorButton(QPushButton):

#     def __init__(self, text: str, fg_color_name_or_hex: str, bg_color_name_or_hex: str):
#         super().__init__()

#         self.setFlat(True)
#         self.setMinimumSize(10, 10)

#         self.setText(text)

#         # note that "border: none" was required for the style to work correctly
#         self.setStyleSheet(_ColorButton.getStyleString(fg_color_name_or_hex, bg_color_name_or_hex))
#         self.show()

#     @classmethod
#     def getStyleString(cls, fg_color_name_or_hex: str, bg_color_name_or_hex: str) -> str:
#         return f"""
#             QPushButton:!pressed {{
#                 color: {fg_color_name_or_hex}; 
#                 background-color: {bg_color_name_or_hex};
#                 border: none;
#             }}
#             QPushButton:pressed {{
#                 color: {fg_color_name_or_hex}; 
#                 background-color: {bg_color_name_or_hex};
#                 border: none;
#             }}
#         """

class _WindowBasedButtonsGrid(QWidget):

    mouse_click_signal = Signal(str)

    def __init__(self, num_rows: int, num_cols: int, gap_size: float):
        super().__init__()

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.gap_size = gap_size
        self.double_gap_size = gap_size * 2

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)

        pen = QPen(QColor("#EB5160"), self.gap_size, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        
        brush = QBrush(QColor(100, 150, 250, 128), Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)

        self.cell_width = self.width() / self.num_cols
        self.cell_height = self.height() / self.num_rows
        
        for i in range(self.num_cols):
            x = i * self.cell_width
            for j in range(self.num_rows):
                y = j * self.cell_height
                painter.drawRect(x + self.gap_size, y + self.gap_size, 
                                 self.cell_width - self.double_gap_size, self.cell_height - self.double_gap_size
                )

        painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        board_width = self.num_cols * (self.cell_width + self.gap_size) + self.double_gap_size
        board_height = self.num_rows * (self.cell_height + self.gap_size) + self.double_gap_size
        row = int(event.y() / (self.cell_height + self.gap_size))
        col = int(event.x() / (self.cell_width + self.gap_size))
        self.mouse_click_signal.emit(f"Mouse clicked at {row}, {col}")

        return super().mousePressEvent(event)

        
class _MainWindow(QMainWindow):

    def __init__(self, grid: _WindowBasedButtonsGrid):
        super().__init__()

        self.setWindowTitle("Wildfire")
        self.resize(400, 400)

        layout = QVBoxLayout()

        topPanel = QHBoxLayout()
        topPanel.addWidget(QLabel("Forest Fire Simulation"))
        topPanel.addWidget(QLabel("Barrier budget"))
        topPanel.addWidget(QLabel("Trees saved"))

        layout.addLayout(topPanel)

        centralPanel = QHBoxLayout()
        rightPanel = QVBoxLayout()
        rightPanel.setAlignment(Qt.AlignmentFlag.AlignTop)
        gridLayout = QVBoxLayout()
        gridLayout.addWidget(grid)
        centralPanel.addLayout(gridLayout)
        centralPanel.addLayout(rightPanel)
        layout.addLayout(centralPanel)

        grid.mouse_click_signal.connect(self.onCellClicked)

        rightPanel.addWidget(QPushButton("Assign smth..."))

        bottomPanel = QVBoxLayout()
        bottomUpperSubPanel = QHBoxLayout()
        bottomLowerSubPanel = QHBoxLayout()
        bottomPanel.addLayout(bottomUpperSubPanel)
        bottomPanel.addLayout(bottomLowerSubPanel)

        self.infoLabel = QLabel("Info text goes here...", margin=10)
        bottomUpperSubPanel.addWidget(self.infoLabel)

        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])
        bottomLowerSubPanel.addWidget(combobox)

        bottomLowerSubPanel.addWidget(QPushButton("Start Simulation"))
        bottomLowerSubPanel.addWidget(QPushButton("Stop"))
        layout.addLayout(bottomPanel)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @Slot(str)
    def onCellClicked(self, val):
        self.infoLabel.setText(val)

    def closeEvent(self, event):
        # TODO
        # if self.worker_thread.isRunning():
        #     self.worker_thread.quit() 
        #     self.worker_thread.wait() 
            
        event.accept()


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
        # self.grid = QVBoxLayout()
        # self.grid.setSiz(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # self.grid.setSpacing(5)
        self.initialized = False

    def _create_qt_grid(self, list2d: list[list[int]]) -> QGridLayout:
        self._window_based_buttons_grid = _WindowBasedButtonsGrid(len(list2d), len(list2d[0]), 5)
        # for row in range(len(list2d)):
            # for col in range(len(list2d[row])):
                # char, fg, bg = QTRenderer.mapping.get(list2d[row][col], ("-", "white", "black"))
                # if not self.initialized:
                    # self.grid.addWidget(_ColorButton(char, fg, bg), row, col)
                # else:
                
                    # widget = self.grid.itemAtPosition(row, col).widget()
                    # widget.setText(char)
                    # widget.setStyleSheet(_ColorButton.getStyleString(fg, bg))

        self.initialized = True


    def render_grid(self, list2d: list[list[int]]):
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)

        self._create_qt_grid(list2d)
        window = _MainWindow(self._window_based_buttons_grid)
        window.show()
        sys.exit(app.exec())
        
    def refresh_grid(self, list2d: list[list[int]]):
        # TODO: problem
        self._create_qt_grid(list2d)

    def finalize_rendering(self):
        pass



