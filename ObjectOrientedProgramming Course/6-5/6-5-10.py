class AdvancedTimer:

    def __init__(self):
        self.runs = []

    @property
    def min(self):
        if self.runs:
            return min(self.runs)
        return None

    @property
    def max(self):
        if self.runs:
            return max(self.runs)
        return None

    @property
    def last_run(self):
        if self.runs:
            return self.runs[-1]
        return None

    def __enter__(self):
        from time import perf_counter

        self.temp_counter_start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        from time import perf_counter

        self.temp_counter_end = perf_counter()
        self.runs.append(self.temp_counter_end - self.temp_counter_start)