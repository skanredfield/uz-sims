import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "core"))

import traceback

from gui.qt_gui import QTRenderer
from PySide6.QtCore import QSemaphore, QThread, Signal, Slot
from src.core.clock import Clock
from src.core.config import Config
from src.core.engine import gather_updateable, init_grid, sim_advance_state
from src.core.grid import Grid


class LogicThread(QThread):

    update_signal = Signal(int)
    
    def __init__(self, sem: QSemaphore, grid: Grid, config: Config, parent = None):
        super().__init__(parent)

        print("Initialized thread", flush=True)

        self.sem = sem
        self.grid = grid
        self.config = config

        self.logic_clock = Clock()


    def run(self):
        try:
            print("Thread", flush=True)
            while self.sem.tryAcquire():
                dt = self.logic_clock.tick(0.5)
                gather_updateable(self.grid)
                
                if sim_advance_state(self.grid, self.config, dt):
                    self.update_signal.emit(1)
                    self.sem.release()
                else:
                    self.update_signal.emit(0)
                    break
        except Exception as e:
            traceback.print_exc()


class QTEngineTest:

    def __init__(self):
        self.config = Config()
        self.grid = init_grid()
        self.renderer = QTRenderer()

        self.config.is_deterministic = False
        self.config.save_config()

        self.sem = QSemaphore(1)

    def start_test(self) -> None:

        self.logic_thread = LogicThread(self.sem, self.grid, self.config)
        self.logic_thread.update_signal.connect(self.update_ui)
        self.logic_thread.finished.connect(self.logic_thread.deleteLater)
        self.logic_thread.start()

        self.renderer.render_grid(self.grid.tolist2d())

    @Slot(int)
    def update_ui(self, val: int) -> None:
        print(f"Update with val: {val}")
        if val > 0:
            self.renderer.refresh_grid(self.grid.tolist2d())
        else:
            # TODO: finalize and quit
            pass


qtenginetest = QTEngineTest()
qtenginetest.start_test()

