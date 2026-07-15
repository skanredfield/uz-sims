import time


class Clock:

    def __init__(self):
        self.last_time = time.perf_counter()

    def tick(self, fps: float = 0) -> float:
        current_time = time.perf_counter()
        elapsed_seconds = current_time - self.last_time
        
        if fps > 0:
            target_period = 1.0 / fps
            remaining_time = target_period - elapsed_seconds
            
            if remaining_time > 0:
                time.sleep(remaining_time)
                current_time = time.perf_counter()
                elapsed_seconds = current_time - self.last_time

        self.last_time = current_time
        
        return elapsed_seconds
