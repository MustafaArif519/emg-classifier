import numpy as np


class WindowPredictor:

    def WindowPredictor(self):
        self.trained = False
    
    def train(self, windows, labels):
        self.trained = True

    def label_window(self, window):
        pass
