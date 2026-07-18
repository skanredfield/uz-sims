import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "core"))

import threading
import queue

from src.core.config import Config
from src.core.clock import Clock
from src.core.engine import init_grid, sim_advance_state, gather_updateable
from gui.console_gui import ConsoleRenderer

config = Config()
grid = init_grid()
renderer = ConsoleRenderer()

config.is_deterministic = False

render_clock = Clock()
state_queue = queue.Queue(maxsize=5)
is_running_flag = threading.Event()
is_running_flag.set()


def run_logic_loop(is_running: threading.Event):
    logic_clock = Clock()
    
    while is_running.is_set():
        dt = logic_clock.tick(0.5)
        gather_updateable(grid)
        if not sim_advance_state(grid, config, dt):
            is_running.clear()
        state_queue.put(grid.tolist2d())


renderer.render_grid(grid.tolist2d())

logic_thread = threading.Thread(target=run_logic_loop, daemon=True, args=(is_running_flag,))
logic_thread.start()

while is_running_flag.is_set():
    while not state_queue.empty():
        try:
            current_grid = state_queue.get_nowait()
            renderer.refresh_grid(current_grid)
            state_queue.task_done()
        except queue.Empty:
            pass

    render_clock.tick(60)
