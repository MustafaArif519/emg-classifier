import numpy as np

# what happens when window size changes?
# add variable to handle it?


class WindowPredictor:

    def WindowPredictor(self):
        self.trained = False
    
    def train(self, windows, labels):
        raise Exception("Implement train")

    def label_window(self, window):
        raise Exception("Implement label_window")
