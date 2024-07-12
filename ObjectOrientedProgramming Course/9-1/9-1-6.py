class HighScoreTable:

    def __init__(self, max_count):
        self.max_count = max_count
        self.scores = []

    def reset(self):
        self.scores = []

    def update(self, score):

        if self.scores:
            temp_list = sorted(list(self.scores + [score]), reverse=True)[:self.max_count]
            self.scores = temp_list
        else:
            self.scores.append(score)