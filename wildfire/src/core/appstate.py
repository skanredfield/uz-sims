class AppState:

    def __init__(self):
        self.grid_update_available = False
        self.simulation_finished = False

    def mark_update_available(self):
        self.grid_update_available = True

    def mark_updated(self):
        self.grid_update_available = False

    def mark_simulation_finished(self):
        self.simulation_finished = True