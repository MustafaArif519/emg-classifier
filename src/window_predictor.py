import numpy as np


class WindowPredictor:

    def WindowPredictor(self):
        self.trained = False
    
    def train(self, windows, labels):
        raise Exception("Implement train")

    def label_window(self, window):
        raise Exception("Implement label_window")
